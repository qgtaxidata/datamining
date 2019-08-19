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



if __name__ =='__main__':
    #new_muti_operate((1,))    #或者(3,4,5)，传入一个可迭代对象
    #new_muti_operate_params((1,))  # 或者(3,4,5)，传入一个可迭代对象
    new_zone_quality()