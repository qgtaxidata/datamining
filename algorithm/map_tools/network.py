import shapefile as shp
from matplotlib.path import Path
from map_tools.coordinate import wgs_gcj
from db_tools.base_table import  Nodes,Records,Session,drop_table,Base,engine
import json
import numpy as np
from pygeohash import encode,decode
# 存储索引、检查连通性，内存存储
# 先考虑在内存进行连通性检查
# 使用一个文件暂时存储信息

def hash_bar():
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.rcParams['axes.unicode_minus'] = False
    dic =  net.query_geohash()
    names = dic.keys()
    x = range(len(names))
    y = [len(v) for v in dic.values()]
    plt.bar(x,y)
    plt.title("广州每个gHase包含的Node（路口）数量")
   # plt.xlabel(names)
    plt.show()

class Network:
    def __init__(self,f):
        self.f = f
        from settings import G
        self.boundery = Path(G)
        self.config()

    def itrRecord(self):
        # 拿到迭代器
        with shp.Reader(self.f,encoding='utf-8') as f:
            for col in f.iterShapeRecords():
                yield col.shape,col.record
    def config(self):
        self.tmp_file = 'tmp.py'
        self.allow_codes = (5113,5114 ,5115 ,5122 ,5121,5123)  #允许的道路类型
        self.d_level = {}   #存放每一级道路对应的索引
        self.d_nid = {} #{node_id:ind}
        self.d_err_nodes = {}  # 存放每一级道路对应的索引
        self.nid = 0
        self.d_gHash  = {}  #存放
        with open('../data/g_boundery.txt','r') as f:
            self.gZone = [[]] * 11
            gG = json.load(f)
            for z in gG['features']:
                coors = z['geometry']['coordinates'][0][0]
                self.gZone.append(Path(coors))
        self.gzErr = []
        self.bool_map = {'T': True, 'F': False, 'B': True}  #用于加载地图

        # 路网存入内存
        self.nodes = []
        self.records = []  # 存储属性,[[*,fromNode,toNod]]
        self.adj_map = {}  # {node:[ind1,ind2]}
    def check_id(self):
        pass

    def query_geohash(self):
        s = Session()
        for id,ghash in s.query(Nodes.id,Nodes.geohash5).all():
            self.d_gHash[ghash] = self.d_gHash.get(ghash,[]) + [id]
        return self.d_gHash
    def trans_map(self,i_lst):
        adj_map = {}
        gProperty = np.zeros((len(i_lst),4))    # [id,osm_id,lon,lat]
        for j, i in enumerate(i_lst):
            # 双向路
            record = self.records[i]  # 第j条记录
            fromNode = record[-2]
            toNode = record[-1]
            adj_map[fromNode] = adj_map.get(fromNode, []) + [(toNode, j)]
            adj_map[toNode] = adj_map.get(toNode, []) + [(fromNode, j)]
            # 路的信息
            gProperty[j, :] = self.nodes[i]
        return adj_map,gProperty
    def load_map(self):
        s = Session()
        # gHase映射
        self.query_geohash()
        # nodes表
        for n in s.query(Nodes):
            self.nodes.append([n.id,n.osm_id,n.longitude,n.latitude])
        # records表
        for r in s.query(Records):
            self.records.append([r.oneway,r.from_node,r.to_node])
        #self.adj_map,_ = self.trans_map(range(len(self.nodes)))
        return self.adj_map,self.nodes
    def connecty_check(self,recodes):
        # 连通性检测,返回不连通的点
        '''连通性检查'''
        dict_ = {}  # 未连通的路
        visited = set(recodes[0][-2:])  # 已连通的路网,传销组织
        for road in recodes[1:]:  # 对每条路
            # if road[3] not in [5]:continue
            sNode = road[-2]  # 起点
            eNode = road[-1]  # 终点
            if sNode in visited or eNode in visited:  # 夫妻一人被骗
                visited.add(sNode)
                visited.add(eNode)  # 都遭殃
                stack = [sNode, eNode]
                while stack:  # dbs坑爹
                    node = stack.pop()
                    if node in dict_.keys():
                        father = dict_.get(node)
                        del dict_[node]  # 删除
                        for i in father:
                            visited.add(i)  # 加入传销组织
                            stack.append(i)
            else:
                dict_[sNode] = dict_.get(sNode, []) + [eNode]
                dict_[eNode] = dict_.get(eNode, []) + [sNode]
        if len(dict_) > 0:
            print("未连通")
            print('可用路线：', len(visited) / 2, '不可用路线:', len(dict_) / 2)
            print(dict_.keys())
            return dict_.keys()  # 返回不连通的点
        else:
            print("连通", len(visited))
            return None
    def to_db(self,allow_codes):
        '''地图入库'''
        # 更新
        session = Session()
        drop_table(Nodes,Base,engine=engine)
        drop_table(Records, Base, engine=engine)
        d_pos = {}  #{(lon,lat):node}   ，用于去重
        for i,(shape,record) in enumerate(self.itrRecord()):
            # if i == 100:break
            points = shape.points
            code = record.code
            # 筛选
            if code in allow_codes:
                from_pos = points[0]
                to_pos = points[-1]
                itr = (from_pos,to_pos)
                if any(self.boundery.contains_points(itr)):
                    # 分级存储索引
                    if code in self.d_level:
                        self.d_level[code].append(i)
                    else:
                        self.d_level[code] = [i]
                    l_node = []
                    # 存储路网
                    for pos in itr:
                        if pos in d_pos:
                            # 单向路判断?
                            node = d_pos[pos]
                        else:
                            # ind = self.get_gZone(pos)
                            # if ind is not None:
                            #     self.gZone[ind].append(pos)
                            self.nid += 1
                            node = self.nid
                            d_pos[pos] = node
                            n = Nodes(id=node, osm_id=record.osm_id, longitude=pos[0],
                                    latitude=pos[1],geohash5=encode(pos[1],pos[0],5))
                            session.add(n)
                        l_node.append(node)
                    r = Records(bridge=self.bool_map[record.bridge], oneway=self.bool_map[record.oneway],
                                tunnel=self.bool_map[record.tunnel],
                                ref=record.ref, name=record.name, code=record.code, fclass=record.fclass,
                                from_node=l_node[0], to_node=l_node[1])
                    session.add(r)
                    record.extend(l_node)   #加入属性
            session.commit()
        session.close()
    def to_mem(self,allow_codes):
        # 1. 筛选地图并存进文件
        # 更新
        d_geohash = {}    #[{pos:[lon,lat],geohash:geohash}},]   !!
        lst = '['
        d_pos = {}  #{(lon,lat):node}
        # adj_map = {}    #{node:[ind1,ind2]}
        for i,(shape,record) in enumerate(self.itrRecord()):
            points = shape.points
            code = record.code
            # 筛选
            if code  in allow_codes:
                from_pos = points[0]
                to_pos = points[-1]
                itr = (from_pos,to_pos)
                if any(self.boundery.contains_points(itr)):

                    #分级存储索引
                    if code in self.d_level:
                        self.d_level[code].append(i)
                    else:
                        self.d_level[code] = [i]
                    l_node = []
                    # 存储路网
                    for pos in itr:
                        if pos in d_pos:
                            # 单向路判断?
                            node = d_pos[pos]
                        else:
                            # ind = self.get_gZone(pos)
                            # if ind is not None:
                            #     self.gZone[ind].append(pos)
                            # ghash = encode(*from_pos,5)
                            # if ghash in d_geohash:
                            #     d_geohash[ghash].append(wgs_gcj(*from_pos[::-1])[::-1])
                            # else:
                            #     d_geohash[ghash] = [wgs_gcj(*to_pos[::-1])[::-1]]
                            self.nid += 1
                            node = self.nid
                            d_pos[pos] = node
                        l_node.append(node)
                    record.extend(l_node)   #加入属性
                    self.records.append(record)
                    # from_node,to_node = l_node
                    # if from_node in adj_map:  #不需要邻接表
                    #     adj_map[from_node].append((to_node,i))
                    # else:
                    #     adj_map[from_node] = [(to_node,i)]
        # 连通性检查
        # with open('level1.json', 'w') as f:
        #     f.write(lst + ']')
        with open('g_level1.json', 'w') as f:
            f.write(str(d_geohash))
        self.connecty_check(self.records)
        #print("点数量",len(nodes))
        print("最大id",self.nid)

