# -*- coding: utf-8 -*-
# CreateDate: 2019-10-14
# Author: lin
import face_recognition
class User(object):

    def __init__(self,img = None,age = None,sex = None,id = None):
        self.img = img
        self.age = age
        self.sex = sex
        self.id = id


    def set_age(self,age):
        self.age = age

    def set_sex(self,sex):
        self.sex = sex

    def set_id(self, id):
        self.id = id

    """
    人脸识别算法
    """

    def recognition(self):
        picture = face_recognition.load_image_file("../../resource/face/1.jpg")
        #print(picture)
        my_face_encoding = face_recognition.face_encodings(picture)
        print(my_face_encoding)

        unknown_picture = face_recognition.load_image_file("../../resource/face/2.jpg")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        print(results)

        if results[0] == True:
            print("It's a picture of me!")
        else:
            print("It's not a picture of me!")


