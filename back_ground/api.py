"""
the api model which will recive and return the data
"""
from flask import Flask, jsonify, make_response, request, url_for
from flask_cors import CORS
import json
from DBSCAN_taxi import DBSCAN_taxi

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app, resources=r'/*')
# deal with the cross-domain problem


@app.route('/todo/api/v1.5/route/<int:id>', methods=['GET'])
def get_task(id):
    return


@app.route('/taxi/api/v1.0/hotspot', methods=['POST'])
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




if __name__ == '__main__':
    app.run(debug=True, host='192.168.31.89', port=8080)