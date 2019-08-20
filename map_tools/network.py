from matplotlib.path import Path
from db_tools.base_table import  Nodes,Records,Session,Quality2
from pygeohash import encode,decode_exactly,northern,southern,eastern,western

class Network:
    def __init__(self):
        self.config()
        # self.load_map()  # 若报错，则路网没有导入数据库，先将句注释，再调用self.to_db(),结束后记得取消注释

    def config(self):
        self.d_gHash  = {}  #存放
        # 路网存入内存
        self.nodes = {}
        self.records = {} # 存储属性,[[*,fromNode,toNod]]
        self.adj_map = {}  # {node:[ind1,ind2]}

    def get_loacl_map(self,ghash1,ghash2):
        itr = (ghash1,ghash2)
        latu,*_ = decode_exactly(northern(itr))
        latl,*_ = decode_exactly(southern(itr))
        _,lonr,*_ = decode_exactly(eastern(itr))
        _,lonl,*_ = decode_exactly(western(itr))
        lonr += 0.2
        lonl -= 0.2
        latu += 0.2
        latl -= 0.2
        plogen = Path([(lonl,latl),(lonl,latu)
                          ,(lonr,latu),(lonr,latl)])
        allow = set()
        for i in self.d_gHash:
            info = decode_exactly(i)
            if plogen.contains_point((info[1],info[0])):
                allow.update(self.d_gHash[i])
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
        # return self.adj_map,self.nodes,self.records
        return adj_map,nodes,self.records

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
            self.records[r.id] = [float(r.length),50,0.6852578070969514,r.oneway,r.from_node,r.to_node] #求平均
        # for i in range(24):
        for q in s.query(Quality2):
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