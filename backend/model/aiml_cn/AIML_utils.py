# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)
from model.aiml_cn import  Kernel
from model.aiml_cn import kernel

"""
AIML工具类
"""
class AIMLUtil(object):

    @classmethod
    def __init__(cls):

        """
        主总控aiml
        """
        cls.master_aiml_kernal = Kernel()
        cls.master_aiml_kernal.learn('../../resource/navi_template.aiml')
        cls.master_aiml_kernal.learn('../../resource/contain_template.aiml')
        cls.master_aiml_kernal.learn('../../resource/time.aiml')
        cls.master_aiml_kernal.learn('../../resource/condition.aiml')
        cls.master_aiml_kernal.learn('../../resource/information.aiml')
        cls.master_aiml_kernal.learn('../../resource/business.aiml')

        """
        百科aiml
        """
        cls.pedia_aiml_kernal = kernel()
        cls.pedia_aiml_kernal.learn('../../resource/pattern_for_cyclopedia.aiml')

        """
        推荐主控
        """
        cls.recommed_aiml_kernal = Kernel()
        cls.recommed_aiml_kernal.learn('../../resource/multiple/recommend.aiml')

        '''
        cls.aiml_kernal.learn('../resource/navi_template.aiml')
        cls.aiml_kernal.learn('../resource/contain_template.aiml')
        cls.aiml_kernal.learn('../resource/time.aiml')
        cls.aiml_kernal.learn('../resource/condition.aiml')
        cls.aiml_kernal.learn('../resource/information.aiml')
        cls.aiml_kernal.learn('../resource/business.aiml')
        '''

    @classmethod
    def response(cls, question, intent):
        """
        :param question:
        :param mtype:
        :return:
        """
        #print("intent",intent)
        if intent == 'recommend':
            recommed_aiml_response = cls.recommed_aiml_kernal.respond(question)
            return recommed_aiml_response
        master_aiml_response = cls.master_aiml_kernal.respond(question)
        return master_aiml_response

    @classmethod
    def pedia_response(cls, question):
        return cls.pedia_aiml_kernal.respond(question)


if __name__ == '__main__':
    AIMLUtil()
    ans = AIMLUtil.response("HED")
    print(ans)

