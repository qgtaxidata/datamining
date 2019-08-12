"""
Douglas-Pecucker算法
Douglas-Peucker算法常用于轨迹压缩，典型步骤如下：
1.在曲线首尾两点A，B之间连接一条直线AB，该直线为曲线的弦
2.计算离弦AB距离最远的点与最大距离
3.比较最大距离与阈值，若小于阈值则舍弃该点，以AB弦作为曲线的近似
4.若大于阈值，则以此点将曲线划分成两段，并对两段曲线分别进行1-3步操作
"""

import math

def Rad(d):
    return d*math.pi / 180

def Geodist(point1,point2):
    """
    返回两个点之间的距离
    :param point1:第一个点
    :param point2:第二个点
    :return:
    """
    radLat1 = Rad(point1[1])
    radLat2 = Rad(point2[1])
    delta_lon = Rad(point1[0] - point2[0])
    top_1 = math.cos(radLat2) * math.sin(delta_lon)
    top_2 = math.cos(radLat1) * math.sin(radLat2) - math.sin(radLat1) * math.cos(radLat2) * math.cos(delta_lon)
    top = math.sqrt(top_1 * top_1 + top_2 * top_2)
    bottom = math.sin(radLat1) * math.sin(radLat2) + math.cos(radLat1) * math.cos(radLat2) * math.cos(delta_lon)
    delta_sigma = math.atan2(top, bottom)
    distance = delta_sigma * 6378137.0

    return round(distance,3)

def get_vertical_dist(pointA,pointB,pointX):
    """返回点X与弦AB的垂直距离"""

    a=math.fabs(Geodist(pointA,pointB))
    #当弦两端重合时,点到弦的距离变为点间距离
    if a==0:
        return math.fabs(Geodist(pointA,pointX))
    b=math.fabs(Geodist(pointA,pointX))
    c=math.fabs(Geodist(pointB,pointX))
    p=(a+b+c)/2
    S=math.sqrt(math.fabs(p*(p-a)*(p-b)*(p-c)))
    vertical_dist=S*2/a
    return vertical_dist

def DP_compress(point_list,output_point_list,Dmax):
    """按照阈值Dmax将压缩后的point_list输出到output_point_list中"""
    start_index=0
    end_index=len(point_list)-1

    #起止点必定是关键点,但是作为递归程序此步引入了冗余数据,后期必须去除
    output_point_list.append(point_list[start_index])
    output_point_list.append(point_list[end_index])

    if start_index<end_index:
        index=start_index+1        #工作指针,遍历除起止点外的所有点
        max_vertical_dist=0        #路径中离弦最远的距离
        key_point_index=0        #路径中离弦最远的点,即划分点

        while(index<end_index):
            cur_vertical_dist=get_vertical_dist(point_list[start_index],point_list[end_index],point_list[index])
            if cur_vertical_dist>max_vertical_dist:
                max_vertical_dist=cur_vertical_dist
                key_point_index=index        #记录划分点
            index+=1

        #递归划分路径
        if max_vertical_dist>=Dmax:
            DP_compress(point_list[start_index:key_point_index],output_point_list,Dmax)
            DP_compress(point_list[key_point_index:end_index],output_point_list,Dmax)

def get_MeanErr(point_list,output_point_list):
    Err=0

    start_index=0
    end_index=len(output_point_list)-1

    while(start_index<end_index):        #遍历所有关键点
        #选取两相邻关键点
        pointA_id=int(output_point_list[start_index][2])
        pointB_id=int(output_point_list[start_index+1][2])

        id=pointA_id+1        #工作指针,用于遍历非关键点
        while(id<pointB_id):        #遍历两关键点之间的非关键点
            Err+=get_vertical_dist(output_point_list[start_index],output_point_list[start_index+1],point_list[id])
            id+=1

        start_index+=1

    return Err/len(point_list)




point_list=[]
output_point_list=[]

point_list = [[123.23, 23.123], []]

DP_compress(point_list,output_point_list,Dmax=30)
output_point_list=list(set(output_point_list))        #去除递归引入的冗余数据
output_point_list=sorted(output_point_list,key=lambda x:x[2])        #按照id排序

#将压缩数据写入输出文件
fd=open(r".\output.txt",'w')
for point in output_point_list:
    fd.write("{},{},{}\n".format(point[2],point[0],point[1]))
fd.close()
