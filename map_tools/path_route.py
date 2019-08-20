from map_tools.network import Network
from geopy.distance import distance
from pygeohash import encode
from map_tools.coordinate import wgs_gcj
import heapq
from time import time
class pathPlaning:
    def __init__(self,net=Network()):
        self.net = net
        net.load_map()
        self.d_gHash = net.d_gHash

    #路径规划代价函数
    def hdist(self,curNode, targetNode):
        '''当前点与目标点的哈曼顿距离'''
        return abs(self.nodes[curNode][1] - self.nodes[targetNode][1]) + \
               abs(self.nodes[curNode][2] - self.nodes[targetNode][2])
    #路径规划函数
    def load_map(self,args=None):

        if args is None:
            self.adj_map =self.net.adj_map
            self.nodes = self.net.nodes
            self.records = self.net.records
        orign,destination = args
        t1 = time()
        self.adj_map,self.nodes,self.records = self.net.get_loacl_map(encode(orign[1],orign[0],5),
                                                encode(destination[1],destination[0],5))
        print("局部地图耗时", time() - t1)
    def planing(self,demand,wtype=0):
        #[(lon,lat),(lon,lat)]

        closeQueue = []
        d_tmpcosts = {}
        gdist = {}  # 存放距离点的表
        orign,destination = demand
        startNode = self.node_match(orign)
        endNode = self.node_match(destination)
        print(startNode,endNode)
        if startNode == endNode:
            return [],0
        gdist[startNode] = 0
        d_tmpcosts[startNode] = (0,0)
        openQueue = [startNode]
        heapQueue = []
        heapq.heappush(heapQueue,(0,startNode)) #加入
        parentTable = {}  # 存放父节点的表
        while openQueue:
            curNode = heapq.heappop(heapQueue)[1]
            openQueue.remove(curNode)
            closeQueue.append(curNode)
            if curNode ==endNode:break    #找到路径
            nextNodeList = self.adj_map[curNode]           # 子节点的索引
            # 处理子节点
            for i in nextNodeList:
                nextNode =i[0];nextNodeIndex=i[1]
                if nextNode not in closeQueue:
                    if nextNode in openQueue:
                        if gdist[curNode] + self.records[nextNodeIndex][0] < gdist[nextNode]:
                            gdist[nextNode] = gdist[curNode] + self.records[nextNodeIndex][wtype]  # 更新子节点的距离
                            tmpcost = d_tmpcosts[curNode]
                            d_tmpcosts[nextNode] = (
                                self.records[nextNodeIndex][0]+tmpcost[0],self.records[nextNodeIndex][1]+tmpcost[1])   #距离时间
                            parentTable[nextNode] = (curNode,nextNodeIndex)  # 更新父节点
                    else:
                        dist = gdist[curNode] + self.records[nextNodeIndex][wtype]
                        gdist[nextNode] = dist # 更新子节点的距离
                        tmpcost = d_tmpcosts[curNode]
                        d_tmpcosts[nextNode] = (
                        self.records[nextNodeIndex][0] + tmpcost[0], self.records[nextNodeIndex][1] + tmpcost[1])  # 距离时间
                        parentTable[nextNode] = (curNode,nextNodeIndex)  # 更新父节点
                        openQueue.append(nextNode)
                        heapq.heappush(heapQueue,(dist,nextNode))
            # 从大到小排序
            # openQueue = sorted(openQueue, key=lambda k: gdist[k] + self.hdist(k,endNode),
            #                    reverse=True)
        if endNode != closeQueue[-1]:return [],None  #没找到路径
        pathIndex = []
        lastNode = closeQueue[-1]
        costs = [0,0]
        while True:
            if not parentTable.get(lastNode):
                break
            pos = self.nodes[parentTable[lastNode][0]][1:]
            pos = list(wgs_gcj(*pos))
            pathIndex.append(pos)
            lastNode = parentTable[lastNode][0]
        d,t = d_tmpcosts[endNode]
        d = round(d/1000,1)
        t = int(t/60)
        return pathIndex[::-1],(d,t)#gdist[endNode]  #[(lon,lat)]

    def node_match(self,pos):
        '''
        :param poss: 轨迹数据
        :param d_ghash: 每个区对应的路口
        :param nodes:路口经纬度、路段信息
        :return:
        '''
        match = []
        # 加载轨迹点

        # 通过gHash定位局部地图
        ghash = encode(pos[1],pos[0],7)
        if ghash not in self.d_gHash:return None    #出界
        inds = self.d_gHash[ghash]
        # 投影的方法匹配到路上
        l_dist = []
        for i in inds:  #找出所有的路
            pos_ = self.net.nodes[i][2],self.net.nodes[i][1]
            l_dist.append(distance(pos_,pos[::-1]).m)
        return inds[l_dist.index(min(l_dist))]


planing = pathPlaning()
def route_plan(origin,destination):
    paths = []
    costs = []
    planing.load_map((origin,destination))
    for i in range(3):
        path,cost = planing.planing([origin,destination],i)
        paths.append([origin]+path+[destination])
        costs.append(cost)
        print("规划路线数量:",len(path),"损失：",cost)
    return paths,costs


if __name__ =='__main__':
    def aa():
        p1 = [113.2507444, 23.1383689]
        p2 = [113.3010155, 23.2226661]
        a = route_plan(p1,p2)
        b =a[0][1]
        with open(('path.json'),'w') as f:
            f.write('[')
            for i in range(len(b)-1):
                f.write(str({'start':b[i],'end':b[i+1]})+',\n')
            f.write(']')
        return a
    # b = aa()


