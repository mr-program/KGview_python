'''
@Author: your name
@Date: 2020-03-31 08:40:50
@LastEditTime: 2020-04-01 15:37:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \IOT\index.py
'''
from flask import Flask, render_template, jsonify, make_response, request
import json

app = Flask(__name__)

@app.route("/KG")
def KGView():
    return render_template('KG.html')

#{"type":"node"/"relation"}
@app.route("/KGDATA", methods=['GET', 'POST'])
def KGData():
    message = {}
    data = {}
    get_data = json.loads(request.get_data(as_text=True))
    type = get_data['type']
    if type == 'node':
        with open("./KG_data/node.json",'r',encoding='utf-8') as json_file:
            data=json.load(json_file)
        json_file.close()
        message = data
        pass
    elif type == 'relation':
        with open("./KG_data/relation.json",'r',encoding='utf-8') as json_file:
            data=json.load(json_file)
        json_file.close()
        message = data
        pass
    else:
        pass
    response = make_response(jsonify(message))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
