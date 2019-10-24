# -*- coding: utf-8 -*-

from py2neo import Node, Graph, Relationship
import xlrd
class Neo4jPrepareforbake(object):


    @classmethod
    def __init__(cls):
        """建立连接"""

        link = Graph("bolt://127.0.0.1:7687", username="lin123", password="lin123")
        cls.graph = link

        """定义label"""
        cls.building = '馆区'
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

        cls.graph.delete_all()

        """建图"""
        workbook = xlrd.open_workbook(r'../../resource/neo4j2.xlsx')
        #cls.create()
        #cls.create_node(workbook)
        #cls.create_relation(workbook)



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
        #workday_opentime = Node(cls.attribute, name="工作日开放时间")
        #cls.graph.create(workday_opentime)
        phone = Node(cls.attribute, name="电话",name2="电话")
        cls.graph.create(phone)
        describe = Node(cls.attribute, name="描述",name2="描述")
        cls.graph.create(describe)
        #weekdy_btime = Node(cls.attribute, name="周末借阅时间")
        #cls.graph.create(weekdy_btime)
        workday_btime = Node(cls.attribute, name="借阅时间",name2="借阅时间")
        cls.graph.create(workday_btime)
        borrow = Node(cls.attribute, name="借阅",name2="借阅")
        cls.graph.create(borrow)
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
        #############################################################
        library = Node(cls.library, name="国家图书馆")
        cls.graph.create(library)
        room = Node(cls.room, name="馆室")
        cls.graph.create(room)
        area = Node(cls.building, name="馆区")
        cls.graph.create(area)
        floor = Node(cls.floor, name="楼层")
        cls.graph.create(floor)
        card = Node(cls.card, name="读者卡")
        cls.graph.create(card)
        resource = Node(cls.resource, name="资源")
        cls.graph.create(resource)
        type = Node(cls.restype, name="资源类型")
        cls.graph.create(type)
        service = Node(cls.service, name="服务")
        cls.graph.create(service)
        #############################################################
        rel = Relationship(cls.graph.find_one(label=cls.library), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="位置"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.building), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.building), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="位置"))


        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="位置"))
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
        rel = Relationship(cls.graph.find_one(label=cls.room), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="借阅"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="数量"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="描述"))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.restype), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="数量"))
        cls.graph.create(rel)


        rel = Relationship(cls.graph.find_one(label=cls.card), "属性",
                           cls.graph.find_one(label=cls.attribute, property_key='name',property_value="别名"))
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
                           cls.graph.find_one(label=cls.attribute, property_key='name', property_value="描述"))
        cls.graph.create(rel)

        #############################################################

        rel = Relationship(cls.graph.find_one(label=cls.room), "位于",
                           cls.graph.find_one(label=cls.floor))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.building), "包括",
                           cls.graph.find_one(label=cls.library))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.room), "处于",
                           cls.graph.find_one(label=cls.building))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.floor), "处于",
                           cls.graph.find_one(label=cls.building))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "属于",
                           cls.graph.find_one(label=cls.restype))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.resource), "存放",
                           cls.graph.find_one(label=cls.room))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.room), "证件",
                           cls.graph.find_one(label=cls.card))
        cls.graph.create(rel)
        rel = Relationship(cls.graph.find_one(label=cls.service), "发生",
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
        #print(entity)
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
            # print(dict(record['b']))
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

        '''
        馆室正名、别名
        '''
        cursor = cls.graph.run("match(n:`馆室`)return n.office_name as room ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            room_list.append(record['room'])
            temp = record['variant_name'].split(u"，")
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
            temp = record['variant_name'].split(u"，")
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
            temp = record['variant_name'].split(u"，")
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
            temp = record['variant_name'].split(u"，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            resource_alias_list.append(temp)
        '''
        print("resource_list====================================================")
        for i in resource_variant_list:
            for j in i:
                print(j)
        '''

        '''
        资源类型正名、别名
        '''
        cursor = cls.graph.run("match(n:`资源类型`)return n.office_name as restype ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            restype_list.append(record['restype'])
            temp = record['variant_name'].split(u"，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            restype_alias_list.append(temp)
        '''
        for i in restype_variant_list:
            for j in i:
                print(j)
        '''
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
                temp = record['variant_name']
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
                temp = record['variant_name']
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            library_alias_list.append(temp)

        '''
        for i in library_variant_list:
            for j in i:
                print(j)
        '''

        cursor = cls.graph.run("match(n:`服务`)return n.office_name as service ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            service_list.append(record['service'])
            temp = record['variant_name'].split(u"，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            service_alias_list.append(temp)

        '''
        for i in service_variant_list:
            for j in i:
                print(j)
        '''

        return room_list,room_alias_list,floor_list,floor_alias_list,area_list,area_alias_list,resource_list,resource_alias_list,restype_list,restype_alias_list,card_list,card_alias_list,library,library_alias_list,service_list,service_alias_list

    @classmethod
    def create_node(cls, workbook):

        """建立馆室节点"""
        room_sheet = workbook.sheet_by_index(0)
        for i in range(1,room_sheet.nrows-6):
            row = room_sheet.row_values(i)
            name=row[0]
            if row[0].find("_") != -1:
                name_arr = row[0].split("_")
                if len(name_arr)>=3:
                    name = name_arr[2]


            room_node = Node(cls.room,type=cls.room,name=name,office_name=row[0],variant_name=row[1],position=row[2],describe=row[3],
                             open_date=row[4],phone=row[5],
                             monday_open=row[6],monday_borrow=row[7],
                             tuseday_open=row[8],tuseday_borrow=row[9],
                             wednesday_open=row[10],wednesday_borrow=row[11],
                             thursday_open=row[12],thursday_borrow=row[13],
                             friday_open=row[14], friday_borrow=row[15],
                             saturday_open=row[16], saturday_borrow=row[17],
                             sunday_open=row[18], sunday_borrow=row[19],
                             area=row[20],floor=row[21],
                             card=row[22],
                             des_x=row[25],
                             des_y=row[26],
                             borrow=row[29]

                             )
            cls.graph.create(room_node)
        for i in range(room_sheet.nrows-6,room_sheet.nrows):
            row = room_sheet.row_values(i)
            mark_node = Node(cls.mark, type=cls.mark,name=row[0], office_name=row[0],self_site=row[24])
            cls.graph.create(mark_node)


        """建立馆区节点"""
        building_sheet = workbook.sheet_by_index(2)
        for i in range(1, building_sheet.nrows):
            row = building_sheet.row_values(i)
            name = row[0]
            #print(name)
            building_node = Node(cls.building, type=cls.building,name=name,
                                 office_name=row[0],
                                 variant_name=row[1],
                                 position=row[2],
                                 date=row[3],
                                 #weekdate=row[4],
                                 worktime=row[5],
                                 weektime=row[6])

            cls.graph.create(building_node)

        """建立楼层节点"""
        floor_sheet = workbook.sheet_by_index(4)
        for i in range(1, floor_sheet.nrows):
            row = floor_sheet.row_values(i)
            name = row[0]
            #print(name)
            floor_node = Node(cls.floor, type=cls.floor,name=name, office_name=row[0], variant_name=row[1],
                              area=row[2],
                              upstair=row[3],downstair=row[4]
                              )
            cls.graph.create(floor_node)

        """建立资源节点"""
        resource_sheet = workbook.sheet_by_index(3)
        for i in range(1, resource_sheet.nrows):
            row = resource_sheet.row_values(i)
            #print(row)
            name = row[0]
            if row[0].find("_") != -1:
                name = row[0].split("_")[1]
            # print(name)
            resource_node = Node(cls.resource, type=cls.resource,name=name, office_name=row[0], variant_name=row[1], describe=row[2], count=row[3],
                              room=row[4],
                              belong=row[5],
                              ctime=row[6],
                              range=row[8],
                              topic=row[9]
                                 )
            cls.graph.create(resource_node)

        '''建立证件节点'''
        card_sheet = workbook.sheet_by_index(1)
        for i in range(1,card_sheet.nrows):
            row = card_sheet.row_values(i)
            card_node = Node(cls.card, type=cls.card, name = row[0], office_name=row[0], variant_name=row[1], age=row[2], function=row[3])
            cls.graph.create(card_node)

        '''建立服务节点'''
        service_sheet = workbook.sheet_by_index(7)
        for i in range(1, service_sheet.nrows):
            row = service_sheet.row_values(i)
            #print(row,row)
            service_node = Node(cls.service, type=cls.service, name=row[0], office_name=row[0], variant_name=row[1], date=row[3],
                             worktime=row[4],weektime=row[5],discribe=row[6],card=row[7])
            cls.graph.create(service_node)

        '''建立资源类型节点'''
        restype_sheet = workbook.sheet_by_index(6)
        for i in range(1, restype_sheet.nrows):

            row = restype_sheet.row_values(i)
            restype_node = Node(cls.restype, type=cls.restype, name=row[0], office_name=row[0], variant_name=row[1], describe=row[2], count=row[3],
                              room=row[4],
                              belong=row[5])
            cls.graph.create(restype_node)

        '''建立国家图书馆节点'''
        variant_name='图书馆，国家图书馆'

        describe='国家图书馆的前身是建于1909年（清宣统元年）9月9日的京师图书馆，1912年8月27日开馆接待读者，1916年京师图书馆按规定正式接受国内出版物呈缴本，开始履行国家图书馆的部分职能，1928年7月更名为国立北平图书馆，1929年8月与北平北海图书馆合并，仍名国立北平图书馆， 1950年3月6日国立北平图书馆更名为国立北京图书馆，1951年6月12日更名为北京图书馆，1998年12月12日经国务院批准，北京图书馆更名为国家图书馆，对外称中国国家图书馆。包括文津街古籍馆、白石桥总馆南区和总馆北区三个馆区。'
        library = Node(cls.library, type=cls.library, name=cls.library, office_name=cls.library, variant_name=variant_name,
                       describe=describe)
        cls.graph.create(library)

        '''建立资源大类'''
        res_sheet = workbook.sheet_by_index(8)
        for i in range(1, res_sheet.nrows):
            row = res_sheet.row_values(i)
            res_node = Node(cls.res, type=cls.res, name=row[0], office_name=row[0], variant_name=row[0], num=row[1])
            cls.graph.create(res_node)



    @classmethod
    def create_relation(cls, workbook):

        """建立馆室联系"""

        room_sheet = workbook.sheet_by_index(0)
        for i in range(1, room_sheet.nrows-5-8):
            try:
                row = room_sheet.row_values(i)

                if row[20].find(u"，")!=-1:
                    area_arr = row[21].split(u"，")
                    for sub_area in area_arr:

                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "位于",
                                           cls.graph.find_one(label=cls.building, property_key='office_name',
                                                               property_value=sub_area))
                        cls.graph.create(rel)
                else:
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.building, property_key='office_name', property_value=row[20]))
                    cls.graph.create(rel)
                if row[21].find(u"，")!=-1:
                    floor_arr = row[21].split(u"，")
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
                                                          property_value=row[21]))
                    cls.graph.create(rel)
                if row[22].find(u"，")!=-1:

                    card_arr = row[22].split(u"，")
                    for sub_card in card_arr:
                        if sub_card == "":
                            continue
                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "证件",
                                           cls.graph.find_one(label=cls.card, property_key='office_name',
                                                               property_value=sub_card))
                        cls.graph.create(rel)
                else:
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=row[0]), "证件",
                                       cls.graph.find_one(label=cls.card, property_key='office_name',
                                                          property_value=row[22]))

                    cls.graph.create(rel)

            except AttributeError as e:
                a=0
                '''
                print("11",row[0],e,row[20])
                print(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]))
                '''
        for i in range(room_sheet.nrows - 5-8, room_sheet.nrows-8):
            try:
                row = room_sheet.row_values(i)
                #print(self.graph.find_one(label=self.building, property_key='area', property_value=row[20]),row[20])
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.room, property_key='office_name', property_value=row[20]))
                cls.graph.create(rel)
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                       property_value=row[0]), "位于",
                                   cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                       property_value=row[21]))
                cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                #print("2",row[0],e,row[20])
                #print(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   #property_value=row[0]))
                #print(cls.graph.find_one(label=cls.room, property_key='office_name', property_value=row[20]))


        """建立楼层联系"""
        floor_sheet = workbook.sheet_by_index(4)
        for i in range(1, floor_sheet.nrows):
            try:
                row = floor_sheet.row_values(i)
                rel = Relationship(cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.building, property_key='office_name', property_value=row[2]))
                cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                #print("2",row[0],e,row[2])

        """建立资源联系"""
        res_sheet = workbook.sheet_by_index(3)
        for i in range(1, res_sheet.nrows):
            try:

                room_arr = []
                row = res_sheet.row_values(i)

                rel = Relationship(cls.graph.find_one(label=cls.resource, property_key='office_name',
                                                      property_value=row[0]), "属于",
                                   cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                      property_value=row[5]))
                cls.graph.create(rel)
                #print(row[4])
                if row[4].find(u"，")!=-1:
                    room_arr = row[4].split(u"，")
                else:
                    room_arr.append(row[4])

                for sub_room in room_arr:
                    #print(sub_room,row[0])

                    rel = Relationship(cls.graph.find_one(label=cls.resource, property_key='office_name',
                                                       property_value=row[0]), "存放",
                                   cls.graph.find_one(label=cls.room, property_key='office_name', property_value=sub_room))
                    cls.graph.create(rel)

            except AttributeError as e:
                a = 0
                #print("3", row[0], e, row[4])
                #print(cls.graph.find_one(label=cls.room, property_key='office_name', property_value=row[4]))
                #print(self.graph.find_one(label=self.room, property_key='room', property_value=row[4]))

        for i in range(room_sheet.nrows-8, room_sheet.nrows-6):
            try:
                row = room_sheet.row_values(i)
                mark_list = row[28].split(u"，")
                dis_list = str(row[23]).split("_")
                dir_list = str(row[27]).split(u";")
                #print("marklist==================================",mark_list,row[0])
                for i in range(len(mark_list)):
                    mark = mark_list[i]
                    dis = dis_list[i]
                    dir = dir_list[i]
                    rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=row[0]), "相邻",
                                       cls.graph.find_one(label=cls.mark, property_key='office_name', property_value=mark),
                                       dis=dis, dir=dir)
                    #print(rel)
                    cls.graph.create(rel)
                #print(self.graph.find_one(label=self.building, property_key='area', property_value=row[20]),row[20])
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.building, property_key='office_name', property_value=row[20]))
                cls.graph.create(rel)
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                      property_value=row[0]), "位于",
                                   cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                      property_value=row[21]))
                cls.graph.create(rel)
                if row[22].find(u"，"):
                    card_arr = row[22].split(u"，")
                    for sub_card in card_arr:
                        if sub_card == '':
                            continue
                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "证件",
                                           cls.graph.find_one(label=cls.card, property_key='office_name',
                                                               property_value=sub_card))
                        cls.graph.create(rel)
                cls.graph.create(rel)

            except AttributeError as e:
                a = 0
                #print("11",row[0],e,row[20])
                #print(cls.graph.find_one(label=cls.room, property_key='office_name',
                #                                  property_value=row[0]))

        for i in range(room_sheet.nrows-6, room_sheet.nrows):
            try:
                row = room_sheet.row_values(i)
                mark_list = row[28].split(u"，")
                dis_list = str(row[23]).split(u"_")
                dir_list = str(row[27]).split(u";")
                x_list = row[25].split(u";")
                y_list = row[26].split(u";")
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
                               cls.graph.find_one(label=cls.building, property_key='office_name', property_value=row[20]))
                cls.graph.create(rel)



                rel = Relationship(cls.graph.find_one(label=cls.mark, property_key='office_name',
                                                      property_value=row[0]), "位于",
                                   cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                      property_value=row[21]))
                cls.graph.create(rel)
                #print("....")
                if row[22].find(u"，"):
                    card_arr = row[22].split(u"，")
                    for sub_card in card_arr:
                        if sub_card=='':
                            continue

                        rel = Relationship(cls.graph.find_one(label=cls.mask, property_key='office_name',
                                                               property_value=row[0]), "证件",
                                           cls.graph.find_one(label=cls.card, property_key='office_name',
                                                               property_value=sub_card))
                        cls.graph.create(rel)


            except AttributeError as e:
                print("1",row[0],e,row[21])
                print(cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                   property_value=row[21]))
        """建立资源类型联系"""
        restype_sheet = workbook.sheet_by_index(6)
        for i in range(1, restype_sheet.nrows):
            try:

                row = restype_sheet.row_values(i)
                #print("==========================",row[0])

                rel = Relationship(cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                      property_value=row[0]), "属于",
                                   cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                      property_value=row[5]))

                cls.graph.create(rel)
                room_arr = []
                if row[4].find(u"，")!=-1:
                    room_arr = row[4].split(u"，")
                else:
                    room_arr.append(row[4])


                for sub_room in room_arr:
                    #print("===========================================",sub_room,row[0])

                    rel = Relationship(cls.graph.find_one(label=cls.restype, property_key='office_name',
                                                       property_value=row[0]), "存放",
                                   cls.graph.find_one(label=cls.room, property_key='office_name', property_value=sub_room))
                    cls.graph.create(rel)
            except AttributeError as e:
                a=0
                print("-----------",row[0],e)

        """建立服务联系"""
        restype_sheet = workbook.sheet_by_index(7)
        for i in range(1, restype_sheet.nrows):
            try:
                row = restype_sheet.row_values(i)
                room_arr = []
                #print("===========",row[2])
                if row[2].find(u"，") != -1:
                    room_arr = row[2].split(u"，")
                else:
                    room_arr.append(row[2])


                for sub_room in room_arr:
                    if sub_room == '':
                        print(sub_room)
                        continue

                    rel = Relationship(cls.graph.find_one(label=cls.service, property_key='office_name',
                                                          property_value=row[0]), "发生",
                                       cls.graph.find_one(label=cls.room, property_key='office_name',
                                                          property_value=sub_room))
                    cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                print("-----------", row[0], e)
        '''建立国家图书馆联系'''
        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.building, property_key='office_name',
                                              property_value="总馆北区"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.building, property_key='office_name',
                                              property_value="总馆南区"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.building, property_key='office_name',
                                              property_value="文津楼"))
        cls.graph.create(rel)

        rel = Relationship(cls.graph.find_one(label=cls.library, property_key='office_name',
                                              property_value=cls.library), "包括",
                           cls.graph.find_one(label=cls.building, property_key='office_name',
                                              property_value="临琼楼"))
        cls.graph.create(rel)


if __name__ == '__main__':
    Neo4jPrepare()


    res = Neo4jPrepare.get_reverse_relation('基藏外文图书外借出纳台','资源')
    for r in res:
        print(r['office_name'])




