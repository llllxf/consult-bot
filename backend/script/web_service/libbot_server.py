# -*- coding: utf-8 -*-
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
print("server",project_path)
sys.path.append(project_path)

import uuid
import tornado.web
import tornado.ioloop
import tornado.escape
import json
from model.nlp import NLPUtil
from model.user import User

#from model.robot_hub.general_hub_2 import GeneralHub
from model.robot_hub.qa_engine import GeneralHub
graph_qa_hub = GeneralHub()

class MainHandler(tornado.web.RequestHandler):



    def post(self):

        target = self.get_argument("target")
        #print(self.request.body)
        post_data = json.loads(self.request.body,strict=False)

        if target == 'graph_qa':

            question_str = post_data['question']
            question_str = NLPUtil.clear_question(question_str)

            graph_respons = graph_qa_hub.question_answer_hub(question_str)

            if question_str == None or question_str == '':
                res_dict = {'first':'我没听清，请您再说一遍'}
            elif len(graph_respons)==2:
                res_dict = {'first': str(graph_respons[0]),'second':graph_respons[1]}
            elif len(graph_respons)==1:
                print(graph_respons[0])

                res_dict = {'first': str(graph_respons[0])}
                if graph_respons[0].find('很抱歉')!=-1 or graph_respons[0] == '':
                    with open("question.txt",'a') as fw:
                        fw.writelines(question_str)
                        fw.writelines("\n")
            elif len(graph_respons) == 3:
                with open("question.txt", 'a') as fw:
                    fw.writelines(graph_respons[0])
                    fw.writelines("\n")
                res_dict = {'first':'收到'}

            res_json = json.dumps(res_dict)
            #print(res_json)
            self.write(res_json)

        elif target == 'recognition':
            user = User()
            print("post_data",post_data)
            age = post_data['age']
            #age = age.decode('utf-8')
            sex = post_data['sex']
            #sex = sex.decode('utf-8')
            img = post_data['img']
            if age == '未知':
                age = None
            if sex == '未知':
                sex = None
            if img == '未知':
                img = None

            import base64,datetime
            img_data = base64.b64decode(img)
            id = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

            with open(id+'.jpg', 'wb') as f:
                f.write(img_data)
            user.set_sex(sex)
            user.set_age(age)
            GeneralHub.set_user(user)
            res_dict = {'response': "已连接"}
            res_json = json.dumps(res_dict)
            print(res_json)
            self.write(res_json)
            print("age,sex",age,sex)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



