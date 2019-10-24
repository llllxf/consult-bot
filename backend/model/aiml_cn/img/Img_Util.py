# -*- coding: utf-8 -*-
# CreateDate: 2019-10-14
# Author: lin
import face_recognition
class ImgUtil(object):
    def __init__(self,age,sex):
        self.img = None
        self.age = age
        self.sex = sex