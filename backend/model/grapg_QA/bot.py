# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.grapg_QA.Task_contain import Task_contain
from model.grapg_QA.Task_information import Task_information
from model.grapg_QA.Task_condition import Task_condition
from model.grapg_QA.Task_business import Task_business
from model.grapg_QA.Task_position import Task_position

class Bot():
    @classmethod
    def task_response(cls, task, entity_dict,question,age=20,sex='女'):
        """
        响应hub指派的回答任务，也就是对graphQA类的问题分intent处理
        :param task:
        :return:
        """

        answer = ""
        if task == 'task_res_pos':
            answer = cls.answer_res_pos(entity_dict)
        elif task == 'task_goods_pos':
            answer = cls.answer_goods_pos(entity_dict)
        elif task == 'task_room_pos':
            answer = cls.answer_room_pos(entity_dict)
        elif task == 'task_room_res_a_contain':
            answer = cls.answer_room_res_a(entity_dict)
        elif task == 'task_room_time':
            answer = cls.answer_room_time(entity_dict)
        elif task == 'task_room_res_time':
            answer = cls.answer_room_res_time(entity_dict)
        elif task == 'task_res_time':
            answer = cls.answer_res_time(entity_dict)
        elif task == 'task_floor_room_a_contain':
            answer = cls.answer_floor_room_a(entity_dict)
        elif task == 'task_room_floor_contain':
            answer = cls.answer_floor_room(entity_dict)
        elif task == "task_res_room_contain":
            answer = cls.answer_res_room(entity_dict)
        elif task == "task_res_floor_contain":
            answer = cls.answer_res_floor(entity_dict)
        elif task == "task_floor_res_a_contain":
            answer = cls.answer_res_floor_a(entity_dict)
        elif task == "task_floor_res_a_contain":
            answer = cls.answer_room_res_a(entity_dict)
        elif task == "task_room_borrow_business":
            answer = cls.answer_room_borrow(entity_dict)
        elif task == "task_res_borrow_business":
            answer = cls.answer_res_borrow(entity_dict)
        elif task == "task_area_borrow_business":
            answer = cls.answer_area_borrow(entity_dict)
        elif task == "task_room_phone_information":
            answer = cls.answer_room_phone(entity_dict)
        elif task == "task_room_describe_information":
            answer = cls.answer_room_describe(entity_dict)
        elif task == "task_res_describe_information":
            answer = cls.answer_res_describe(entity_dict)
        elif task == "task_count_res_contain":
            answer = cls.answer_count_res(entity_dict)
        elif task == "task_count_restype_contain":
            answer = cls.answer_count_restype(entity_dict)
        elif task == "task_count_multype_contain":
            answer = cls.answer_count_multype(entity_dict)
        elif task == "task_res_res_h_contain":
            answer = cls.answer_res_res_h(entity_dict)
        elif task == "task_res_res_a_contain":
            answer = cls.answer_res_res_a(entity_dict)
        elif task == "task_mul_res_h_contain":
            answer = cls.answer_mul_res_h(entity_dict)
        elif task == "task_mul_res_a_contain":
            answer = cls.answer_mul_res_a(entity_dict)
        elif task == "task_res_res_t_contain":
            answer = cls.answer_res_res_t(entity_dict)
        elif task == "task_room_card_a_condition":
            answer = cls.answer_room_card_a(entity_dict)
        elif task == "task_card_yes_business":
            answer = cls.answer_card_yes()
        elif task == "task_card_no_business":
            answer = cls.answer_card_no()
        elif task == "task_card_thirteen_business":
            answer = cls.answer_card_thirteen()
        elif task == "task_card_twelve_business":
            answer = cls.answer_card_twelve()
        elif task == "task_restype_borrow_business":
            answer = cls.answer_restype_borrow(entity_dict)
        ###################################################
        elif task == "task_multype_borrow_business":
            answer = cls.answer_multype_borrow(entity_dict)
        ###################################################
        elif task == "task_restype_describe_information":
            answer = cls.answer_restype_describe(entity_dict)
        elif task == "task_multype_describe_information":
            answer = cls.answer_multype_describe(entity_dict)
        elif task == "task_count_floor_contain":
            answer = cls.answer_count_floor(entity_dict)
        elif task == "task_floor_count_room_contain":
            answer = cls.answer_floor_count_room(entity_dict)
        elif task == "task_room_pos":
            answer = cls.answer_room_pos(entity_dict)
        elif task == 'task_res_pos':
            answer = cls.answer_res_pos(entity_dict)
        elif task == "task_card_describe_information":
            answer = cls.answer_card_describe(entity_dict)
        elif task == "task_finance_describe_information":
            answer = cls.answer_finance_describe()
        elif task == "task_restype_pos":
            answer = cls.answer_restype_pos(entity_dict)
        elif task == "task_multype_pos":
            answer = cls.answer_multype_pos(entity_dict)
        elif task == "task_music_or_movie_contain":
            answer = cls.answer_music_or_movie()
        elif task == "task_library_describe_information":
            answer = cls.answer_library_describe()
        elif task == "task_library_area_contain":
            answer = cls.answer_library_area()
        elif task == "task_res_read_business":
            answer = cls.answer_res_read(entity_dict)
        elif task == "task_restype_read_business":
            answer = cls.answer_restype_read(entity_dict)
        elif task == 'task_service_describe_information':
            answer = cls.answer_service_describe(entity_dict)
        elif task == 'task_task_describe_information':
            answer = cls.answer_task_describe(entity_dict)
        elif task == 'task_service_pos':
            answer = cls.answer_service_pos(entity_dict)
        elif task == 'task_task_pos':
            answer = cls.answer_task_pos(entity_dict)
        elif task == 'task_service_time':
            answer = cls.answer_service_time(entity_dict)
        elif task == 'task_task_time':
            answer = cls.answer_task_time(entity_dict)
        elif task == 'task_library_time':
            answer = cls.answer_library_time(entity_dict)
        elif task == 'task_area_time':
            answer = cls.answer_area_time(entity_dict)
        elif task == 'task_floor_borrow_business':
            answer = cls.answer_floor_borrow(entity_dict)
        elif task == 'task_library_res_a_contain':
            answer = cls.answer_library_res_a()
        elif task == 'task_library_res_contain':
            answer = cls.answer_library_res()
        elif task == 'task_area_res_a_contain':
            answer = cls.answer_area_res_a(entity_dict)
        elif task == 'task_library_phone_information':
            answer = cls.answer_library_phone()
        elif task == 'task_service_exit_contain':
            answer = cls.answer_service_exit(entity_dict)
        elif task == 'task_task_exit_contain':
            answer = cls.answer_task_exit(entity_dict)
        elif task == 'task_res_form_information':
            answer = cls.answer_res_form(entity_dict)
        elif task == 'task_res_topic_information':
            answer = cls.answer_res_topic(entity_dict)
        ################################################
        elif task == 'task_service_room_all':
            answer = cls.answer_service_room_all(entity_dict)
        elif task == "task_area_pos":
            answer = cls.answer_area_pos(entity_dict)
        elif task == 'task_return_back_res_business':
            answer = cls.answer_return_back_res(entity_dict)
        elif task == 'task_service_exit_all_contain':
            answer = cls.answer_service_exit_all()
        elif task == 'task_service_area_all_contain':
            answer = cls.answer_service_area_all(entity_dict)
        elif task == 'task_service_room_exit_contain':
            answer = cls.answer_service_room_exit(entity_dict)
        elif task == 'task_service_area_exit_contain':
            answer = cls.answer_service_area_exit(entity_dict)
        elif task == 'task_open_room_information':
            answer = cls.answer_open_room()
        elif task == 'task_res_search_business':
            answer = cls.answer_res_search(entity_dict)
        elif task == 'task_restype_room_contain':
            answer = cls.answer_restype_room(entity_dict)
        elif task == 'task_restype_area_contain':
            answer = cls.answer_restype_area(entity_dict)
        elif task == 'task_multype_room_contain':
            answer = cls.answer_multype_room(entity_dict)
        elif task == 'task_multype_area_contain':
            answer = cls.answer_multype_area(entity_dict)
        elif task == 'task_multype_library_contain':
            answer = cls.answer_multype_library(entity_dict)
        elif task == 'task_restype_library_contain':
            answer = cls.answer_restype_library(entity_dict)
        elif task == 'task_ttype_area_contain':
            answer = cls.answer_ttype_area(entity_dict)
        elif task == 'task_ttype_library_contain':
            answer = cls.answer_ttype_library(entity_dict)
        elif task == 'task_res_library_contain':
            answer = cls.answer_res_library(entity_dict)
        elif task == 'task_goods_library_contain':
            answer = cls.answer_goods_library(entity_dict)
        elif task == 'task_get_card_business':
            answer = cls.answer_get_card(entity_dict,age,sex)
        elif task == 'task_book_recommend':
            answer = cls.answer_recommend_book(age,sex)
        elif task == 'task_book_other_recommend':
            answer = cls.answer_recommend_book_other()
        elif task == 'task_borrow_card_condition':
            answer = cls.answer_borrow_card(age)
        elif task == 'task_end_multiple_normal':
            answer = cls.answer_end_multiple_normal(question)
        elif task == 'task_money_back_no_business':
            answer = cls.answer_money_back_no()
        elif task == 'task_money_back_business':
            answer = cls.answer_money_back()
        return answer

    @classmethod
    def answer_end_multiple_normal(cls, question):
        return ['repeat',question]

    @classmethod
    def answer_get_card(cls, entity_dict,age,sex):

        task_business = Task_business()
        res = task_business.solve_get_card(entity_dict,age,sex)
        return [res]

    @classmethod
    def answer_borrow_card(cls,age):

        task_business = Task_business()
        res = task_business.solve_borrow_card(age)
        return [res]

    @classmethod
    def answer_recommend_book(cls, age, sex):

        task_business = Task_business()
        res = task_business.solve_recommend_book(age, sex)
        return [res]

    @classmethod
    def answer_recommend_book_other(cls):

        task_business = Task_business()
        res = task_business.solve_recommend_book_other()
        return [res]

    @classmethod
    def answer_room_time(cls,entity_dict):

        task_information = Task_information()
        res = task_information.solve_room_time(entity_dict)
        return [res]

    @classmethod
    def answer_room_res_time(cls,entity_dict):
        task_information = Task_information()
        res = task_information.solve_room_res_time(entity_dict)
        return [res]

    @classmethod
    def answer_res_time(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_res_time(entity_dict)
        return [res]

    @classmethod
    def answer_floor_room_a(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_floor_room_a(entity_dict)
        return [res]

    @classmethod
    def answer_floor_room(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_room_floor(entity_dict)
        return [res]

    @classmethod
    def answer_res_room(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_room(entity_dict)
        return [res]

    @classmethod
    def answer_restype_room(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_restype_room(entity_dict)
        return [res]

    @classmethod
    def answer_multype_room(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_multype_room(entity_dict)
        return [res]

    @classmethod
    def answer_restype_area(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_restype_area(entity_dict)
        return [res]

    @classmethod
    def answer_restype_library(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_restype_library(entity_dict)
        return [res]

    @classmethod
    def answer_multype_area(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_multype_area(entity_dict)
        return [res]

    @classmethod
    def answer_multype_library(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_multype_library(entity_dict)
        return [res]

    @classmethod
    def answer_restype_library(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_restype_library(entity_dict)
        return [res]

    @classmethod
    def answer_ttype_area(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_ttype_area(entity_dict)
        return [res]

    @classmethod
    def answer_ttype_library(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_ttype_library(entity_dict)
        return [res]

    @classmethod
    def answer_res_library(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_library(entity_dict)
        return [res]

    @classmethod
    def answer_goods_library(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_goods_library(entity_dict)
        return [res]

    @classmethod
    def answer_res_floor(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_floor(entity_dict)
        return [res]

    @classmethod
    def answer_res_floor_a(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_floor_a(entity_dict)
        return [res]

    @classmethod
    def answer_room_res_a(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_room_res_a(entity_dict)
        return [res]

    @classmethod
    def answer_room_borrow(cls, entity_dict):
        task_business = Task_business()
        res = task_business.solve_room_borrow(entity_dict)
        return [res]

    @classmethod
    def answer_res_borrow(cls, entity_dict):
        task_business = Task_business()
        res = task_business.solve_res_borrow(entity_dict)
        return [res]

    @classmethod
    def answer_room_phone(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_room_phone(entity_dict)
        return [res]

    @classmethod
    def answer_room_describe(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_room_describe(entity_dict)
        return [res]

    @classmethod
    def answer_res_describe(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_res_describe(entity_dict)
        return [res]

    @classmethod
    def answer_count_res(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_count_res(entity_dict)
        return [res]

    @classmethod
    def answer_count_restype(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_count_restype(entity_dict)
        return [res]

    @classmethod
    def answer_count_multype(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_count_multype(entity_dict)
        return [res]

    @classmethod
    def answer_res_res_h(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_res_h(entity_dict)
        return [res]

    @classmethod
    def answer_res_res_a(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_res_a(entity_dict)
        return [res]

    @classmethod
    def answer_mul_res_h(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_mul_res_h(entity_dict)
        return [res]

    @classmethod
    def answer_mul_res_a(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_mul_res_a(entity_dict)
        return [res]

    @classmethod
    def answer_res_res_t(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_res_res_t(entity_dict)
        return [res]

    @classmethod
    def answer_room_card_a(cls, entity_dict):
        task_condition = Task_condition()
        res = task_condition.solve_room_card_a(entity_dict)
        return [res]

    @classmethod
    def answer_card_yes(cls):
        task_business = Task_business()
        return [task_business.solve__card_yes()]

    @classmethod
    def answer_card_no(cls):
        task_business = Task_business()
        return [task_business.solve__card_no()]

    @classmethod
    def answer_card_thirteen(cls):
        task_business = Task_business()
        return [task_business.solve__card_thirteen()]

    @classmethod
    def answer_card_twelve(cls):
        task_business = Task_business()
        return [task_business.solve__card_twelve()]

    @classmethod
    def answer_restype_borrow(cls, entity_dict):

        task_business = Task_business()
        res = task_business.solve_restype_borrow(entity_dict)
        return [res]

    @classmethod
    def answer_multype_borrow(cls, entity_dict):

        task_business = Task_business()
        res = task_business.solve_multype_borrow(entity_dict)
        return [res]

    @classmethod
    def answer_restype_describe(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_restype_describe(entity_dict)
        return [res]

    @classmethod
    def answer_multype_describe(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_multype_describe(entity_dict)
        return [res]

    @classmethod
    def answer_count_floor(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_count_floor(entity_dict)
        return [res]

    @classmethod
    def answer_floor_count_room(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_floor_count_room(entity_dict)
        return [res]

    @classmethod
    def answer_room_pos(cls, entity_dict):
        task_position = Task_position()
        res = task_position.solve_room_pos(entity_dict)
        return res


    @classmethod
    def answer_res_pos(cls, entity_dict):
        task_position = Task_position()
        res = task_position.solve_res_pos(entity_dict)
        return [res]

    @classmethod
    def answer_goods_pos(cls, entity_dict):
        task_position = Task_position()
        res = task_position.solve_goods_pos(entity_dict)
        return [res]

    @classmethod
    def answer_area_borrow(cls, entity_dict):
        task_business = Task_business()
        res = task_business.solve_area_borrow(entity_dict)
        return [res]

    @classmethod
    def answer_card_describe(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_card_describe()
        return [res]

    @classmethod
    def answer_finance_describe(cls):
        task_information = Task_information()
        res = task_information.solve_finance_describe()
        return [res]

    @classmethod
    def answer_money_back(cls):
        task_business = Task_business()
        res = task_business.solve_money_back()
        return [res]

    @classmethod
    def answer_money_back_no(cls):
        task_business = Task_business()
        res = task_business.solve_money_back_no()
        return [res]

    @classmethod
    def answer_restype_pos(cls,entity):
        task_position = Task_position()
        res = task_position.solve_restype_pos(entity)
        return [res]

    @classmethod
    def answer_multype_pos(cls, entity):
        task_position = Task_position()
        res = task_position.solve_multype_pos(entity)
        return [res]

    @classmethod
    def answer_music_pos(cls):
        dict = {'room':'视听阅览区'}
        task_position = Task_position()
        res = task_position.solve_room_pos(dict)
        return res

    @classmethod
    def answer_music_or_movie(cls):
        dict = {'room': ['视听阅览区']}
        res = "\n视听阅览室可以欣赏电影和音乐"
        task_position = Task_position()
        res += task_position.solve_room_pos(dict)[0]
        return [res]

    @classmethod
    def answer_library_describe(cls):
        task_information = Task_information()
        res = task_information.solve_library_describe()
        return [res]

    @classmethod
    def answer_library_area(cls):
        task_contain = Task_contain()
        res = task_contain.solve_library_area()
        return [res]

    @classmethod
    def answer_res_read(cls,entity_dict):
        task_business = Task_business()
        res = task_business.solve_res_read(entity_dict)
        return [res]

    @classmethod
    def answer_restype_read(cls, entity_dict):
        task_business = Task_business()
        res = task_business.solve_restype_read(entity_dict)
        return [res]

    @classmethod
    def answer_service_describe(cls,entity_dict):
        print("entity_dict",entity_dict)
        task_information = Task_information()
        res = task_information.solve_service_describe(entity_dict)
        print(res)
        return [res]

    @classmethod
    def answer_task_describe(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_task_describe(entity_dict)
        return [res]

    @classmethod
    def answer_service_pos(cls, entity_dict):
        task_position = Task_position()
        res = task_position.solve_service_pos(entity_dict)
        return [res]

    @classmethod
    def answer_task_pos(cls, entity_dict):
        task_position = Task_position()
        res = task_position.solve_task_pos(entity_dict)
        return [res]

    @classmethod
    def answer_service_time(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_service_time(entity_dict)
        return [res]

    @classmethod
    def answer_task_time(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_task_time(entity_dict)
        return [res]

    @classmethod
    def answer_area_time(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_area_time(entity_dict)
        return [res]


    @classmethod
    def answer_library_time(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_library_time(entity_dict)
        return [res]

    @classmethod
    def answer_floor_borrow(cls, entity_dict):
        task_business = Task_business()
        res = task_business.solve_floor_borrow(entity_dict)
        return [res]

    @classmethod
    def answer_library_res_a(cls):
        task_contain = Task_contain()
        res = task_contain.solve_library_res_a()
        return [res]

    @classmethod
    def answer_library_res(cls):
        task_contain = Task_contain()
        res = task_contain.solve_library_res()
        return [res]

    @classmethod
    def answer_area_res_a(cls,entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_area_res_a(entity_dict)
        return [res]

    @classmethod
    def answer_library_phone(cls):
        task_information = Task_information()
        res = task_information.solve_library_phone()
        return [res]

    @classmethod
    def answer_service_exit(cls,entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_service_exit(entity_dict)
        return [res]

    @classmethod
    def answer_task_exit(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_task_exit(entity_dict)
        return [res]

    @classmethod
    def answer_res_form(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_res_form(entity_dict)
        return [res]

    @classmethod
    def answer_res_topic(cls, entity_dict):
        task_information = Task_information()
        res = task_information.solve_res_topic(entity_dict)
        return [res]

    @classmethod
    def answer_service_room_all(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_service_room_all(entity_dict)
        return [res]

    @classmethod
    def answer_service_room_exit(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_service_room_exit(entity_dict)
        return [res]

    @classmethod
    def answer_service_area_exit(cls, entity_dict):
        task_contain = Task_contain()
        res = task_contain.solve_service_area_exit(entity_dict)
        return [res]


    @classmethod
    def answer_area_pos(cls, entity_dict):
        task_position = Task_position()
        res = task_position.solve_area_pos(entity_dict)
        return [res]

    @classmethod
    def answer_return_back_res(cls, entity_dict):
        task_business = Task_business()
        res = task_business.solve_return_back_res(entity_dict)
        return [res]

    @classmethod
    def answer_service_exit_all(cls):
        task_contain = Task_contain()
        res = task_contain.solve_service_exit_all()
        return [res]

    @classmethod
    def answer_service_area_all(cls,entity):
        task_contain = Task_contain()
        res = task_contain.solve_service_area_all(entity)
        return [res]

    @classmethod
    def answer_open_room(cls):
        task_contain = Task_contain()
        res = task_contain.solve_open_room()
        return [res]

    @classmethod
    def answer_res_search(cls,entity_dict):
        task_business = Task_business()
        res = task_business.solve_res_search(entity_dict)
        return [res]