guangzhou_geohash5 =['ws0b0', 'ws0kz', 'ws0f6', 'ws083', 'ws10d', 'ws0c8', 'ws0vs', 'ws0ut', 'ws1pc', 'ws0m6', 'ws0fq', 'ws0ws', 'ws0cp', 'ws0zp', 'ws0gw', 'ws0d1', 'ws0z6', 'ws07t', 'ws09c', 'ws0my', 'ws0vw', 'ws143', 'ws0xp', 'ws0g1', 'ws0v0', 'ws0t9', 'ws0w0', 'ws0bk', 'ws0g7', 'ws0vy', 'ws0z9', 'ws0w9', 'ws281', 'ws1n0', 'ws025', 'ws08m', 'ws0bn', 'ws0sm', 'ws02r', 'ws0fz', 'ws03r', 'ws119', 'ws157', 'ws0kx', 'ws0gt', 'ws0tg', 'ws0ur', 'ws0ym', 'ws0gp', 'ws0xx', 'ws08v', 'ws0f2', 'ws0yu', 'ws0wt', 'ws0cu', 'ws0fu', 'ws0gg', 'ws0qx', 'ws1p0', 'ws117', 'ws145', 'ws0zb', 'ws0mw', 'ws0gy', 'ws085', 'ws0zd', 'ws1h3', 'ws0x4', 'ws11d', 'ws0b2', 'ws0tp', 'ws0y7', 'ws0xw', 'ws0wd', 'ws1jb', 'ws1p7', 'ws0qy', 'ws08g', 'ws1hf', 'ws07q', 'ws0d9', 'ws0vr', 'ws0fe', 'ws1n7', 'ws092', 'ws0qk', 'ws0cs', 'ws1pd', 'ws06w', 'ws08b', 'ws114', 'ws0cr', 'ws06h', 'ws03q', 'ws0dp', 'ws0sc', 'ws300', 'ws0y4', 'ws1p1', 'ws0fk', 'ws0xg', 'ws0yv', 'ws22n', 'ws1j9', 'ws0v5', 'ws0d6', 'ws0zn', 'ws14e', 'ws08e', 'ws08u', 'ws06y', 'ws15f', 'ws0wb', 'ws2b0', 'ws1h1', 'ws03v', 'ws0vd', 'ws0zg', 'ws0b1', 'ws0ey', 'ws0xr', 'ws1h7', 'ws0zm', 'ws0rx', 'ws0kt', 'ws0xf', 'ws1n1', 'ws08w', 'ws1nd', 'ws0ru', 'ws10c', 'ws0e8', 'ws07e', 'ws0ee', 'ws284', 'ws1h4', 'ws0s6', 'ws1nb', 'ws0wm', 'ws109', 'ws0fx', 'ws0bq', 'ws0vf', 'ws06v', 'ws0c0', 'ws0gb', 'ws0yh', 'ws0uk', 'ws02d', 'ws0x9', 'ws1n6', 'ws065', 'ws06r', 'ws0dr', 'ws0y1', 'ws0zu', 'ws03x', 'ws0wk', 'ws0kd', 'ws0fr', 'ws08k', 'ws0cg', 'ws0xs', 'ws0c1', 'ws0r6', 'ws0sf', 'ws0vh', 'ws0bh', 'ws0te', 'ws1j3', 'ws0bm', 'ws0rp', 'ws0y5', 'ws0rg', 'ws07x', 'ws0f5', 'ws09q', 'ws02u', 'ws02g', 'ws0fh', 'ws0uh', 'ws0ud', 'ws09e', 'ws0xb', 'ws088', 'ws15c', 'ws0yw', 'ws0uq', 'ws0kn', 'ws0fd', 'ws03d', 'ws0cb', 'ws102', 'ws0fb', 'ws141', 'ws0vv', 'ws159', 'ws0br', 'ws0qj', 'ws304', 'ws0qe', 'ws1p3', 'ws08z', 'ws0ef', 'ws0qp', 'ws1ng', 'ws0bu', 'ws03s', 'ws0b6', 'ws158', 'ws0ww', 'ws0c7', 'ws225', 'ws1p8', 'ws11c', 'ws0vk', 'ws1h0', 'ws03g', 'ws110', 'ws0mk', 'ws0gq', 'ws112', 'ws0vc', 'ws1hg', 'ws0s0', 'ws0fj', 'ws0yt', 'ws10e', 'ws0mu', 'ws0x8', 'ws0us', 'ws0fm', 'ws0yq', 'ws06z', 'ws0we', 'ws0ts', 'ws1j2', 'ws03p', 'ws0d5', 'ws02m', 'ws0c5', 'ws0vx', 'ws280', 'ws28p', 'ws0sk', 'ws101', 'ws103', 'ws06m', 'ws1h8', 'ws0m5', 'ws0q5', 'ws0y3', 'ws0xe', 'ws1je', 'ws0tj', 'ws301', 'ws0y8', 'ws0c6', 'ws0mp', 'ws0d4', 'ws086', 'ws0mm', 'ws03k', 'ws0g9', 'ws0w4', 'ws0b9', 'ws0kj', 'ws146', 'ws0db', 'ws0y0', 'ws0em', 'ws0et', 'ws0v2', 'ws0m4', 'ws1n9', 'ws06e', 'ws0rd', 'ws0bf', 'ws096', 'ws0g8', 'ws0dd', 'ws08h', 'ws0b3', 'ws1pb', 'ws08s', 'ws0c3', 'ws0u9', 'ws0qn', 'ws0kq', 'ws02y', 'ws0t1', 'ws0m7', 'ws06f', 'ws06t', 'ws0dc', 'ws0u5', 'ws081', 'ws0t2', 'ws0gk', 'ws03y', 'ws0mt', 'ws104', 'ws0w5', 'ws0w1', 'ws0dj', 'ws07f', 'ws037', 'ws09y', 'ws0tf', 'ws089', 'ws0e2', 'ws027', 'ws0g4', 'ws1pf', 'ws0ms', 'ws0tn', 'ws08c', 'ws1j7', 'ws0z0', 'ws0uz', 'ws0tv', 'ws149', 'ws0ry', 'ws09d', 'ws0b5', 'ws095', 'ws0vz', 'ws0wv', 'ws035', 'ws0ex', 'ws0fw', 'ws0eu', 'ws08x', 'ws0xm', 'ws0tq', 'ws07r', 'ws07g', 'ws0v4', 'ws0d8', 'ws0rf', 'ws0uj', 'ws02p', 'ws0sy', 'ws0dv', 'ws07j', 'ws09h', 'ws066', 'ws1h5', 'ws0qf', 'ws0u3', 'ws0z2', 'ws02j', 'ws0t5', 'ws0v6', 'ws09z', 'ws0dn', 'ws1nc', 'ws0e9', 'ws03w', 'ws07m', 'ws0rk', 'ws09p', 'ws0zt', 'ws02h', 'ws10f', 'ws100', 'ws0w2', 'ws075', 'ws0gs', 'ws02f', 'ws0sr', 'ws0uy', 'ws0d3', 'ws0gh', 'ws0sd', 'ws0ze', 'ws22j', 'ws0dh', 'ws1he', 'ws0vu', 'ws0x0', 'ws0zy', 'ws08t', 'ws0dx', 'ws087', 'ws118', 'ws09w', 'ws0un', 'ws0v8', 'ws0fg', 'ws0s7', 'ws111', 'ws0dw', 'ws1j4', 'ws0ty', 'ws0yn', 'ws0b8', 'ws1hc', 'ws0kp', 'ws0de', 'ws0en', 'ws0f8', 'ws0cz', 'ws0re', 'ws0mf', 'ws144', 'ws0yb', 'ws06q', 'ws11b', 'ws0v3', 'ws06n', 'ws0er', 'ws305', 'ws07h', 'ws0fc', 'ws0ux', 'ws09n', 'ws080', 'ws0sg', 'ws0f4', 'ws0fy', 'ws02z', 'ws0e7', 'ws0rj', 'ws0xn', 'ws1pg', 'ws02n', 'ws0wf', 'ws0u1', 'ws0rm', 'ws0uv', 'ws0qw', 'ws036', 'ws0zq', 'ws0g3', 'ws15g', 'ws0mq', 'ws0yc', 'ws0ej', 'ws0q6', 'ws0f3', 'ws0f9', 'ws0gd', 'ws0eb', 'ws0ys', 'ws0bj', 'ws0r4', 'ws2bj', 'ws0t3', 'ws155', 'ws0bz', 'ws1h9', 'ws0wn', 'ws0dm', 'ws0bd', 'ws0tm', 'ws0tt', 'ws0vt', 'ws0yf', 'ws06s', 'ws076', 'ws0w8', 'ws0gz', 'ws1nf', 'ws08q', 'ws0mj', 'ws077', 'ws0ks', 'ws08f', 'ws0tc', 'ws2bp', 'ws1h6', 'ws03n', 'ws07p', 'ws0kg', 'ws0gj', 'ws0x7', 'ws142', 'ws0k4', 'ws15b', 'ws0mr', 'ws0v9', 'ws1p4', 'ws03j', 'ws0x3', 'ws09x', 'ws07y', 'ws0qs', 'ws0g5', 'ws0bx', 'ws1j6', 'ws0rq', 'ws0rz', 'ws0qr', 'ws098', 'ws0k5', 'ws0c4', 'ws0z5', 'ws0w3', 'ws0qh', 'ws0se', 'ws06k', 'ws0me', 'ws0md', 'ws14c', 'ws1j8', 'ws0sh', 'ws0wy', 'ws0ft', 'ws02t', 'ws0z8', 'ws0u6', 'ws02x', 'ws0cd', 'ws0g2', 'ws0gn', 'ws03f', 'ws0cq', 'ws09u', 'ws0s2', 'ws0mz', 'ws08j', 'ws0ds', 'ws0bc', 'ws0ed', 'ws1p9', 'ws1hd', 'ws153', 'ws0th', 'ws0ch', 'ws2bh', 'ws0u8', 'ws07w', 'ws094', 'ws0mv', 'ws0cx', 'ws2b5', 'ws0r7', 'ws06d', 'ws0ug', 'ws0zx', 'ws22p', 'ws10g', 'ws0ce', 'ws0by', 'ws0cy', 'ws0qz', 'ws03u', 'ws0u4', 'ws0dg', 'ws09f', 'ws14b', 'ws0vm', 'ws03e', 'ws0ge', 'ws07u', 'ws0s1', 'ws0wu', 'ws28n', 'ws0es', 'ws0bt', 'ws097', 'ws0yp', 'ws0xh', 'ws0wc', 'ws0up', 'ws150', 'ws0v1', 'ws0yy', 'ws0gr', 'ws0vb', 'ws0k7', 'ws15d', 'ws0zf', 'ws1h2', 'ws0z1', 'ws0s5', 'ws0st', 'ws0gf', 'ws0e4', 'ws0sb', 'ws1jd', 'ws0z7', 'ws0eq', 'ws0km', 'ws0y6', 'ws0zs', 'ws0bb', 'ws06j', 'ws07z', 'ws0eh', 'ws0tw', 'ws22h', 'ws0ck', 'ws09j', 'ws0gu', 'ws115', 'ws113', 'ws03m', 'ws02k', 'ws0gv', 'ws0vq', 'ws0yr', 'ws0sx', 'ws064', 'ws0rv', 'ws07n', 'ws1n3', 'ws0dt', 'ws0t8', 'ws152', 'ws11e', 'ws0f7', 'ws0x5', 'ws0yz', 'ws0xu', 'ws0ku', 'ws02w', 'ws0c9', 'ws0s8', 'ws1jg', 'ws0uw', 'ws0uc', 'ws0rh', 'ws067', 'ws0tb', 'ws10b', 'ws0xq', 'ws1p5', 'ws105', 'ws0ec', 'ws1j1', 'ws093', 'ws0yg', 'ws0ss', 'ws0wp', 'ws108', 'ws09t', 'ws0td', 'ws0ek', 'ws0vj', 'ws0sq', 'ws0zj', 'ws06u', 'ws0sw', 'ws03h', 'ws07d', 'ws0d2', 'ws0qt', 'ws0zz', 'ws148', 'ws0ew', 'ws0x6', 'ws0su', 'ws0wz', 'ws0du', 'ws0qm', 'ws0tr', 'ws224', 'ws0b7', 'ws0yk', 'ws0dq', 'ws0wj', 'ws0ke', 'ws107', 'ws0r5', 'ws0vp', 'ws0e1', 'ws14d', 'ws0w6', 'ws0zw', 'ws0gc', 'ws0q7', 'ws0kh', 'ws0xd', 'ws06x', 'ws147', 'ws0vn', 'ws1j5', 'ws0fs', 'ws0gx', 'ws0ev', 'ws06g', 'ws0gm', 'ws14f', 'ws0cn', 'ws116', 'ws0uu', 'ws0xz', 'ws0bw', 'ws0zh', 'ws0vg', 'ws0q4', 'ws1hb', 'ws1p6', 'ws0d7', 'ws0yx', 'ws08y', 'ws0sj', 'ws0sp', 'ws28j', 'ws11g', 'ws0cw', 'ws14g', 'ws090', 'ws285', 'ws09k', 'ws0u7', 'ws074', 'ws0rr', 'ws0cm', 'ws0tk', 'ws08d', 'ws02v', 'ws1n2', 'ws154', 'ws0rt', 'ws091', 'ws0qg', 'ws0dz', 'ws026', 'ws0dy', 'ws024', 'ws0rs', 'ws1n8', 'ws0wh', 'ws0qq', 'ws02s', 'ws0yd', 'ws0cc', 'ws0e0', 'ws09g', 'ws0eg', 'ws0tz', 'ws1jc', 'ws0wq', 'ws0rw', 'ws0xj', 'ws0dk', 'ws0xy', 'ws0bs', 'ws0k6', 'ws11f', 'ws0sv', 'ws0df', 'ws0g0', 'ws07s', 'ws0e5', 'ws0t7', 'ws0x2', 'ws106', 'ws0mx', 'ws02e', 'ws0ct', 'ws0t6', 'ws1p2', 'ws0v7', 'ws084', 'ws2b1', 'ws0u2', 'ws0yj', 'ws0zr', 'ws0fn', 'ws02q', 'ws0e6', 'ws0wx', 'ws0qu', 'ws0qv', 'ws082', 'ws0tx', 'ws0y9', 'ws0kw', 'ws1j0', 'ws1n4', 'ws09s', 'ws07k', 'ws0ff', 'ws0y2', 'ws034', 'ws0cv', 'ws28h', 'ws0zv', 'ws0ez', 'ws0qd', 'ws0b4', 'ws03z', 'ws07v', 'ws0xt', 'ws0e3', 'ws0kk', 'ws0mh', 'ws0f1', 'ws0z3', 'ws0ye', 'ws0zc', 'ws1n5', 'ws09v', 'ws0cf', 'ws0ub', 'ws0zk', 'ws140', 'ws08n', 'ws0kf', 'ws0sn', 'ws0xc', 'ws0be', 'ws1pe', 'ws09r', 'ws0ue', 'ws099', 'ws0fp', 'ws0f0', 'ws0g6', 'ws0s3', 'ws08p', 'ws0bv', 'ws0t4', 'ws0c2', 'ws0kv', 'ws0sz', 'ws0w7', 'ws0rn', 'ws0u0', 'ws0xv', 'ws0bg', 'ws03t', 'ws0tu', 'ws0s4', 'ws151', 'ws0s9', 'ws0um', 'ws1jf', 'ws2b4', 'ws0z4', 'ws0xk', 'ws0d0', 'ws0bp', 'ws0cj', 'ws0fv', 'ws0ep', 'ws156', 'ws0mg', 'ws09m', 'ws2bn', 'ws0kr', 'ws0t0', 'ws0x1', 'ws09b', 'ws0wg', 'ws0wr', 'ws08r', 'ws15e', 'ws06p', 'ws0ky', 'ws0mn', 'ws1ne', 'ws0uf', 'ws0ve']

