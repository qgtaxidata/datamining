import numpy as np
import math
PI = math.pi

pi = math.pi
a = 6378245.0
ee = 0.00669342162296594323


arr = ["ws0kz","ws0m6","ws0my","ws0t9","ws0tg","ws0mw",
"ws0sc","ws0kt","ws0sf","ws0te","ws0mk","ws0ts",
"ws0m5","ws0mp","ws0mm","ws0w4","ws0m4",
"ws0kq","ws0t1","ws0m7","ws0t2","ws0mt","ws0w1",
"ws0tf","ws0tv","ws0mq","ws0t3","ws0tt","ws0mj","ws0tc",
"ws0kg","ws0mr","ws0w3","ws0mz","ws0mv","ws0sb",
"ws0km","ws0t8","ws0ku","ws0tb","ws0td","ws0w6",
"ws0mx","ws0t6","ws0kw","ws0mh","ws0kf","ws0t4",
"ws0kv","ws0tu","ws0t0","ws0ky","ws0mn",
"ws0c8","ws0b2","ws0c0","ws0c1","ws09q","ws09e",
"ws0cb","ws08z","ws0b6","ws0c7","ws0d5","ws0c5",
"ws0c6","ws0b9","ws0bf","ws0b3", "ws0c3","ws0dj",
"ws09y","ws09z","ws09p","ws0dh","ws09w","ws0b8",
"ws09n","ws0dm","ws0bd","ws09x", "ws0c4","ws09u",
"ws0bc","ws0bb","ws0c9","ws09t","ws0b7","ws0d7",
"ws08y","ws0cc","ws09g","ws0dk","ws09s","ws09v",
"ws0be","ws09r","ws0c2","ws0bg",
"ws0vs", "ws0ut", "ws0vw", "ws0v0", "ws0vy", "ws0ur", "ws0ym", "ws0gg", "ws0gy", "ws1h3", "ws1jb", "ws1hf", "ws0vr",
 "ws0v5", "ws0gb", "ws0yh", "ws0uk", "ws0vh", "ws1j3", "ws0uh", "ws0ud", "ws0uq", "ws0vv", "ws0vk", "ws0us", "ws0yq",
 "ws1j2", "ws0vx", "ws1h8", "ws0g9", "ws0v2", "ws0g8", "ws0u9", "ws0u5", "ws0uz", "ws0vz", "ws0v4", "ws0uj", "ws0u3",
 "ws0v6", "ws0uy", "ws0vu", "ws0un", "ws1j4", "ws0yn", "ws1hc", "ws0v3", "ws0ux", "ws0u1", "ws0uv", "ws0g3", "ws1h9",
 "ws0vt", "ws1h6", "ws1j6", "ws1j8", "ws0u6", "ws0g2", "ws1hd", "ws0u8", "ws0ug", "ws0u4", "ws0vm", "ws0v1", "ws1h2",
 "ws0gf", "ws0gu", "ws0gv", "ws0vq", "ws0uw", "ws0uc", "ws1j1", "ws0vj", "ws0yk", "ws0vp", "ws0gc", "ws0vn", "ws0uu",
 "ws1hb", "ws0u7", "ws0v7", "ws0u2", "ws0yj", "ws1j0", "ws0ub", "ws0ue", "ws0u0", "ws0um", "ws0uf",
"ws1pc", "ws0ws", "ws0zp", "ws0z6", "ws0yu", "ws0wt", "ws1p0", "ws0zd", "ws0y7", "ws1pd", "ws300", "ws0y4", "ws1p1",
 "ws0yv", "ws0zn", "ws0vd", "ws0zm", "ws1nb", "ws0wm", "ws0vf", "ws0y1", "ws0zu", "ws0wk", "ws0y5", "ws0yw", "ws304",
 "ws1p3", "ws1p8", "ws0vc", "ws0yt", "ws0we", "ws0y3", "ws301", "ws0y0", "ws1pb", "ws0w5", "ws1pf", "ws0wv", "ws0zt",
 "ws0ze", "ws0zy", "ws0v8", "ws0ty", "ws0zq", "ws0ys", "ws2bj", "ws0wn", "ws0yf", "ws2bp", "ws0v9", "ws1p4", "ws0z5",
 "ws1p9", "ws2bh", "ws0zx", "ws0wu", "ws0yy", "ws0vb", "ws0z7", "ws0y6", "ws0zs", "ws0tw", "ws0yz", "ws0yg", "ws0wp",
 "ws0zj", "ws0zz", "ws0wj", "ws0zw", "ws0zh", "ws0vg", "ws1p6", "ws0yx", "ws1n8", "ws0wh", "ws0yd", "ws0tz", "ws0wq",
 "ws1p2", "ws0zr", "ws0tx", "ws0y2", "ws0zv", "ws0ye", "ws0zk", "ws0w7", "ws0z4", "ws2bn", "ws0wg", "ws0wr", "ws0ve"
"ws0d1", "ws0d9", "ws0dp", "ws0d6", "ws0dr", "ws0d4", "ws0dd", "ws0dc", "ws0dv", "ws0dn", "ws0d3", "ws0dx", "ws0dw",
 "ws0de", "ws0en", "ws0ej", "ws0ds", "ws0dg", "ws0e4", "ws0eh", "ws0dt", "ws0du", "ws0dq", "ws0e1", "ws0dz", "ws0dy",
 "ws0df", "ws0e5", "ws0ep",
"ws0sm", "ws0kx", "ws0s6", "ws0ef", "ws0s0", "ws0sk", "ws0tj", "ws0t5", "ws0sr", "ws0sd", "ws0s7", "ws0kp", "ws0sg",
 "ws0eb", "ws0tm", "ws0se", "ws0s2", "ws0th", "ws0s1", "ws0st", "ws07z", "ws0sx", "ws0s8", "ws0ec", "ws0ss", "ws0sq",
 "ws0sw", "ws0su", "ws0tk", "ws0sv", "ws0t7", "ws0s3", "ws0s4", "ws0s9", "ws0kr",
"ws0tp", "ws0ey", "ws0tn", "ws0ex", "ws0tq", "ws0sy", "ws0er", "ws0eq", "ws0ew", "ws0tr", "ws0sp", "ws0ez", "ws0sn", "ws0sz",
"ws0e8","ws0e2",
"ws0ee", "ws0em", "ws0et", "ws0e9", "ws0e7", "ws0ed", "ws0es", "ws0ek", "ws0e6", "ws0e3",
"ws0eu", "ws0sh", "ws0s5", "ws0ev", "ws0sj", "ws0eg",
"ws07r","ws07x"
]
# sum_lng = 0
# sum_lat = 0
max_lng = -1
min_lng = np.inf
max_lat = -1
min_lat = np.inf
for a in area:
    if a[0] > max_lng:
        max_lng = a[0]
    if a[0] < min_lng:
        min_lng = a[0]
    if a[1] > max_lat:
        max_lat = a[1]
    if a[1] < min_lat:
        min_lat = a[1]

