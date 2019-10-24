# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from py2neo import Node, Graph, Relationship
from model.kb_prepare.room import room
from model.kb_prepare.floor import floor
from model.kb_prepare.resource import resource
from model.kb_prepare.card import card
from model.kb_prepare.resType import resType
from model.kb_prepare.service import service
from model.kb_prepare.task import task
from model.kb_prepare.area import area
from model.kb_prepare.res import mulType
from model.kb_prepare.goods import goods


class Neo4jPrepare(object):

    @classmethod
    def __init__(cls):
        """建立连接"""

        link = Graph("bolt://127.0.0.1:7687", username="lin123", password="lin123")
        cls.graph = link

        """定义label"""
        cls.area = '馆区'
        cls.room = '馆室'
        cls.floor = '楼层'
        cls.resource = "资源"
        cls.mark = "标志点"
        cls.card = '证件'
        cls.restype = '资源类型'
        cls.library = '国家图书馆'
        cls.service = '服务'
        cls.attribute = '属性'
        cls.res = '资源大类'
        cls.goods = '精品'
        """
        具有个性的业务与服务
        """
        cls.task = '业务'
        cls.multype = '资源中级类'

        #cls.graph.delete_all()
        """建图"""

        #cls.create_node()
        #cls.create_relation()

        #cls.create()

    @classmethod
    def create(cls):
        name = Node(cls.attribute, name="名称",name2="名称")
        cls.graph.create(name)
        variant_name = Node(cls.attribute, name="别名",name2="别名")
        cls.graph.create(variant_name)
        weekdy_opentime = Node(cls.attribute, name="开放时间",name2="开放时间")
        cls.graph.create(weekdy_opentime)
        open_date = Node(cls.attribute, name="开放日",name2="开放日")
        cls.graph.create(open_date)
        phone = Node(cls.attribute, name="电话",name2="电话")
        cls.graph.create(phone)
        describe = Node(cls.attribute, name="描述",name2="描述")
        cls.graph.create(describe)
        workday_btime = Node(cls.attribute, name="借阅时间",name2="借阅时间")
        cls.graph.create(workday_btime)
        #borrow = Node(cls.attribute, name="借阅",name2="借阅")
        #cls.graph.create(borrow)
        position = Node(cls.attribute, name="位置",name2="位置")
        cls.graph.create(position)
        site = Node(cls.attribute, name="坐标",name2="坐标")
        cls.graph.create(site)
        time = Node(cls.attribute, name="时间",name2="时间")
        cls.graph.create(time)
        num = Node(cls.attribute, name="数量",name2="数量")
        cls.graph.create(num)
        age = Node(cls.attribute, name="年龄",name2="年龄")
        cls.graph.create(age)
        function = Node(cls.attribute, name="功能",name2="功能")
        cls.graph.create(function)
        kind = Node(cls.attribute, name="类别", name2="类别")
        cls.graph.create(kind)
        author = Node(cls.attribute, name="作者", name2="作者")
        cls.graph.create(author)
        author = Node(cls.attribute, name="主题", name2="主题")
        cls.graph.create(author)
        collect_time = Node(cls.attribute, name="收藏时间", name2="收藏时间")
        cls.graph.create(collect_time)
        #############################################################
        library = Node(cls.library, name="国家图书馆")
        cls.graph.create(library)
        room = Node(cls.room, name="馆室")
        cls.graph.create(room)
        area = Node(cls.area, name="馆区")
        cls.graph.create(area)
        floor = Node(cls.floor, name="楼层")
        cls.graph.create(floor)
        card = Node(cls.card, name="读者卡")
        cls.graph.create(card)
        resource = Node(cls.resource, name="资源")
        cls.graph.create(resource)
        restype = Node(cls.restype, name="资源初级类型")
        cls.graph.create(restype)
        multype = Node(cls.multype, name="资源中级类型")
        cls.graph.create(multype)
        ttype = Node(cls.res, name="资源大类")
        cls.graph.create(ttype)
        service = Node(cls.service, name="服务")
        cls.graph.create(service)
        task = Node(cls.task, name="业务")
        cls.graph.create(task)
        goods = Node(cls.goods, name="精品")
        cls.graph.create(goods)
        #############################################################
        rel = Relationship(cls.graph.find_one(label=cls.library), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="位置"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.library), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.library), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.library), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="电话"))
        cls.graph.create(rel)
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.library), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.area), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.area), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.area), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="电话"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.area), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="位置"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.floor), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="位置"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="坐标"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="开放日"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute,property_key='name',property_value="开放时间"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="电话"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="借阅时间"))
        cls.graph.create(rel)
        #rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           #cls.graph.find_one(label=cls.attribute, property_key='name',property_value="借阅"))
        #cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="数量"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="主题"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="收藏时间"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.goods), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="类别"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="作者"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="数量"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.multype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.multype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.multype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.multype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="数量"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.res), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.res), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.res), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.res), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="数量"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.card), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.card), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.card), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.card), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="年龄"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.card), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="功能"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.service), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="时间"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.service), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.service), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.service), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.task), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="时间"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.task), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="名称"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.task), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.task), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)

        #############################################################

        rel = Relationship(cls.graph.find_one(label=cls.room), "位于",
                           cls.graph.find_one(label=cls.floor))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.area), "包括",
                           cls.graph.find_one(label=cls.library))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.room), "处于",
                           cls.graph.find_one(label=cls.area))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.floor), "处于",
                           cls.graph.find_one(label=cls.area))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.goods), "属于",
                           cls.graph.find_one(label=cls.resource))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.resource), "属于",
                           cls.graph.find_one(label=cls.restype))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.restype), "属于",
                           cls.graph.find_one(label=cls.multype))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.restype), "属于",
                           cls.graph.find_one(label=cls.res))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.resource), "存放",
                           cls.graph.find_one(label=cls.room))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.goods), "存放",
                           cls.graph.find_one(label=cls.room))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.room), "证件",
                           cls.graph.find_one(label=cls.card))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.service), "发生",
                           cls.graph.find_one(label=cls.room))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.task), "发生",
                           cls.graph.find_one(label=cls.room))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.service), "对象",
                           cls.graph.find_one(label=cls.resource))
        cls.graph.create(rel)
        ###################################################################


    '''
    属性查询
    '''
    @classmethod
    def get_property(cls,entity):
        cursor = cls.graph.run("match(n {office_name:{a}})return n",a=entity)
        cursor.forward()
        record = cursor.current()
        return (dict(record['n']))


    '''
    关系查询，直接关联
    '''

    @classmethod
    def get_relation(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})-[]->(b {type:{r}}) return b", a=entity,r=type)

        ans=[]
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))

        return ans

    '''
    关系查询，多级关联，最多两跳
    '''

    @classmethod
    def get_relation_mul(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})-[*..2]->(b {type:{r}}) return b", a=entity, r=type)

        ans = []
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            #print(dict(record['b']))
        return ans

    '''
    关系查询，多级关联，最多三跳
    '''

    @classmethod
    def get_relation_triple(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})-[*..3]->(b {type:{r}}) return b", a=entity, r=type)

        ans = []
        while cursor.forward():
            record = cursor.current()
            ans.append(dict(record['b']))
            # print(dict(record['b']))
        return ans


    '''
    逆向关系查询 直接关联
    '''

    @classmethod
    def get_reverse_relation(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})<-[]-(b {type:{r}}) return b", a=entity, r=type)
        #cursor = cls.graph.run("match(n{office_name: '数字共享空间'}) < -[] - (b {type:'资源'})return b")

        ans = []
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            #print(dict(record['b']))
        return ans

    '''
    逆向关系查询 多级关联 最多两跳
    '''

    @classmethod
    def get_reverse_relation_mul(cls, entity, type):
        #print(entity,type)
        cursor = cls.graph.run("match(n {office_name:{a}})<-[*..2]-(b {type:{r}}) return b", a=entity, r=type)
        #cursor = cls.graph.run("match(n {office_name:{a}})<-[*]-(b {type:{r}}) return b", a='总馆北区', r='资源')

        ans = []
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            #print(dict(record['b']))
        return ans


    '''
    得到某个类型的所有实体
    '''
    @classmethod
    def get_entity(cls, type):
        # print(entity,type)
        cursor = cls.graph.run("match(n {type:{a}}) return n", a=type)
        # cursor = cls.graph.run("match(n {office_name:{a}})<-[*]-(b {type:{r}}) return b", a='总馆北区', r='资源')
        ans = []
        while cursor.forward():
            record = cursor.current()
            ans.append(dict(record['n']))
        return ans

    '''
    得到某个类型具有某一kind属性的所有实体
    '''

    @classmethod
    def get_entity_for_kind(cls, type, att):

        cursor = cls.graph.run("match (n) where n.type={a} and n.kind={b} return n", a=type,b=att)
        # cursor = cls.graph.run("match(n {office_name:{a}})<-[*]-(b {type:{r}}) return b", a='总馆北区', r='资源')
        ans = []
        while cursor.forward():
            record = cursor.current()
            ans.append(dict(record['n']))
        return ans

    '''
    查出所有的别名
    '''
    @classmethod
    def get_all_varname(cls):

        room_list=[]
        room_alias_list=[]
        floor_list=[]
        floor_alias_list=[]
        area_list=[]
        area_alias_list = []
        resource_list=[]
        resource_alias_list=[]
        restype_list=[]
        restype_alias_list=[]
        card_list=[]
        card_alias_list=[]
        library = ""
        library_alias_list=[]
        service_list=[]
        service_alias_list=[]
        task_list = []
        task_alias_list = []
        multype_list = []
        multype_alias_list = []
        ttype_list = []
        ttype_alias_list = []
        goods_list = []
        goods_alias_list = []


        '''
        馆室正名、别名
        '''
        cursor = cls.graph.run("match(n:`馆室`)return n.office_name as room ,n.variant_name as variant_name")

        while cursor.forward():
            #record = dict(cursor.current)
            #print record

            record = dict(cursor.current())
            room_list.append(record['room'])
            if record['variant_name'].find(u"，")!=-1:
                temp = record['variant_name'].split(u"，")
            else:
                temp =[record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            room_alias_list.append(temp)
        '''
        print("room_list====================================================")
        for i in room_variant_list:
            for j in i:
                print(j)
        '''

        '''
        楼层正名、别名
        '''
        cursor = cls.graph.run("match(n:`楼层`)return n.office_name as floor ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            floor_list.append(record['floor'])
            if record['variant_name'].find(u"，") != -1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            floor_alias_list.append(temp)
        '''
        print("floor_list====================================================")
        for i in floor_variant_list:
            for j in i:
                print(j)
        '''

        '''
        馆区正名、别名
        '''
        cursor = cls.graph.run("match(n:`馆区`)return n.office_name as area ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            area_list.append(record['area'])
            if record['variant_name'].find(u"，")!=-1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            area_alias_list.append(temp)

        '''        
        print("area_list====================================================")
        for i in area_variant_list:
            for j in i:
                print(j)
        '''

        '''
        资源正名、别名
        '''
        cursor = cls.graph.run("match(n:`资源`)return n.office_name as resource ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            resource_list.append(record['resource'])
            if record['variant_name'].find(u"，")!=-1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            resource_alias_list.append(temp)
        '''
        print("resource_list====================================================")
        for i in resource_variant_list:
            for j in i:
                print(j)
        '''

        '''
        精品正名、别名
        '''
        cursor = cls.graph.run("match(n:`精品`)return n.office_name as goods ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            goods_list.append(record['goods'])
            if record['variant_name'].find(u"，") != -1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            goods_alias_list.append(temp)

        '''
        资源类型正名、别名
        '''
        cursor = cls.graph.run("match(n:`资源类型`)return n.office_name as restype ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            restype_list.append(record['restype'])
            if record['variant_name'].find(u"，"):
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            restype_alias_list.append(temp)

        '''
        资源类型正名、别名
        '''
        cursor = cls.graph.run("match(n:`资源中级类`)return n.office_name as multype ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            multype_list.append(record['multype'])
            if record['variant_name'].find(u"，"):
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            multype_alias_list.append(temp)
        '''
        for i in restype_variant_list:
            for j in i:
                print(j)
        '''

        '''
        资源类型正名、别名
        '''
        cursor = cls.graph.run("match(n:`资源大类`)return n.office_name as ttype ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            ttype_list.append(record['ttype'])
            if record['variant_name'].find(u"，"):
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            ttype_alias_list.append(temp)
        """
        证件别名、正名
        """
        cursor = cls.graph.run("match(n:`证件`)return n.office_name as card ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            card_list.append(record['card'])
            if record['variant_name'].find(u"，")!=-1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            #print(temp)
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            card_alias_list.append(temp)
        '''
        for i in card_variant_list:
            for j in i:
                print(j)
        '''
        """
        图书馆正名，别名
        """
        cursor = cls.graph.run("match(n:`国家图书馆`)return n.office_name as library ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            library = record['library']
            if record['variant_name'].find(u"，")!=-1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            library_alias_list.append(temp)

        '''
        for i in library_variant_list:
            for j in i:
                print(j)
        '''
        """
        服务
        """

        cursor = cls.graph.run("match(n:`服务`)return n.office_name as service ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            service_list.append(record['service'])
            if record['variant_name'].find(u"，") != -1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            service_alias_list.append(temp)

        """
        业务
        """
        cursor = cls.graph.run("match(n:`业务`)return n.office_name as task ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            task_list.append(record['task'])
            if record['variant_name'].find(u"，") != -1:
                temp = record['variant_name'].split(u"，")
            else:
                temp = [record['variant_name']]
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            task_alias_list.append(temp)

        '''
        for i in service_variant_list:
            for j in i:
                print(j)
        '''

        return room_list,room_alias_list,floor_list,floor_alias_list,area_list,area_alias_list,resource_list,resource_alias_list,restype_list,restype_alias_list,card_list,card_alias_list,library,library_alias_list,service_list,service_alias_list,task_list,task_alias_list,multype_list,multype_alias_list,ttype_list,ttype_alias_list,goods_list,goods_alias_list

    @classmethod
    def create_node(cls):

        """建立馆室节点"""
        #room_sheet = workbook.sheet_by_index(0)
        room_values = room.split("@")
        for i in range(1,len(room_values)-6):
            row = room_values[i].split(" ")
            name=row[0]
            #print("des_x,des_y",row[0],row[15],row[16])
            room_node = Node(cls.room,type=cls.room,name=name,office_name=row[0],variant_name=row[1],position=row[2],describe=row[3],
                             open_date=row[4],phone=row[5],
                             work_open=row[6],work_borrow=row[7],
                             week_open=row[8], week_borrow=row[9],
                             area=row[10],floor=row[11],
                             card=row[12],
                             des_x=row[15],
                             des_y=row[16],
                             borrow=row[19],
                             open=row[20])
            cls.graph.create(room_node)
        for i in range(len(room_values)-6,len(room_values)):

            row = room_values[i].split(" ")
            #print(row[0])
            #print("selfsite", row[0], row[14])
            mark_node = Node(cls.mark, type=cls.mark,name=row[0], office_name=row[0],self_site=row[14])
            cls.graph.create(mark_node)

        """建立馆区节点"""
        area_values = area.split("@")
        for i in range(1, len(area_values)):
            row = area_values[i].split(" ")
            name = row[0]
            area_node = Node(cls.area, type=cls.area,name=name,
                                 office_name=row[0],
                                 variant_name=row[1],
                                 position=row[2],
                                 date=row[3],
                                 worktime=row[5],
                                 weektime=row[6])

            cls.graph.create(area_node)

        """建立楼层节点"""
        floor_values = floor.split("@")
        for i in range(1, len(floor_values)):
            row = floor_values[i].split(" ")
            name = row[0]
            floor_node = Node(cls.floor, type=cls.floor,name=name, office_name=row[0], variant_name=row[1],
                              area=row[2],
                              upstair=row[3],downstair=row[4]
                              )
            cls.graph.create(floor_node)

        """建立资源节点"""
        resource_values = resource.split("@")
        for i in range(1, len(resource_values)):
            row = resource_values[i].split(" ")
            name = row[0]

            resource_node = Node(cls.resource, type=cls.resource,name=name, office_name=row[0], variant_name=row[1], describe=row[2], count=row[3],
                              room=row[4],
                              belong=row[5],
                              collection_time=row[6],
                              form=row[8],
                              topic=row[9])
            cls.graph.create(resource_node)

        """建立精品节点"""
        goods_values = goods.split("@")
        for i in range(1, len(goods_values)):
            row = goods_values[i].split(" ")
            name = row[0]

            resource_node = Node(cls.goods, type=cls.goods, name=name, office_name=row[0], variant_name=row[1],
                                 kind=row[2], writer=row[3])
            cls.graph.create(resource_node)

        '''建立证件节点'''
        card_values = card.split("@")
        for i in range(1,len(card_values)):
            row = card_values[i].split(" ")
            card_node = Node(cls.card, type=cls.card, name = row[0], office_name=row[0], variant_name=row[1], age=row[2], function=row[3])
            cls.graph.create(card_node)

        '''建立服务节点'''
        service_values = service.split("@")
        for i in range(1, len(service_values)):
            row = service_values[i].split(" ")
            service_node = Node(cls.service, type=cls.service, name=row[0], office_name=row[0], variant_name=row[1], date=row[3],
                             worktime=row[4],weektime=row[5],discribe=row[6],card=row[7])
            cls.graph.create(service_node)

        '''建立业务节点'''
        task_values = task.split("@")
        for i in range(1, len(task_values)):
            row = task_values[i].split(" ")
            print("row[3]",row[3],row[0])
            task_node = Node(cls.task, type=cls.task, name=row[0], office_name=row[0], variant_name=row[1],
                                date=row[3],
                                worktime=row[4], weektime=row[5], discribe=row[6], card=row[7])
            cls.graph.create(task_node)

        '''建立资源中级类型节点'''
        mulType_values = mulType.split("@")
        for i in range(1, len(mulType_values)):

            row = mulType_values[i].split(" ")
            restype_node = Node(cls.multype, type=cls.multype, name=row[0], office_name=row[0], variant_name=row[1])
            cls.graph.create(restype_node)

        '''建立资源类型节点'''
        resType_values = resType.split("@")
        for i in range(1, len(resType_values)):
            #print(row[4],row[3])
            row = resType_values[i].split(" ")
            restype_node = Node(cls.restype, type=cls.restype, name=row[0], office_name=row[0], variant_name=row[1], describe=row[2], kind=row[3],
                              count=row[4],
                              belong=row[5])
            cls.graph.create(restype_node)

        '''建立国家图书馆节点'''
        alias_name='图书馆，国家图书馆，国图'

        describe='国家图书馆的前身是建于1909年（清宣统元年）9月9日的京师图书馆，1912年8月27日开馆接待读者，1916年京师图书馆按规定正式接受国内出版物呈缴本，开始履行国家图书馆的部分职能，1928年7月更名为国立北平图书馆，1929年8月与北平北海图书馆合并，仍名国立北平图书馆， 1950年3月6日国立北平图书馆更名为国立北京图书馆，1951年6月12日更名为北京图书馆，1998年12月12日经国务院批准，北京图书馆更名为国家图书馆，对外称中国国家图书馆。包括文津街古籍馆、白石桥总馆南区和总馆北区三个馆区。'
        phone='010-88545114'

        library = Node(cls.library, type=cls.library, name=cls.library, office_name=cls.library, variant_name=alias_name,describe=describe,phone=phone)
        cls.graph.create(library)

        '''建立资源大类'''
        res_values = [['数字资源',19609100],['实体资源',39011882]]
        variant_name = '数字资源，电子资源，数据库资源，数据库'
        res_node = Node(cls.res, type=cls.res, name=res_values[0][0], office_name=res_values[0][0], variant_name=variant_name, num=res_values[0][1])
        cls.graph.create(res_node)
        res_node = Node(cls.res, type=cls.res, name=res_values[1][0], office_name=res_values[1][0],
                        variant_name=res_values[1][0], num=res_values[1][1])
        cls.graph.create(res_node)

    @classmethod
    def create_relation(cls):

        """建立馆室联系"""
        room_values = room.split("@")
        #room_sheet = workbook.sheet_by_index(0)
        for i in range(1, len(room_values)-6):
            try:
                row = room_values[i].split(" ")

                if row[10].find(u"，")!=-1:
                    area_arr = row[10].split(u"，")
                    for sub_area in area_arr:
                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "位于",
                                           cls.graph.find_one(label=cls.area, property_key='office_name',
                                                               property_value=sub_area))
                        cls.graph.create(rel)
                else:
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.area, property_key='office_name', property_value=row[10]))
                    cls.graph.create(rel)
                if row[11].find(u"，")!=-1:
                    floor_arr = row[11].split(u"，")
                    for sub_floor in floor_arr:
                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "位于",
                                           cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                               property_value=sub_floor))
                        cls.graph.create(rel)
                else:
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=row[0]), "位于",
                                       cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                          property_value=row[11]))
                    cls.graph.create(rel)
                #print("============================")

                if row[12].find(u"，")!=-1:

                    card_arr = row[12].split(u"，")
                    for sub_card in card_arr:
                        if sub_card == "":
                            continue
                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "证件",
                                           cls.graph.find_one(label=cls.card, property_key='office_name',
                                                               property_value=sub_card))
                        cls.graph.create(rel)
                else:
                    if row[12] == 'nan':
                        continue
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=row[0]), "证件",
                                       cls.graph.find_one(label=cls.card, property_key='office_name',
                                                          property_value=row[12]))

                    cls.graph.create(rel)
                #print(row[0],row[18],row[13],row[17])
                mark_list = row[18].split(u",")
                #print("mark_list",mark_list)
                dis_list = str(row[13]).split("_")
                dir_list = str(row[17]).split(u";")
                for i in range(len(mark_list)):
                    mark = mark_list[i]
                    #print(mark)
                    dis = dis_list[i]
                    dir = dir_list[i]

                    #print(cls.graph.find_one(label=cls.mark, property_key='office_name',
                    #                         property_value=mark))
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=row[0]), "相邻",
                                       cls.graph.find_one(label=cls.mark, property_key='office_name',
                                                          property_value=mark),
                                       dis=dis, dir=dir)
                    cls.graph.create(rel)

            except AttributeError as e:
                print("room",e)

                #print("11",row[0],e,row[10])
                #print(cls.graph.find_one(label=cls.mark, property_key='office_name',
                #                                          property_value=mark))


        for i in range(len(room_values)-6, len(room_values)):
            try:
                #print("kkk",row[0],row[13],row[15],row[16],row[17],row[18])
                row = room_values[i].split(" ")
                mark_list = row[18].split(u",")
                dis_list = str(row[13]).split(u"_")
                dir_list = str(row[17]).split(u";")
                x_list = row[15].split(u";")
                y_list = row[16].split(u";")
                for i in range(len(mark_list)):
                    mark = mark_list[i]
                    dis = dis_list[i]
                    dir = dir_list[i]
                    if len(x_list) > 0 and len(y_list) > 0:
                        x = x_list[i]
                        y = y_list[i]
                    rel = Relationship(cls.graph.find_one(label=cls.mark, property_key='office_name',
                                                          property_value=row[0]),
                                       "互连",
                                       cls.graph.find_one(label=cls.mark, property_key='office_name',
                                                          property_value=mark), dis=dis, dir=dir, x=x, y=y)

                    cls.graph.create(rel)

                rel = Relationship(cls.graph.find_one(label=cls.mark, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.area, property_key='office_name', property_value=row[10]))
                cls.graph.create(rel)



                rel = Relationship(cls.graph.find_one(label=cls.mark, property_key='office_name',
                                                      property_value=row[0]), "位于",
                                   cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                      property_value=row[11]))
                cls.graph.create(rel)


            except AttributeError as e:
                print("room",e)

        """建立楼层联系"""
        floor_values = floor.split("@")

        for i in range(1, len(floor_values)):
            try:
                row = floor_values[i].split(" ")
                rel = Relationship(cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.area, property_key='office_name', property_value=row[2]))
                cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                print("2",row[0],e,row[2])

        """建立资源联系"""
        res_values = resource.split("@")
        for i in range(1, len(res_values)):
            try:
                room_arr = []
                row = res_values[i].split(" ")
                rel = Relationship(cls.graph.find_one(label=cls.resource, property_key='office_name',
                                                      property_value=row[0]), "属于",
                                   cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                      property_value=row[5]))
                cls.graph.create(rel)
                if row[4].find(u"，")!=-1:
                    room_arr = row[4].split(u"，")
                else:
                    room_arr.append(row[4])

                for sub_room in room_arr:
                    rel = Relationship(cls.graph.find_one(label=cls.resource, property_key='office_name',
                                                       property_value=row[0]), "存放",
                                   cls.graph.find_one(label=cls.room, property_key='office_name', property_value=sub_room))
                    cls.graph.create(rel)

            except AttributeError as e:
                print("3", row[0], e, row[4],row[5])

        """建立精品联系"""
        goods_values = goods.split("@")
        for i in range(1, len(goods_values)):
            try:
                room_arr = []
                row = goods_values[i].split(" ")
                rel = Relationship(cls.graph.find_one(label=cls.goods, property_key='office_name',
                                                      property_value=row[0]), "属于",
                                   cls.graph.find_one(label=cls.resource, property_key='office_name',
                                                      property_value=row[5]))
                cls.graph.create(rel)
                if row[4].find(u"，") != -1:
                    room_arr = row[4].split(u"，")
                else:
                    room_arr.append(row[4])

                for sub_room in room_arr:
                    rel = Relationship(cls.graph.find_one(label=cls.goods, property_key='office_name',
                                                          property_value=row[0]), "存放",
                                       cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=sub_room))
                    cls.graph.create(rel)

            except AttributeError as e:
                print("goods", row[0], e, row[4], row[5])

        """建立资源类型联系"""
        resType_values = resType.split("@")
        for i in range(1, len(resType_values)):
            try:
                row = resType_values[i].split(" ")

                rel = Relationship(cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                      property_value=row[0]), "属于",
                                   cls.graph.find_one(label=cls.res, property_key='office_name',
                                                      property_value=row[5]))

                cls.graph.create(rel)
                room_arr = []
                if row[6] == 'nan':
                    continue
                if row[6].find(u"，")!=-1:
                    room_arr = row[6].split(u"，")
                else:
                    room_arr.append(row[6])
                for sub_room in room_arr:
                    rel = Relationship(cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                       property_value=row[0]), "存放",
                                   cls.graph.find_one(label=cls.room, property_key='office_name', property_value=sub_room))
                    cls.graph.create(rel)

                rel = Relationship(cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                      property_value=row[0]), "属于",
                                   cls.graph.find_one(label=cls.multype, property_key='office_name',
                                                      property_value=row[7]))
                cls.graph.create(rel)
            except AttributeError as e:
                a=0
                print("-----------",row[0],e,row[7])

        """建立服务联系"""
        service_values = service.split("@")

        for i in range(1, len(service_values)):
            try:
                row = service_values[i].split(" ")
                room_arr = []
                if row[2].find(u"，") != -1:
                    room_arr = row[2].split(u"，")
                else:
                    room_arr.append(row[2])
                for sub_room in room_arr:
                    if sub_room == 'nan':
                        continue

                    rel = Relationship(cls.graph.find_one(label=cls.service, property_key='office_name',
                                                          property_value=row[0]), "发生",
                                       cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=sub_room))
                    cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                print("-----------", row[0], e)
        """建立业务联系"""
        task_values = task.split("@")

        for i in range(1, len(task_values)):
            try:
                row = task_values[i].split(" ")
                room_arr = []
                if row[2].find(u"，") != -1:
                    room_arr = row[2].split(u"，")
                else:
                    room_arr.append(row[2])

                for sub_room in room_arr:
                    if sub_room == 'nan':
                        continue
                    rel = Relationship(cls.graph.find_one(label=cls.task, property_key='office_name',
                                                          property_value=row[0]), "办理",
                                       cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=sub_room))
                    cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                print("-----------", row[0], e)
        '''建立国家图书馆联系'''

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.area, property_key='office_name',
                                              property_value="总馆北区"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.area, property_key='office_name',
                                              property_value="总馆南区"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.area, property_key='office_name',
                                              property_value="文津楼"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.area, property_key='office_name',
                                              property_value="临琼楼"))
        cls.graph.create(rel)

    ########################################################################################
    ######################################特定任务查询########################################
    '''
    馆藏分布查询：通过资源查找对应的馆室，再通过资源查找对应的资源类别
    '''

    @classmethod
    def get_area_resource_type(cls, area):
        cursor = cls.graph.run("match (b {type:'资源类型'})<-[]-(a {type:'资源'})-[*2]->(n {office_name:{a}}) return b", a=area)
        ans = []
        while cursor.forward():
            record = cursor.current()
            if dict(record['b']) not in ans:
                ans.append(dict(record['b']))
        return ans

#Neo4jPrepare()
'''
if __name__ == '__main__':
    Neo4jPrepare()


    res = Neo4jPrepare.get_reverse_relation('基藏外文图书外借出纳台','资源')
    for r in res:
        print(r['office_name'])
'''




