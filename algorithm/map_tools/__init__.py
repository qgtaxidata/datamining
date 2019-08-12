import shapefile as shp
from db_tools.new_table import drop_table
from matplotlib.path import Path
import pandas as pd
from map_tools.coordinate import wgs_gcj
from db_tools.base_table import Nodes,Base,engine,NetworkSession,Records
# import geopandas as gpd
from shapely.geometry import Polygon
# 加载广州边界
from settings import G

#创建映射


# file = '../data/OSM_Roads/gis.osm_roads.shp'
# allow_codes = (5113,5114 ,5115 ,5122 ,5121,5123)  #允许的道路类型
# boundery = Path(G)

#
# def get_id(session,lon,lat):
#     return session.query(Nodes.id).filter(Nodes.longitude == lon).filter(Nodes.latitude == lat).first()
def insert_map():
    session = NetworkSession()
    lst = '['
    drop_table(Nodes, Base, engine)
    drop_table(Records, Base, engine)
    node_id = 0
    with shp.Reader(file, encoding='utf-8') as f:
        for col in f.iterShapeRecords():
            shape = col.shape
            points = shape.points
            if col.record.code in allow_codes:
                from_node = points[0]
                to_node = points[-1]
                if any(boundery.contains_points([from_node, to_node])):  # 只要有一个点在广州内
                    # 先查询站点是否在数据库内，再写入
                    record = col.record
                    itr = (from_node, to_node)
                    ids = []
                    for pos in itr:
                        id = get_id(session, *pos)
                        if not id:
                            node_id += 1
                            id = node_id
                            n = Nodes(id=id, osm_id=record.osm_id, longitude=pos[0], latitude=pos[1])
                            session.add(n)
                        else:
                            id = id[0]
                        ids.append(id)
                    r = Records(bridge=bool_map[record.bridge], oneway=bool_map[record.oneway],
                                tunnel=bool_map[record.tunnel],
                                ref=record.ref, name=record.name, code=record.code, fclass=record.fclass,
                                from_node=ids[0], to_node=ids[1])
                    lst = lst + str(
                        {"start": wgs_gcj(from_node[1], from_node[0])[::-1], "end": wgs_gcj(to_node[1], to_node[0])[::-1]}) + ',\n'
                    session.add(r)
                    session.commit()
        session.close()
    with open('lst.json', 'w') as f:
        f.write(lst + ']')
#
#
#
#
# insert_map()
# lst = ''
#
# #地图测试
# m = len(G)
# for i in range(m-1):
#     lst =  lst + str({"start":wgs_gcj(G[i][1],G[i][0])[::-1], "end": wgs_gcj(*G[i+1][::-1])[::-1]}) +',\n'
# lst += ']'
# with open('lst2.json','w') as f:
#     f.write(lst)
#
#
# def expore():
#     '''属性探索'''
#     shapes = shp.Shapes([])
#     records = []
#     n = 0
#     with shp.Reader(file,encoding='utf-8') as f:
#         for col in f.iterShapeRecords():
#             n+=1
#             if n>1000:break
#             shape = col.shape
#             points = shape.points
#             shapes.append(col.shape)
#             records.append(col.record.as_dict())
#     #col = ['bridge','code','fclass','layer','name','oid','oneway','osm_id','ref','tunnel']
#     a = {'bridge':'是否桥','oneway':'是否单向路','tunnel':'是否隧道','ref':'有道路信息'}
#     df = pd.DataFrame(records)
#     df.set_index('osm_id',inplace=True)
#
#     for i in ('bridge','oneway','tunnel'):
#         print(df[i].value_counts())
# # expore()
# # if __name__ == '__main__':
# #     p = Polygon(G)
# #     s = gpd.GeoSeries(p)
#

