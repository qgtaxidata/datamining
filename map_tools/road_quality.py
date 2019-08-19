from db_tools import Quality,drop_table,Session,query_taxi_qua
from map_tools.network import Network
from geopy.distance import distance
from pygeohash import decode,encode
from geopy.distance import geodesic
from multiprocessing import Process,Queue
# from queue import Queue

class RoadQuality():
    def __init__(self,network=Network()):
        super().__init__()
        self.sentinel = object
        self.network = network
        network.load_map()
        self.d_gHash = network.d_gHash
        self.nodes = network.nodes
        self.records =network.records

    def match_dist(self,pos,road):
        '''将轨迹点匹配到道路上'''
        if (road[0][0] - road[1][0]) == 0 and (road[0][1] - road[1][1]) == 0 :return 100,0
        status = (road[0][0] - road[1][0]) == 0 #反转标志
        if status:
            pos = pos[::-1]
            road = (road[0][1],road[0][0]),(road[1][1],road[1][0])
        (x1, y1), (x2, y2) = road
        x , y = pos
        k = (y2 -y1)/(x2-x1)
        xp = (k**2*x1+k*y-k*y1+x)/(1+k**2)
        yp = k*(xp-x1) + y1
        if  status:
            pos_ = (xp, yp)
        else:
            pos = pos[::-1]
            pos_ = (yp, xp)
        dist = distance(pos,pos_).m
        return dist,pos_[::-1]
    def road_match(self,poss,det=10):
        '''
        :param poss: 轨迹数据
        :param d_ghash: 每个区对应的路口
        :param nodes:路口经纬度、路段信息
        :return:
        '''
        match = []
        # 加载轨迹点
        for pos in poss:
        # 通过gHash定位局部地图
            ghash = encode(pos[-1],pos[-2],7)
            if ghash not in self.d_gHash:continue   #出界
            inds = self.d_gHash[ghash]
        # 投影的方法匹配到路上
            l_dist = []
            s_road = set() #所有的路
            for i in inds:  #找出所有的路
                for r in self.nodes[i][0]:
                    if r not in s_road:
                        # print(r,self.records[r][-2],self.records[r][-1])
                        s_road.add(r)
                        dist,pos_ = self.match_dist(pos,(self.nodes[self.records[r][-2]][-2:],
                                                         self.nodes[self.records[r][-1]][-2:]))   #起末点经纬度
                       # print(dist)
                        if dist < det:
                            l_dist.append((dist,pos_,r))
            if l_dist:  #小于阈值的则认为是异常点
                match.append(min(l_dist,key=lambda x:x[0]))
        return match
    def road_match_one(self,pos,det=10):
        '''
        :param poss: 轨迹数据
        :param d_ghash: 每个区对应的路口
        :param nodes:路口经纬度、路段信息
        :return:
        '''
        # 加载轨迹点

        # 通过gHash定位局部地图
        t,*pos = pos
        ghash = encode(pos[-1],pos[-2],7)
        if ghash not in self.d_gHash: return None  # 出界
        inds = self.d_gHash[ghash]
        # 投影的方法匹配到路上
        l_dist = []
        s_road = set()  # 所有的路
        for i in inds:  # 找出所有的路
            for r in self.nodes[i][0]:
                if r not in s_road:
                    # print(r,self.records[r][-2],self.records[r][-1])
                    s_road.add(r)
                    dist, pos_ = self.match_dist(pos, (self.nodes[self.records[r][-2]][-2:],
                                                       self.nodes[self.records[r][-1]][-2:]))  # 起末点经纬度
                    # print(dist)
                    if dist < det:
                        l_dist.append((dist, pos_,t, r))
        if l_dist:  # 小于阈值的则认为是异常点
            return min(l_dist, key=lambda x: x[0])

    def to_db(self,q,table_itr,maxrq):
        while True:
            # *****多线程部分
            firstid = q.get()
            if firstid is self.sentinel:
                q.put(self.sentinel)
                break
            itr = query_taxi_qua(firstid, table_itr, maxrq)
            if itr is None:
                q.put(self.sentinel)
                break

            # *****数据转换部分
            d_match = {}
            for trace in itr:
                car,hour, *pos = trace
                rst = self.road_match_one(pos)  # 地图匹配
                if rst is None: continue
                if hour in d_match:
                    match = d_match[hour]
                    if car not in match:
                        match[car] = [rst]
                    else:
                        match[car].append(rst)
                else:
                    d_match[hour] = {car:[rst]}
            # print(firstid,d_match)

            # ****存入数据库部分
            # drop_table(Quality) #删除表
            # s.query(Quality).delete() #清空表
            s = Session()
            for h in d_match:  # 每辆车的轨迹
                for lst in d_match[h].values():
                    root_val = lst[0]
                    for i in range(1, len(lst)):
                        cur_val = lst[i]
                        if root_val[-1] != cur_val[-1]:  # 若是两个不同的路
                            # ****公式计算部分
                            root_val = cur_val
                            end_val = lst[i - 1]
                            r = end_val[-1]
                            det =  abs(root_val[-2].timestamp() -end_val[-2].timestamp())
                            if det == 0: continue
                            dist = geodesic((end_val[1][1], end_val[1][0]), (root_val[1][1], root_val[1][0])).m
                            if dist == 0: continue
                            length = self.records[r][0]
                            density = 1 / length * 41.67
                            det = det * length / dist
                            flow = len(lst)
                            # print(dist, length)

                            # ****存入数据库
                            qry = s.query(Quality).filter(Quality.rid == r)
                            inst = qry.first()
                            if inst is not None:
                                qry.update({'average_time': (float(inst.average_time) + det) / 2,'flow':inst.flow+flow,
                                          'density': (float(inst.density) + density),'count': inst.count + 1})
                            else:
                                s.add(Quality(rid=r,average_time=det,hour_repre=h,density=density,count=1,flow=flow,length=length))
                            s.commit()

            s.close()

    def to_db_1(self,q,table_itr,maxrq):
        while True:
            # *****多线程部分
            firstid = q.get()
            if firstid is self.sentinel:
                q.put(self.sentinel)
                break
            itr = query_taxi_qua(firstid, table_itr, maxrq)
            if itr is None:
                q.put(self.sentinel)
                break

            # *****数据转换部分
            d_match = {}
            for trace in itr:
                car, hour, *pos = trace
                rst = self.road_match_one(pos)  # 地图匹配
                if rst is None: continue
                if hour in d_match:
                    match = d_match[hour]
                    if car not in match:
                        match[car] = [rst]
                    else:
                        match[car].append(rst)
                else:
                    d_match[hour] = {car: [rst]}


def start_thread(num=10):
    # 队列的生产者、消费者模型
    from time import sleep
    tahle_itr =(13,)
    maxrq = 100000
    rq = RoadQuality()
    inq,outq = Queue(),Queue()
    cur_num = 0
    for i in range(num):
        print(i)
        thread = Process(target=rq.to_db,args=(inq,tahle_itr,maxrq))
        thread.start()
    print("开始")
    while True:
        if  inq.qsize() == 0:
            for i in range(num):
                inq.put((cur_num+i)*maxrq)
            cur_num += num
            print(cur_num)
        elif inq.qsize() == 1:
            rst = inq.get()
            if rst is rq.sentinel:
                break
            inq.put(rst)
        sleep(1)

if __name__ == '__main__':
    from myfunc import timethis
    road = RoadQuality()
    @timethis
    def a():
        start_thread(3)
    b = a()
