
#!/usr/bin/env Python
# coding=utf-8
import sys
import os
project_path = os.path.abspath(os.path.join(os.getcwd(), "../"))
#print(project_path)
sys.path.append(project_path)
from flask import Flask, render_template, request, make_response
from flask import jsonify

import time
import threading
from model.robot_hub.general_hub_2 import GeneralHub

generalHub = GeneralHub()
def heartbeat():
    print (time.strftime('%Y-%m-%d %H:%M:%S - heartbeat', time.localtime(time.time())))
    timer = threading.Timer(60, heartbeat)
    timer.start()
timer = threading.Timer(60, heartbeat)
timer.start()

try:  
    import xml.etree.cElementTree as ET  
except ImportError:  
    import xml.etree.ElementTree as ET


import re
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

app = Flask(__name__,static_url_path="/static") 

@app.route('/message', methods=['POST'])
def reply():

    question = request.form['msg']
    #res_msg = '^_^'
    #print(req_msg)
    #print(''.join([f+' ' for fh in req_msg for f in fh]))
    #req_msg=''.join([f+' ' for fh in req_msg for f in fh])
    #print(req_msg)
    res_msg = generalHub.question_answer_hub(question)[0]
    
    #res_msg = res_msg.replace('_UNK', '^_^')
    res_msg=res_msg.strip()
    
    # 如果接受到的内容为空，则给出相应的恢复
    if res_msg == '很抱歉，我好像不明白，请您换一种说法':
        import requests, json
        github_url = "http://openapi.tuling123.com/openapi/api/v2"
        data = json.dumps({
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": question
                },
            },
            "userInfo": {
                "apiKey": "62f1c8991a6d499c8b22e497de6cdd11",
                "userId": "219315"
            }
        })

        r = requests.post(github_url, data)
        print(r.json())
        res_msg = r.json()['results'][0]['values']['text']
        '''
        if r.json()['intent']['code'] == 10004:
            res_msg = r.json()['results'][0]['values']['text']
        else:
            import requests, json
            github_url = "http://openapi.tuling123.com/openapi/api/v2"
            data = r
            r = requests.post(github_url, data)
            print(r.json())
            if r.json()['intent']['code'] == 10004:
                res_msg = r.json()['results'][0]['values']['text']
        '''

    return jsonify( { 'text': res_msg } )

@app.route("/")
def index():
    return render_template("index.html")
#



# 启动APP
if (__name__ == "__main__"): 
    app.run(host = '0.0.0.0', port = 8809)


