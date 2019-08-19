from map_tools.network import Network
from geopy.distance import distance
from pygeohash import encode
from map_tools.coordinate import wgs_gcj

class pathPlaning:
    def __init__(self,net=Network()):
        self.net = net
        # self.records =net.records
        # self.adj_map =net.adj_map
        # self.nodes = net.nodes
        self.d_gHash = net.d_gHash
    #路径规划代价函数
    def hdist(self,curNode, targetNode):
        '''当前点与目标点的哈曼顿距离'''
        return abs(self.nodes[curNode][1] - self.nodes[targetNode][1]) + \
               abs(self.nodes[curNode][2] - self.nodes[targetNode][2])
    #路径规划函数
    def planing(self,demand,wtype=0):
        #[(lon,lat),(lon,lat)]
        from time import time
        closeQueue = []
        gdist = {}  # 存放距离点的表
        orign,destination = demand
        startNode = planing.node_match(orign)
        endNode = planing.node_match(destination)
        print(startNode,endNode)
        if startNode == endNode:
            return [],0
        t1 = time()
        self.adj_map,self.nodes,self.records = self.net.get_loacl_map(encode(orign[1],orign[0],5),
                                                encode(destination[1],destination[0],5))
        print(time()-t1)
        print(self.adj_map)
        gdist[startNode] = 0
        openQueue = [startNode]
        parentTable = {}  # 存放父节点的表
        while openQueue:
            curNode = openQueue.pop()
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
                            parentTable[nextNode] = (curNode,nextNodeIndex)  # 更新父节点
                    else:
                        gdist[nextNode] = gdist[curNode] + self.records[nextNodeIndex][wtype]  # 更新子节点的距离
                        parentTable[nextNode] = (curNode,nextNodeIndex)  # 更新父节点
                        openQueue.append(nextNode)
            # 从大到小排序
            openQueue = sorted(openQueue, key=lambda k: gdist[k] + self.hdist(k,endNode),
                               reverse=True)
        if endNode != closeQueue[-1]:return [],None  #没找到路径
        pathIndex = []
        lastNode = closeQueue[-1]
        while True:
            if not parentTable.get(lastNode):
                break
            pos = self.nodes[parentTable[lastNode][0]][1:]
            pos = list(wgs_gcj(*pos))
            pathIndex.append(pos)
            lastNode = parentTable[lastNode][0]
        return pathIndex[::-1],gdist[endNode]  #[(lon,lat)]

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


def route_plan(origin,destination):
    net = Network()
    net.load_map()
    print('开始')
    planing = pathPlaning(net)
    paths = []
    costs = []
    for i in range(3):
        path,cost = planing.planing([origin,destination],i)
        print(path,cost)
        paths.append(path)
        costs.append(cost)
    return paths,costs


if __name__ =='__main__':
    net = Network()
    net.load_map()
    planing = pathPlaning(net)

    from myfunc import timethis
    @timethis
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
    b = aa()


