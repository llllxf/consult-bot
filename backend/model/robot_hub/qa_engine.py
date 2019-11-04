# -*- coding: utf-8 -*-
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
print("hub",project_path)
sys.path.append(project_path)

"""
from model.grapg_QA.bot import Bot
from model.search_QA import similarQuestionBot
from model.aiml_cn import AIMLUtil
from model.nlp import NLPUtil
from model.pedia import TaskManager
"""
from model.grapg_QA.bot import Bot
from model.search_QA import similarQuestionBot
from model.aiml_cn import AIMLUtil
from model.nlp import NLPUtil
from model.pedia.manager import TaskManager
#from model.open_chat.chatterbot_chat import ChatterPolite
from model.nlp import IntentUtil
from model.nlp import ClearUtil
from model.user import User
import random
#from model.log import DialogLog


class GeneralHub():
    """
    总控程序版本2
    """

    @classmethod
    def __init__(cls):
        """
        主控模块的初始化
        1.得到AIML工具类
        2.得到NLP工具类
        """
        cls.user = None
        cls.aiml_util = AIMLUtil()
        cls.nlp_util = NLPUtil('ltp_data_v3.4.0')
        cls.search_bot = similarQuestionBot()
        cls.intent = IntentUtil()
        #cls.dialog_util = DialogLog()
        cls.clear_util = ClearUtil("../../resource/sensitiveness/keyword.txt")
        cls.last_question = ''
        cls.sorry = ['哎呀抱歉，暂时回答不了这个问题','很抱歉，我还在学习中，暂时回答不了这个问题','很抱歉，这个问题我还不会']

    @classmethod
    def set_user(cls,user):
        cls.user = user

    @classmethod
    def question_answer_hub(cls, question_str):
        """
        问答主总控，基于aiml构建问题匹配器
        :param question_str:问句输入
        :return:
        """
        if cls.user == None:
            cls.user = User()
            cls.user.set_age(20)
            cls.user.set_sex('女')


        question_str = cls.nlp_util.clear_question(question_str)
        question_str = cls.clear_util.filter(question_str)
        if '*' in question_str:
            return ['很抱歉，请您注意文明用语']

        if question_str == '不对':
            return [cls.last_question,'q','q']
        cls.last_question = question_str

        aiml_response = ''
        aiml_response_normal = ''
        aiml_response_specify = ''

        question_first,question_replaced_normal,question_replaced_spcify,entity_dict = cls.nlp_util.repalce_question(question_str)

        #print(question_first,question_replaced_normal,question_replaced_spcify)

        #print(question_first)
        aiml_response = cls.aiml_util.response(question_first,cls.intent.get_intent())
        #print(question_first,question_replaced_normal,question_replaced_spcify,entity_dict,aiml_response)

        if 'task_' in aiml_response:
            cls.intent.set_intent(aiml_response)

            graph_response = Bot.task_response(aiml_response, entity_dict,question_str,cls.user.age,cls.user.sex)

        elif aiml_response != '':
            cls.intent.set_intent(aiml_response)
            graph_response = [aiml_response]
        else:
            aiml_response_normal = cls.aiml_util.response(question_replaced_normal,cls.intent.get_intent())
            if 'task_' in aiml_response_normal:
                cls.intent.set_intent(aiml_response_normal)
                graph_response = Bot.task_response(aiml_response_normal, entity_dict,question_str,cls.user.age,cls.user.sex)
            elif aiml_response_normal != '':
                cls.intent.set_intent(aiml_response_normal)
                graph_response = [aiml_response_normal]
            else:
                aiml_response_specify = cls.aiml_util.response(question_replaced_spcify,cls.intent.get_intent())
                if 'task_' in aiml_response_specify:
                    cls.intent.set_intent(aiml_response_specify)
                    graph_response = Bot.task_response(aiml_response_specify, entity_dict,question_str,cls.user.age,cls.user.sex)
                elif aiml_response_specify != '':
                    cls.intent.set_intent(aiml_response_specify)
                    graph_response = [aiml_response_specify]
                else:
                    #print(question_str)
                    response = dict(cls.search_bot.answer_question(question_str)[0])
                    #print(response)

                    if float(response['score']) > 0.7:
                        cls.intent.set_intent(response['answer'])
                        graph_response = [response['answer']]

                    else:

                        words, pattern, arcs_dict, postags, hed_index = NLPUtil.get_sentence_pattern(question_str)
                        #print(words, pattern, arcs_dict, postags, hed_index)
                        aiml_reponse = AIMLUtil.pedia_response(pattern)

                        answer = TaskManager.task_response(aiml_reponse, words, arcs_dict, postags, hed_index)
                        if answer != None:
                            cls.intent.reset_intent('pedia')
                            return [answer]
                        else:
                            cls.intent.reset_intent('chat')
                            response_index = random.randint(0, 2)
                            #print("cls.chat.get_response(question_str)",cls.chat.get_response(question_str))
                            graph_response = [cls.sorry[response_index]]

        dialog_dict = {'intent':cls.intent.get_intent(),'question':question_str,'answer':graph_response[0]}
        #print(aiml_response,aiml_response_normal,aiml_response_specify)

        return graph_response



import time

if __name__ == '__main__':


    gh = GeneralHub()

    while True:
        question_str = input('User:')
        if question_str == 'exit':
            break
        else:
            time_start = time.time()
            response = gh.question_answer_hub(question_str)
            #print(response)
            print('Libot:', response[0])
            time_end = time.time()