def get_gZone():
    err = []
    ghash_to_write = [[],[],[],[],[],[],[],[],[],[],[]]
    ghash_str = [[], [], [], [], [], [], [], [], [], [], []]
    names = []
    with open('../data/g_boundery.txt', 'r') as f:
        gZ = {}
        gZone = []
        gG = json.load(f)
        for z in gG['features']:
            coors = z['geometry']['coordinates'][0][0]
            name =  z['properties']['name']
            names.append(name)
            gZone.append(Path(coors))
    for ghash in guangzhou_geohash5:
        count = []
        for i,z in enumerate(gZone):
            pos = decode(ghash)[::-1]
            #生成四个点
            delta = 0.01
            pos1 = (pos[0] + delta, pos[1])
            pos2 = (pos[0] - delta, pos[1])
            pos3 = (pos[0], pos[1] - delta)
            pos4 = (pos[0], pos[1] + delta)
            num = 0
            for p in (pos1,pos2,pos3,pos4):
                if z.contains_point(p):
                    num += 1
            count.append(num)
        max_count = max(count)
        if max_count:
            ind = count.index(max_count)

            if names[ind] in gZ:
                gZ[names[ind]].append(ghash)
            else:
                gZ[names[ind]] = [ghash]
            ghash_to_write[ind].append(wgs_gcj(*decode(ghash)[::-1]))
            ghash_str[ind].append(ghash)
        else:
            err.append(wgs_gcj(*decode(ghash)[::-1]))
    # for i in range(11):
    #     with open(f'gZones{i}.json','w') as f:
    #         # input(ghash_to_write[i])
    #         json.dump(ghash_to_write[i],f)
    #     with open(f'geoHase{i}.json','w') as f:
    #         json.dump(ghash_str[i],f)
    # lst = []
    # for i in ghash_to_write:
    #     lst += i
    # with open('gZones_all.json', 'w') as f:
    #     json.dump(lst, f)
    #
    # with open('gZones_err.json', 'w') as f:
    #     # input(ghash_to_write[i])
    #     json.dump(err, f)

    return gZ,gG