def gcj02_to_wgs84(coordinates):
    """
    GCJ-02转WGS-84
    :param coordinates: GCJ-02坐标系的经度和纬度的numpy数组
    :returns: WGS-84坐标系的经度和纬度的numpy数组
    """
    ee = 0.006693421622965943  # 偏心率平方
    a = 6378245  # 长半轴
    lng = coordinates[:, 0]
    lat = coordinates[:, 1]
    is_in_china = (lng > 73.66) & (lng < 135.05) & (lat > 3.86) & (lat < 53.55)
    _transform = coordinates[is_in_china]  # 只对国内的坐标做偏移

    dlat = _transformlat(_transform)
    dlng = _transformlng(_transform)
    radlat = _transform[:, 1] / 180 * PI
    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = np.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * PI)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * PI)
    mglat = _transform[:, 1] + dlat
    mglng = _transform[:, 0] + dlng
    coordinates[is_in_china] = np.array([
        _transform[:, 0] * 2 - mglng, _transform[:, 1] * 2 - mglat
    ]).T
    return coordinates
def _transformlat(coordinates):
    lng = coordinates[:, 0] - 105
    lat = coordinates[:, 1] - 35
    ret = -100 + 2 * lng + 3 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * np.sqrt(np.fabs(lng))
    ret += (20 * np.sin(6 * lng * PI) + 20 *
            np.sin(2 * lng * PI)) * 2 / 3
    ret += (20 * np.sin(lat * PI) + 40 *
            np.sin(lat / 3 * PI)) * 2 / 3
    ret += (160 * np.sin(lat / 12 * PI) + 320 *
            np.sin(lat * PI / 30.0)) * 2 / 3
    return ret
def _transformlng(coordinates):
    lng = coordinates[:, 0] - 105
    lat = coordinates[:, 1] - 35
    ret = 300 + lng + 2 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * np.sqrt(np.fabs(lng))
    ret += (20 * np.sin(6 * lng * PI) + 20 *
            np.sin(2 * lng * PI)) * 2 / 3
    ret += (20 * np.sin(lng * PI) + 40 *
            np.sin(lng / 3 * PI)) * 2 / 3
    ret += (150 * np.sin(lng / 12 * PI) + 300 *
            np.sin(lng / 30 * PI)) * 2 / 3
    return ret

area_list1 = np.array([[max_lng, max_lat], [min_lng,  min_lat]])
area_list2 = np.array([[(max_lng + min_lng) / 2, (max_lat + min_lat) / 2]])
print(area_list1)
print(area_list2)

