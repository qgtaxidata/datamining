from db_tools.base_table import *
_engine = create_engine('mysql+pymysql://qgtaxi:qgtaxi_2018@10.21.48.11/operate_his') #,echo=True ,print执行的sql
_Session = sessionmaker(bind=_engine)
_Base = declarative_base(bind=_engine)

def drop_table(cls,Base,engine):
    try:
        cls.__table__.drop(engine)
    except:
        pass
    Base.metadata.create_all(engine)
# 根据原来数据创建新的表
def new_muti_operate(table_itr=range(3, 5),table_base='operate_his',class_base = '_Operate',):
    #删除原有表格
    drop_table(Operate,Base,engine)
    # 多个映射表
    for i in table_itr:
        exec(f'''class {class_base}{i}(BaseOperate,_Base):
        __tablename__ = "{table_base}{i}"''')
    _session = _Session()
    session = Session()
    for i in table_itr:
        c = eval(class_base+str(i))   #映射单个表的类
        for col in _session.query(c).filter(c.GET_ON_LATITUDE != 0).filter(c.GET_ON_LATITUDE != 0).all():
            col = Operate(WORK_BEGIN_TIME=col.WORK_BEGIN_TIME,GET_ON_LONGITUDE=col.GET_ON_LONGITUDE,
                           GET_ON_LATITUDE=col.GET_ON_LATITUDE,GEOHASH5=col.GEOHASH5,GEOHASH7=col.GEOHASH7,
                          WORK_END_TIME=col.WORK_END_TIME,UNIT_PRICE=col.UNIT_PRICE)
            session.add(col)
    session.commit()
    session.close()
    _session.close()
    return True

def new_muti_operate_params(table_itr=range(3, 5),table_base='operate_his',class_base = '_Operate',):
    #删除原有表格
    drop_table(OperateParams,Base,engine)
    # 多个映射表
    for i in table_itr:
        exec(f'''class {class_base}{i}(BaseOperate,_Base):
        __tablename__ = "{table_base}{i}"''')
    _session = _Session()
    session = Session()
    for i in table_itr:
        c = eval(class_base+str(i))   #映射单个表的类
        for col in _session.query(c).filter(c.GET_ON_LATITUDE != 0).filter(c.GET_ON_LATITUDE != 0).all():
            col = OperateParams(WORK_BEGIN_TIME=col.WORK_BEGIN_TIME,GEOHASH=col.GEOHASH7)
            session.add(col)
    session.commit()
    session.close()
    _session.close()
    return True


def new_zone_quality():
    from settings import g_boundury,g_name
    drop_table(ZoneQuality)
    s = Session()
    d_match = {}
    rst = s.query(Quality.rid,Quality.hour_repre,Quality.average_time, Quality.density, Quality.flow).all()
    for rid,h,a_time,density,flow in rst:
        ghash5, = s.query(Records.geohash5).filter(Records.id==rid).first()
        for i,b in enumerate(g_boundury):
            if ghash5 in b:
                if i in d_match:
                    match = d_match[i]
                    if h in match:
                        match[h]['a_time'] = (match[h]['a_time'] + a_time) / 2
                        match[h]['density'] = (match[h]['density'] + density) / 2
                        match[h]['flow'] = (match[h]['flow'] + flow) / 2
                    else:
                        match[h] = {'a_time': a_time, 'density': density, 'flow': flow}
                else:
                    d_match[i] = {h: {'a_time': a_time, 'density': density, 'flow': flow}}
                break
    for i,match in d_match.items():
        for h in match:
            a_time = match[h]['a_time']
            density = match[h]['density']
            flow = match[h]['flow']
            s.add(ZoneQuality(g_zone=i,g_name=g_name[i],hour_repre=str(h),average_time=a_time,density=density,flow=flow))
    s.commit()
    s.close()

def new_zone_quality_1(d,maxrq=1000,date='2017-01-31'):
    '''取100个样本'''
    from settings import g_boundury,g_name
    s = Session()
    #全盘读取
    cls = eval(f'Quality_{d}')   #某一天
    date = datetime.strptime(date,'%Y-%m-%d') + timedelta(days=d)
    print("开始")
    for each_z,ghashs in enumerate(g_boundury): #对每个行政区
        for h in range(24): #对每个小时
            print("小时", h, "  /总数24", "区域")
            qry = s.query(cls.average_speed, cls.density, cls.flow)\
            .filter(cls.hour_repre==str(h))
            i = 0
            tmp = []
            for each_g in ghashs:  # 对每个ghash块
                i += 1
                # print("小时", h, "  /总数24","区域", i, "  /总数", len(ghashs))
                for rst in qry.filter(Records.geohash5 == each_g).order_by(cls.count).limit(maxrq):   #限制样本数
                    (a_time, density, flow) =rst
                    if a_time > 1e7:
                        a_time /= 1e6
                    a_time *= 3.6
                    if density > 1e7:
                        density /= 1e9
                    #数据预处理
                    tmp.append([a_time,density,flow])
            if tmp:
                tmp = np.array(tmp)
                a_time,density,flow = np.mean(tmp,axis=0)
            else:
                a_time, density, flow = 0,0,0
            date_time = date + timedelta(hours=h)
            # # **写入数据库
            print(g_name[each_z],date_time,each_z,a_time,density,flow)
            s.add(ZoneQuality_1(date_time=date_time,g_zone=each_z+1,g_name=g_name[each_z]
                        ,average_speed=float(a_time),density=float(density),flow=float(flow)))

            s.commit()
    s.close()

if __name__ =='__main__':
    #new_muti_operate((1,))    #或者(3,4,5)，传入一个可迭代对象
    #new_muti_operate_params((1,))  # 或者(3,4,5)，传入一个可迭代对象
    new_zone_quality()