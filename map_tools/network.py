import shapefile as shp
from matplotlib.path import Path
from map_tools.coordinate import wgs_gcj
from db_tools.base_table import  Nodes,Records,Session,drop_table,Base,engine,Quality
import json
import heapq
import numpy as np
from pygeohash import encode,decode_exactly,northern,southern,eastern,western
from geopy.distance import distance
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
def dist_sta():
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.rcParams['axes.unicode_minus'] = False
    from geopy.distance import distance
    dist = {}
    for s,record in net.itrRecord():
        code = record.code
        # 筛选
        if code in net.allow_codes:
            p1 = s.points[-1]
            p2 = s.points[0]
            d = (int(distance(p1[::-1],p2[::-1]).m))
            num = 10**(len(str(d))-1)
            d = int(int(d)/num)* num
            dist[d] = dist.get(d,0) + 1
    plt.scatter(list(dist.keys()),list(dist.values()))
    plt.show()
    return dist

class Network:
    def __init__(self,f='../data/OSM_Roads/gis.osm_roads.shp'):
        self.f = f
        from settings import G
        self.boundery = Path(G)
        self.config()
        # self.load_map()  # 若报错，则路网没有导入数据库，先将句注释，再调用self.to_db(),结束后记得取消注释

    def itrRecord(self):
        # 拿到迭代器
        with shp.Reader(self.f,encoding='utf-8') as f:
            for col in f.iterShapeRecords():
                yield col.shape,col.record
    def config(self):
        self.allow_codes = (5113,5114 ,5115 ,5122 ,5121,5123)  #允许的道路类型
        self.d_level = {}   #存放每一级道路对应的索引
        self.d_nid = {} #{node_id:ind}
        self.d_err_nodes = {}  # 存放每一级道路对应的索引
        self.rid = 0
        self.nid = 0
        self.d_gHash  = {}  #存放
        self.gzErr = []
        self.bool_map = {'T': True, 'F': False, 'B': True}  #用于加载地图
        # 路网存入内存
        self.nodes = {}
        self.records = {} # 存储属性,[[*,fromNode,toNod]]
        self.adj_map = {}  # {node:[ind1,ind2]}
    def check_id(self):
        pass

    def get_loacl_map(self,ghash1,ghash2):
        itr = (ghash1,ghash2)
        latu,*_ = decode_exactly(northern(itr))
        latl,*_ = decode_exactly(southern(itr))
        _,lonr,*_ = decode_exactly(eastern(itr))
        _,lonl,*_ = decode_exactly(western(itr))
        lonr += 0.05
        lonl -= 0.05
        latu += 0.05
        latl -= 0.05
        print(latl,latu,lonr,lonl)
        plogen = Path([(lonl,latl),(lonl,latu)
                          ,(lonr,latu),(lonr,latl)])
        allow = set()
        for i in self.d_gHash:
            info = decode_exactly(i)
            if plogen.contains_point((info[1],info[0])):
                allow.update(self.d_gHash[i])
        print(len(allow))
        nodes,adj_map = {},{}
        for n in allow:
            if n not in nodes:
                nodes[n] = self.nodes[n]
                adj_map[n] = self.adj_map[n]
            for to_node,_ in self.adj_map[n]:
                if to_node not in nodes:
                    nodes[to_node] = self.nodes[n]
                    adj_map[to_node] = self.adj_map[to_node][:]
                    for i,(tt,_) in enumerate(self.adj_map[to_node]):
                        if tt not in allow:
                            adj_map[to_node].remove((tt,_))
        return adj_map,nodes,self.records

        # s = Session()
        # # nodes表
        # for n in s.query(Nodes):
        #     if n.geohash7 in allow:
        #         if n.nid not in self.nodes:
        #             self.nodes[n.nid] = [[n.rid],float(n.longitude),float(n.latitude)]
        #         else:
        #             self.nodes[n.nid][0].append(n.rid)
        # # records表
        # for r in s.query(Records):
        #     if r.from_node in allow or r.to_node in allow:
        #         self.records[r.id] = [float(r.length),0,0,r.oneway,r.from_node,r.to_node]
        # # for i in range(24):
        # for q in s.query(Quality):
        #     if q.rid in self.records:
        #         a_time = float(q.average_time)
        #         density = float(q.density)
        #         if self.records[q.rid][1] == 0:
        #             self.records[q.rid][1] += a_time
        #         else:
        #             self.records[q.rid][1] =(a_time+self.records[q.rid][1] )/2
        #         if self.records[q.rid][2] == 0:
        #             self.records[q.rid][2] = density
        #         else:
        #             self.records[q.rid][2] = (self.records[q.rid][2] +density) /2
        # self.adj_map = self.trans_map(self.records.keys())
        return self.adj_map,self.nodes,self.records



    def query_geohash(self):
        s = Session()
        for id,ghash in s.query(Nodes.nid,Nodes.geohash7).all():
            self.d_gHash[ghash] = self.d_gHash.get(ghash,[]) + [id]
        return self.d_gHash
    def trans_map(self,i_lst):
        adj_map = {}
        for i in i_lst:
            # 双向路
            record = self.records[i]  # 第j条记录
            fromNode = record[-2]
            toNode = record[-1]
            adj_map[fromNode] = adj_map.get(fromNode, []) + [(toNode, i)]
            adj_map[toNode] = adj_map.get(toNode, []) + [(fromNode, i)]
            # 路的信息
        return adj_map
    def load_map(self):
        s = Session()
        # gHase映射
        self.query_geohash()
        # nodes表
        for n in s.query(Nodes):
            if n.nid not in self.nodes:
                self.nodes[n.nid] = [[n.rid],float(n.longitude),float(n.latitude)]
            else:
                self.nodes[n.nid][0].append(n.rid)
        # records表
        for r in s.query(Records):
            self.records[r.id] = [float(r.length),0,0,r.oneway,r.from_node,r.to_node]
        # for i in range(24):
        for q in s.query(Quality):
            a_time = float(q.average_time)
            density = float(q.density)
            if self.records[q.rid][1] == 0:
                self.records[q.rid][1] += a_time
            else:
                self.records[q.rid][1] =(a_time+self.records[q.rid][1] )/2
            if self.records[q.rid][2] == 0:
                self.records[q.rid][2] = density
            else:
                self.records[q.rid][2] = (self.records[q.rid][2] +density) /2
        self.adj_map = self.trans_map(self.records.keys())
        return self.adj_map,self.nodes
    def connecty_check(self,records=None):
        # 连通性检测,返回不连通的点
        '''连通性检查'''
        records = list(self.records.values()) if records is None else records
        dict_ = {}  # 未连通的路
        visited = set(records[0][-2:])  # 已连通的路网,传销组织
        # visited = set(recodes[1200][-2:])  # 已连通的路网,传销组织
        # recodes_ = recodes[:]
        # recodes_.pop(1200)
        for road in records[1:]:  # 对每条路
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
        # if len(dict_) > 0:
            # print("未连通")
            # print('可用路口：', len(visited), '不可用路口:', len(dict_))
            # print(dict_.keys())
        # else:
        #     print("连通", len(visited))
        return visited, dict_.keys()  # 返回不连通的点
    def to_db(self,allow_codes):
        '''地图入库'''
        # 更新
        #self.config()
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
                if from_pos == to_pos:continue #几率很小
                itr = (from_pos,to_pos)
                if any(self.boundery.contains_points(itr)):
                    self.rid += 1
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
                        n = Nodes(nid=node,rid=self.rid, longitude=pos[0],geohash7=encode(pos[1],pos[0],7),
                                    latitude=pos[1],geohash5=encode(pos[1],pos[0],5))
                        session.add(n)
                        l_node.append(node)
                    # 计算路段的长度
                    length = 0
                    m = len(points)
                    points = [(p[1],p[0]) for p in points]
                    for i in range(m-1):
                        length += distance(points[i],points[i+1]).m
                    r = Records(bridge=self.bool_map[record.bridge], oneway=self.bool_map[record.oneway],
                                tunnel=self.bool_map[record.tunnel],
                                ref=record.ref, name=record.name, code=record.code, fclass=record.fclass,
                                length=length,from_node=l_node[0], to_node=l_node[1])
                    session.add(r)
                    record.extend(l_node)   #加入属性
            session.commit()
        session.close()

        def to_mem(self, allow_codes):
            # 1. 筛选地图并存进文件
            # 更新
            d_geohash = {}  # [{pos:[lon,lat],geohash:geohash}},]   !!
            lst = '['
            d_pos = {}  # {(lon,lat):node}
            # adj_map = {}    #{node:[ind1,ind2]}
            for i, (shape, record) in enumerate(self.itrRecord()):
                points = shape.points
                code = record.code
                # 筛选
                if code in allow_codes:
                    from_pos = points[0]
                    to_pos = points[-1]
                    itr = (from_pos, to_pos)
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
                                # ghash = encode(*from_pos,5)
                                # if ghash in d_geohash:
                                #     d_geohash[ghash].append(wgs_gcj(*from_pos[::-1])[::-1])
                                # else:
                                #     d_geohash[ghash] = [wgs_gcj(*to_pos[::-1])[::-1]]
                                self.nid += 1
                                node = self.nid
                                d_pos[pos] = node
                            l_node.append(node)
                        record.extend(l_node)  # 加入属性
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
            # print("点数量",len(nodes))
            print("最大id", self.nid)


