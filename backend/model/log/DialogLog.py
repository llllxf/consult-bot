# -*- coding: utf-8 -*-
# CreateDate: 2019-10-22
# Author: lin

class DialogLog(object):

    @classmethod
    def __init__(cls):

        cls.dialog_dict = {}

    @classmethod
    def add(cls,userid,question_dict):
        if cls.dialog_dict[userid] == None:
            cls.dialog_dict[userid] = [question_dict]
        else:
            cls.dialog_dict[userid].append(question_dict)






