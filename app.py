from chalice import Chalice
import os
import json
import requests

app = Chalice(app_name='bimza-api')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/get_blocks', cors=True, methods=['GET'])
def get_blocks():
    r = requests.get('http://54.174.139.35:3002/blocks')
    return {'status': r.status_code, 'result': r.json()}


@app.route('/put_block', cors=True, methods=['POST'], content_types=['application/json'])
def put_block():
    post_data = json.loads(app.current_request.raw_body.decode())['data']
    print({'data': post_data})
    r = requests.post('http://54.174.139.35:3002/addBlock', json={"data": post_data})
    return {'status': r.status_code}