# 连通性检查****************
# def get_re(nodes):
#     s_re = set()  # 路线去重
#     records = []
#     for i in nodes:
#         for r in net.nodes[i][0]:
#             if r not in s_re:
#                 s_re.add(r)
#                 records.append(net.records[r])
#     return records
# def coon_test(n=5,records=None):
#     records = list(net.records.values()) if records is None else records
#     while (n):
#         n -= 1
#         conn, non = net.connecty_check(records)
#         print("连通",len(conn),"未连通",len(non))
#         records = get_re(non)
#     return conn,non



# 步骤一：将小于50米的点合并
# 步骤二：将小于50米的点连接
class Connecty(Network):
    # 连通性修改****************
    # 注意，内存的修改并不全面，仅仅是为了测试，修改后的地图需要重新导入
    def modify_dist(self,allow,non):
        '''获取破碎的子网中每个点，与路网的最小距离'''
        l_allow = list(allow)
        dist = []
        node_to_m = []
        nodes = non
        for n in nodes:
            p1 = self.nodes[n][2], self.nodes[n][1]
            ghash = encode(self.nodes[n][2],self.nodes[n][1],5)   #
            match_nodes = set(self.d_gHash[ghash])  #区域中的点
            to_reps = list(match_nodes & allow)
            if not to_reps:continue
            lst = []
            for a in to_reps:
                p2 = self.nodes[a][2], self.nodes[a][1]
                lst.append(distance(p1, p2).m)
            minVal = min(lst)
            dist.append(minVal)
            node_to_m.append(l_allow[lst.index(minVal)])
        return dist,node_to_m
    def modify_filter(self,n,a ,deat,de):
        '''测试合并数量'''
        records = {}
        for i in self.records:
            records[i] = self.records[i][:]
        for to_n, r in self.adj_map[n]:
            records[r][records[r].index(n)] = a
        conn, b = self.connecty_check(list(records.values()))
        det = len(conn) - deat
        if det > de:
            print("实际减少路口数:", det,end='  ')
            self.bind_node(n,a)
            return True,det
        print("实际减少路口数:", det, end='  ')
        return False,det
    def bind_node(self,to_del,to_rep):
        '''
        :param self:
        :param node_to_rep:代替的点
        :param node_to_del: 删除的点
        :return: None
        '''
        s = Session()
        # print("修改对象",to_del)
        del self.nodes[to_del]
        for to_node, r in self.adj_map[to_del]:
            ind = self.records[r].index(to_del)
            self.records[r][ind] = to_rep
            self.adj_map[to_rep].append((to_node,r))
            self.nodes[to_rep][0].append(r)
            for i,(from_node,_) in enumerate(self.adj_map[to_node]):
                if from_node == to_del:
                    self.adj_map[to_node][i] = to_rep,r
                    break
            q = s.query(Records).filter(Records.id==r)
            # qr = q.first()
            if ind - len(self.records[r]) == -2:
                q.update({'from_node':to_rep})
            else:
                q.update({'to_node':to_rep})
        s.query(Nodes).filter(Nodes.nid==to_del).delete()
        s.commit()
        s.close()

        return
    def add_record(self,dist,to_add,to_rep):
        r = max(self.records.keys())+1
        self.records[r] = [dist,10,0.5,False,to_rep,to_add]
        self.records[r+1] = [dist, 10, 0.5,False,to_add,to_rep]
        self.adj_map[to_rep].append((to_add,r))
        self.adj_map[to_add].append((to_rep, r+1))
        self.nodes[to_add][0].extend([r,r+1])
        self.nodes[to_rep][0].extend([r, r + 1])
        s = Session()
        s.add(Records(id=r,bridge=False,oneway=False,tunnel=False,ref='',name=''
                      ,code=0,fclass='',length=dist,from_node=to_rep,to_node=to_add))
        s.add(Records(id=r+1,bridge=False,oneway=False,tunnel=False,ref='',name=''
                      ,code=0,fclass='',length=dist,from_node=to_add,to_node=to_rep))
        s.commit()
        s.close()
    def del_record(self,to_del):
        s =Session()
        print(to_del)
        for _,r in self.adj_map[to_del]:
            if r in self.records:
                del self.records[r]
            s.query(Records).filter(Records.id==r).delete()
        s.query(Nodes).filter(Nodes.nid==to_del).delete()
        s.commit()
        s.close()

    # 连通性检查****************
    def get_re(self,nodes):
        s_re = set()  # 路线去重
        records = []
        for i in nodes:
            for r in self.nodes[i][0]:
                if r not in s_re:
                    s_re.add(r)
                    records.append(self.records[r])
        return records
    def conn_batch(self,n=1e4, records=None,best=False):
        '''返回每一批连通的集合'''
        records = list(self.records.values()) if records is None else records
        l_conn  = []  # 存放每一批连通的点
        while (n):
            n -= 1
            if not  records:break
            conn, non = net.connecty_check(records)
            l_conn.append(conn)
            # print("连通", len(conn), "未连通", len(non))
            records = self.get_re(non)
        l_conn.sort(key=lambda x:len(x),reverse=True)
        if best:
            return l_conn[0]
        else:
            return l_conn

    def modify_map(self,n=1):
        # 策略：小于50米进行合并，大于则进行连接/删除
        # 筛选出路口最大的一批路网
        def run(conn,batch):
            err = []
            for non in batch:
                print(len(batch), batch.index(non))  # xpath
                deat = len(conn)
                # 简单考虑对最近的进行合并
                rst = self.modify_dist(conn, non)
                dist, node_to_m = rst
                if not dist:
                    err.append(non)
                    continue
                s_del = set()
                for small in heapq.nsmallest(n, dist):
                    # print("距离",small)
                    ind = dist.index(small)
                    to_del = list(non)[ind]
                    to_rep = node_to_m[ind]
                    if small < 50:
                        s_del.add(to_del)
                        self.bind_node(to_del, to_rep)
                    else:
                        self.add_record(small,to_del,to_rep)
                conn |= non ^ s_del
                # aa, bb = self.connecty_check(self.get_re(conn))
                # print("连通", len(aa), "未连通", len(bb),end='  ')
            return conn,err

        batch = self.conn_batch()
        if not batch:return
        conn,err = run(batch[0],batch[1:])
        out_status,pre_err = 3,0
        while err and  out_status:
            conn,err = run(conn,err)
            # 跳出死循环
            if pre_err == len(err):
                out_status -= 1
            else:
                pre_err = len(err)
                out_status = 3
        for non in err: #删除无法改变的点
            for node in non:
                self.del_record(node)
        a,b = self.connecty_check()
        print("连通数",len(a),'未连通数',len(b))
        return n

    def load(self):
        import json
        with open('../data/dist.json') as f:
            nsmall = json.load(f)
            small = nsmall[0]



if __name__ == '__main__':
    file = '../data/OSM_Roads/gis.osm_roads.shp'
    net = Network(file)
    net.load_map()
    # import time
    # a = net.road_match([[113.31739,23.209]])
    # a = dist_sta()
    # a,b = net.load_map()
    # net.query_geohash()
    # 写入数据库
    # from myfunc import timethis
    # @timethis
    # def to_db():
    #     net.to_db(net.allow_codes)
    # # to_db()
    #
    # # 连通性检查，修改
    # c = Connecty()
    # c.load_map()
    # c.modify_map(1)

    # 添加geohash7
    # net.load_map()
    # from pygeohash import encode
    # s = Session()
    # import  random
    # for n,lst in net.records.items():
    #     n1,n2 = lst[-2:]
    #     lon,lat = net.nodes[n1][1:]
    #     lon1, lat1 = net.nodes[n2][1:]
    #     ghash5 = encode(lat,lon,5)
    #     ghash51 = encode(lat1, lon1, 5)
    #     ghash5 = random.choice([ghash5,ghash51])
    #     q = s.query(Records).filter(Records.id == n)
    #     q.update({"geohash5":ghash5})
    # s.commit()
    # s.close()
