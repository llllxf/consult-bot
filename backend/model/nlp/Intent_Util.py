# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
print("intent",project_path)
sys.path.append(project_path)

"""
意图识别工具类
"""
class IntentUtil(object):

    @classmethod
    def __init__(cls):
        cls.intent_keyword = {'INFORMATION':[['介绍'],['是什么']],
                      'TIME':[['几点'],['时间'],['时候'],['今天'],['明天'],['后天'],['周一'],['星期一'],['周二'],['星期二'],['周三'],['星期三'],['星期四'],['周四'],['星期五'],['周五'],['星期六'],['周六'],['星期日'],['周日'],['礼拜天'],['哪天'],['周几'],['星期几'],['哪周'],['现在'],['开放'],['上午'],['下午'],['晚上']],
                      'POSITION':['去哪','哪里','在哪','地方','位置'],
                      'CONTAIN':['包括','包含','有什么','有哪些','多少','有几','含'],
                      'BUSINESS':['怎么','如何'],
                      'MULTIPLE':['办理','推荐'],
                      'CONDITION':[['借','书','证'],['借阅','证']]
                      }
        cls.intent = 'normal'
        cls.mul_intent = ['recommend']

    @classmethod
    def reset_intent(cls, intent):
        cls.intent = intent

    @classmethod
    def set_intent(cls, respond):
        print(respond)
        if respond.find("_")!=-1:
            intent = respond.split("_")[-1]
            cls.intent = intent
        else:
            cls.intent = 'normal'

    @classmethod
    def get_intent(cls):
        return cls.intent


    """
    @classmethod
    def judge_intent(cls):
    """











