# -*- coding: utf-8 -*-
from model.kb_prepare.neo4j_prepare2 import Neo4jPrepare
from model.config import GraphBaseConfig
class Task_information():
    '''
    def solve_room_borrow(self,entity):
        room = entity['room'][0]
        room_name = room
        if room.find("_")!=-1:
            room_name=room.split("_")[2]

        ans = "\n"

        res = Neo4jPrepare.get_property(room)

        if res['borrow'] == 1:
            ans+=room_name+"的资源书籍均可以外借\n"
        else:
            ans += room_name + "的资源书籍均不可以外借\n"
        return ans

    def solve_res_borrow(self,entity):
        res = entity['res'][0]
        room_res = Neo4jPrepare.get_relation(res,'馆室')
        #print(room_res)
        room = room_res[0]['office_name']
        room_name = room
        if room.find("_")!=-1:
            room_name=room.split("_")[2]
        ans = "\n"
        if room_res[0]['borrow'] == 1:
            ans+=res+"可以外借\n"
        else:
            ans += res + "不可以外借\n"
        return ans

    def solve_restype_borrow(self,entity):
        restype = entity['restype'][0]
        room_res = Neo4jPrepare.get_relation(restype,'馆室')
        #print(room_res)
        yes_room = []
        no_room = []
        for r in room_res:
            room = r['office_name']
            room_name = room
            if room.find("_") != -1:
                room_name = room.split("_")[2]
            if r['borrow'] == 1:
                yes_room.append(room_name)
            else:
                no_room.append(room_name)
        #print(yes_room,no_room)
        ans = "\n"
        if len(yes_room)>0:
            ans += "存放在"
            for y in yes_room[:-1]:
                ans += y+","
            ans += yes_room[len(yes_room)-1]+"的"+restype+"可以外借\n"
        if len(no_room)>0:
            ans += "存放在"
            for y in no_room[:-1]:
                ans += y+","
            ans += no_room[len(no_room)-1]+"的"+restype+"不可以外借\n"
        return ans
    '''
    def solve_room_phone(self, entity):
        room = entity['room'][0]
        res = Neo4jPrepare.get_property(room)
        ans = "\n"
        if res['phone'] != 'nan':
            ans += room+"的联系电话为："+res['phone']+"\n"
        else:
            ans += "很抱歉，"+room+"暂无联系电话\n"
        return ans

    def solve_library_phone(self):
        res = Neo4jPrepare.get_property(GraphBaseConfig['place'])
        #print(res)
        ans = "\n"+GraphBaseConfig['place']+"联系电话为"+res['phone']+"\n"
        return ans


    def solve_room_describe(self, entity):
        room = entity['room'][0]
        res = Neo4jPrepare.get_property(room)
        ans = "\n"
        if res['describe'] != 'nan':
            ans += room + "：" + res['describe']
        else :
            ans += "对不起，暂时没有"+room+"的描述信息\n"

        return ans

    def solve_res_describe(self, entity):
        ans = "\n"
        for resource in entity['res']:

            res = Neo4jPrepare.get_property(resource)
            if res['collection_time'] != 'nan':
                ans += GraphBaseConfig['place']+"的"+resource+"始藏于"+str(int(float(res['collection_time'])))+"年\n"
            if res['describe'] != 'nan':
                ans += res['describe']+"\n"
            if res['belong'] != 'nan':
                ans += resource+"属于"+res['belong']
            if res['form'] != 'nan':
                ans += ","+GraphBaseConfig['place']+"收藏"+resource+"包括:"+res['form']
            if res['topic'] != 'nan':
                ans += "\n涵盖的主题包括"+res['topic']+"\n"
            if ans == "" :
                ans += "对不起，暂时没有"+resource+"的描述信息\n"
        return ans

    def solve_card_describe(self):


        res = Neo4jPrepare.get_entity("证件")
        #print(res)
        ans = "\n"
        num = len(res)
        ans += "一共有"+str(num-1)+"种读者卡\n"
        for r in res:
            if r['office_name'] == '第二代身份证':
                continue
            ans += '年龄'+r['age']+'可以办理和使用'+r['office_name']+"\n"

        return ans

    def solve_finance_describe(self):
        res = Neo4jPrepare.get_property('国家图书馆读者卡')
        ans = '\n'+'读者卡的金融功能指读者卡'+res['function']+'的功能\n'
        return ans

    def solve_restype_describe(self, entity):

        restype = entity['restype'][0]

        restype_search = Neo4jPrepare.get_property(restype)

        res = Neo4jPrepare.get_reverse_relation(restype,'资源')
        res_arr=[]
        yes_res=[]
        no_res = []
        describe=[]
        ans="\n"

        if restype_search['count'] != 'nan':
            ans += restype+"在"+GraphBaseConfig['place']+"的馆藏数量为:"+restype_search['count']+"\n"
        if restype_search['describe'] != 'nan':
            ans += restype_search['describe']+"\n"
            return ans
        for r in res:
            sub_res = Neo4jPrepare.get_property(r['office_name'])

            res_arr.append(sub_res['office_name'])

            if sub_res['describe'] != 'nan':

                yes_res.append(sub_res['office_name'])
                describe.append(sub_res['describe'])

            else :
                no_res.append(sub_res['office_name'])
        if len(res)>0:
            ans += restype+"包括"
            for r in res_arr[:-1]:
                ans+=r+","
            ans += res_arr[-1]
            for y in range(len(yes_res)):
                ans += yes_res[y]+":"+describe[y]+"\n"
        return ans

    def solve_multype_describe(self, entity):
        multype = entity['multype'][0]
        restype_search = Neo4jPrepare.get_reverse_relation(multype,'资源类型')
        restype_arr = [x['office_name'] for x in restype_search]
        ans = "\n"
        if len(restype_arr)>0:
            ans += multype+"包括"
        else:
            return "很抱歉，没有"+multype+"的具体信息\n"
        for restype in restype_arr[:-1]:
            ans += restype+","
        ans += restype_arr[-1]+"\n"
        for restype in restype_arr:
            entity['restype'] = [restype]
            ans += self.solve_restype_describe(entity)[1:]
        return ans

    def solve_library_describe(self):
        res = Neo4jPrepare.get_entity(GraphBaseConfig['place'])
        ans = "\n"+res[0]['describe']
        return ans

    """
    服务实体介绍
    """
    def solve_service_describe(self,entity):
        service = entity['service'][0]
        #print(service)
        res = Neo4jPrepare.get_property(service)
        #print(res.keys())
        ans = ''
        if res['discribe'] != 'nan':
            ans = "\n"+service+"指"+res['discribe']
        else:
            room_res = Neo4jPrepare.get_relation(service,'馆室')
            for r in room_res:
                if r['describe']!='nan':
                    ans += "\n"+r['office_name']+r['describe']
        if ans == '':
            ans = "很抱歉，暂时没有"+service+"的描述信息\n"
        return ans

    """
    业务实体介绍
    """
    def solve_task_describe(self,entity):
        task = entity['task'][0]
        #print(service)
        res = Neo4jPrepare.get_property(task)
        #print(res.keys())
        ans = ''
        if res['discribe'] != 'nan':
            ans = "\n"+task+"指"+res['discribe']
        else:
            room_res = Neo4jPrepare.get_relation(task,'馆室')
            for r in room_res:
                if r['describe']!='nan':
                    ans += "\n"+r['office_name']+r['describe']
        if ans == '':
            ans = "很抱歉，暂时没有"+task+"的描述信息\n"
        return ans



    """
    馆室开放时间
    """

    def solve_room_time(self, entity):
        room = entity['room'][0]
        res = Neo4jPrepare.get_property(room)
        # print(res)
        open_day = res['open_date']
        ans = "\n"
        if open_day != 'nan':
            ans += room + "开放日为：" + open_day + "\n"
        workday_time = res['work_open']
        weekend_time = res['week_open']
        if workday_time != 'nan':
            ans += "工作日开放时间为：" + workday_time + "\n"
        if weekend_time != 'nan':
            ans += "周末开放时间为：" + weekend_time + "\n"
        if ans == "\n":
            ans += "很抱歉，没有" + room + "的时间信息\n"

        return ans

    """
    馆室的资源借阅时间
    """

    def solve_room_res_time(self, entity):
        room = entity['room'][0]
        # print(entity)
        res = Neo4jPrepare.get_property(room)
        # print("================================",res)
        workday_time = res['work_borrow']
        weekend_time = res['week_borrow']
        if workday_time == 'nan' and weekend_time == 'nan':
            return "很抱歉，" + room + "的资源材料不提供借阅\n"
        ans = "\n" + room + "的书籍材料借阅时间为："
        if workday_time != 'nan':
            ans += "\n工作日：" + workday_time
        if weekend_time != 'nan':
            ans += "\n周未：" + weekend_time
        return ans + "\n"

    """
    资源借阅时间
    """

    def solve_res_time(self, entity):
        resource = entity['res'][0]
        # print(Neo4jPrepare.get_property(resource))
        room = Neo4jPrepare.get_property(resource)['room']
        res = Neo4jPrepare.get_property(room)
        workday_time = res['work_borrow']
        weekend_time = res['week_borrow']
        if workday_time == 'nan' and weekend_time == 'nan':
            return "很抱歉，" + room + "的资源材料不提供借阅\n"
        # ans = "\n" + resource + "的借阅时间为：\n工作日：" + workday_time + "\n周未：" + weekend_time + "\n"
        ans = "\n" + resource + "存放在" + room + ","
        ans += room + "的借阅时间为："
        if workday_time != 'nan':
            ans += "\n工作日：" + workday_time
        if weekend_time != 'nan':
            ans += "\n周未：" + weekend_time
        return ans + "\n"

    """
    服务时间
    """

    def solve_service_time(self, entity):
        service = entity['service'][0]
        res = Neo4jPrepare.get_property(service)
        ans = "\n"
        if res['date'] != 'nan':
            ans += "服务日期：" + res['date'] + "\n"
        if res['worktime'] != 'nan':
            ans += "工作日服务时间为" + str(res['worktime']) + "\n"
        if res['weektime'] != 'nan':
            ans += "工作日服务时间为" + str(res['weektime']) + "\n"
        if ans == "\n":
            res_room = Neo4jPrepare.get_relation(service,"馆室")
            for room in res_room:
                if room['open_date'] != 'nan':
                    ans += room['office_name']+"的开放日为"+room['open_date']
                if room['work_open'] != 'nan':
                    ans += ",工作日开放时间为"+room['work_open']
                if room['week_open'] != 'nan':
                    ans += ",周末或节假日开放时间为"+room['week_open']+"\n"
        return ans

    """
    业务时间
    """

    def solve_task_time(self, entity):
        task = entity['task'][0]
        res = Neo4jPrepare.get_property(task)
        ans = "\n"
        if res['date'] != 'nan':
            ans += "业务日期：" + res['date'] + "\n"
        if res['worktime'] != 'nan':
            ans += "工作日服务时间为" + str(res['worktime']) + "\n"
        if res['weektime'] != 'nan':
            ans += "工作日服务时间为" + str(res['weektime']) + "\n"
        if ans == "\n":
            res_room = Neo4jPrepare.get_relation(task, "馆室")
            for room in res_room:
                if room['open_date'] != 'nan':
                    ans += room['office_name'] + "的开放日为" + room['open_date']
                if room['work_open'] != 'nan':
                    ans += ",工作日开放时间为" + room['work_open']
                if room['week_open'] != 'nan':
                    ans += ",周末或节假日开放时间为" + room['week_open'] + "\n"
        return ans

    """
    国家图书馆开放时间
    """

    def solve_library_time(self, entity):
        library = entity['library'][0]
        res = Neo4jPrepare.get_relation(library, '馆区')
        # print(res)
        ans = "\n"
        ans += library + "包括" + str(len(res)) + "个馆区\n"
        for r in res:
            ans += r['office_name'] + "开放日期为" + r['date'] + "\n"
            ans += "工作开放时间为" + r['worktime'] + "\n"
            ans += "周末开放时间为" + r['weektime'] + "\n"
        return ans

    """
    馆区开放时间
    """

    def solve_area_time(self, entity):
        area = entity['area'][0]
        res = Neo4jPrepare.get_property(area)
        # print(res)
        ans = "\n"
        if res['date'] != 'nan':
            ans += area + "开放日期为" + res['date'] + "\n"
        if res['worktime'] != 'nan':
            ans += "工作日开放时间为" + res['worktime'] + "\n"
        if res['weektime'] != 'nan':
            ans += "周末开放是时间为" + res['weektime'] + "\n"
        return ans

    """
    资源形式
    """
    def solve_res_form(self, entity):
        resource = entity['res'][0]
        res = Neo4jPrepare.get_property(resource)
        ans = "\n"
        if res['form'] != 'nan':
            ans += GraphBaseConfig['place']+"收藏的"+resource+"包括"+res['form']+"\n"
        else:
            ans += "很抱歉，暂时没有"+resource+"的形式信息\n"
        return ans

    """
    资源主题
    """

    def solve_res_topic(self, entity):
        resource = entity['res'][0]
        res = Neo4jPrepare.get_property(resource)
        ans = "\n"
        if res['topic'] != 'nan':
            ans += resource + "涵盖的主题包括" + res['form'] + "\n"
        else:
            ans += "很抱歉，暂时没有" + resource + "的主题信息\n"
        return ans
















