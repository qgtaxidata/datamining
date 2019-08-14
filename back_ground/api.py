"""
the api model which will recive and return the data
"""
from flask import Flask, jsonify, make_response, request, url_for
from flask_cors import CORS
import json
from DBSCAN_taxi import DBSCAN_taxi
from hot_Predict.hot_predict import predict_hotmap
from rank_sort import get_rank
from pagerank import demand
from driverInfor import calculate_driver

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app, resources=r'/*')
# deal with the cross-domain problem

mapping = {0: '全广州', 1: '花都区', 2: '南沙区', 3: '增城区', 4: '从化区',
           5: '番禺区', 6: '白云区', 7: '黄埔区', 8: '荔湾区', 9: '海珠区',
           10: '天河区', 11: '越秀区'}


@app.route('/todo/api/v1.5/route/<int:id>', methods=['GET'])
def get_task(id):
    return


@app.route('/taxi/api/v1.1/HotSpot', methods=['POST'])
def get_hotspot():
    """

    :return:
    """
    json_data = request.get_data()
    dic = json.loads(json_data)
    departure_x = dic['longitude']
    departure_y = dic['latitude']
    str_time = dic['time']
#   departure_x = request.form.get('longtiude', type=float, default=None)
#   departure_y= request.form.get('latitude', type=float, default=None)
#   str_time = request.form.get('time', type=str, default=None)
    info = DBSCAN_taxi([departure_y, departure_x], str_time + ':00')
    print(info)
    return jsonify(info)
#
# latitude

@app.route('/taxi/api/v1.0/FutureHeat', methods=['POST'])
def get_future_heat():
    """

    :return:
    """
    json_data = request.get_data()
    dic = json.loads(json_data)
    print(dic.keys())
    print(dic)
    result = predict_hotmap(dic)
    return jsonify(result['heat'])


@app.route('/taxi/api/v1.0/IncomeRank', methods=['POST'])
def get_income_rank():
    """

    :return:
    """
    json_data = request.get_data()
    dic = json.loads(json_data)
    print(dic)
    rank = get_rank(dic)
    print(rank)

    return jsonify(rank)

@app.route('/taxi/api/v1.0/Demand', methods=['POST'])
def get_demand():
    """

    :return:
    """
    json_data = request.get_data()
    print('connected')
    dic = json.loads(json_data)
    demands = demand(dic['area'], dic['time']) # '2017-02-03 19:15:48'
    graph_data = list()
    graph_data.append({'title': '一个小时前', 'demand': demands[0]})
    graph_data.append({'title': '当前时间', 'demand': demands[1]})
    graph_data.append({'title': '一个小时后', 'demand': demands[2]})
    result = dict()
    result['graph_data'] = graph_data
    result['graph_title'] = mapping[dic['area']] + '需求分析及预测'
    print(result)
    return result


@app.route('/taxi/api/v1.0/GetDriverInfo', methods=['POST'])
def get_driver_info():
    json_data = request.get_data()
    dic = json.loads(json_data)
    print('input:', dic)
    result = calculate_driver(dic)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.101', port=8080)