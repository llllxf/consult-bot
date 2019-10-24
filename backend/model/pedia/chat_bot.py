# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_path)
from aiml_cn import AIMLUtil
from nlp import NLPUtil
from pedia.manager import TaskManager
def chat(question_str):

    words,pattern,arcs_dict,postags,hed_index = NLPUtil.get_sentence_pattern(question_str)
    print(words,pattern,arcs_dict,postags,hed_index)
    aiml_reponse = AIMLUtil.response(pattern)
    print(pattern,aiml_reponse)
    answer = TaskManager.task_response(aiml_reponse,words,arcs_dict,postags,hed_index)
    return answer


if __name__ == '__main__':
    AIMLUtil()
    NLPUtil('ltp_data_v3.4.0')

    while True:
        question_str = input('User:')
        if question_str == 'exit':
            break
        else:
            ans = chat(question_str)
            print(ans)