def get_gHase():
    lst = []
    for hash in guangzhou_geohash5:
        lst.append(wgs_gcj(*decode(hash)[::-1]))
    with open('gHase.json','w') as f:
        json.dump(lst,f)
# 边集数据可视化
def boundury_view():
    lst = []
    with open('../data/g_boundery.txt', 'r') as f:
        gZone = []
        gG = json.load(f)
        for j,z in enumerate(gG['features']):
            coors = z['geometry']['coordinates'][0][0]
            coors = [wgs_gcj(*d )for d in coors]
            # input(coors)
            for i in range(len(coors)-1):
                lst.append({'start':coors[i],'end':coors[i+1],'count':j})
            gZone.append(Path(coors))
    with open('gZone.json','w') as f:
        json.dump(lst,f)

# boundury_view()
if __name__ == '__main__':
    file = '../data/OSM_Roads/gis.osm_roads.shp'
    net = Network(file)
    a,b = net.load_map()
    # net.query_geohash()
    #net.to_db(net.allow_codes)
    # a,b = get_gZone()
    # get_gHase()
    # n = 0
    # for i in a:
    #     print(len(i))
    #     n += len(i)
    # print(n,len(guangzhou_geohash5))


# json 格式
# lst = lst + str(
#     {"start": wgs_gcj(from_pos[1], from_pos[0])[::-1],
#      "end": wgs_gcj(to_pos[1], to_pos[0])[::-1]}) + ',\n'