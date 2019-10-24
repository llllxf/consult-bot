# -*- coding: utf-8 -*-
from model.kb_prepare.neo4j_prepare2 import Neo4jPrepare
import numpy as np
import random
class Task_business():



    """
    书籍推荐任务，根据监测到的年龄性别信息来实现推荐算法
    """
    def get_kind(self, age, sex):
        recommand_book_male = ['漫画', '武侠', '历史']
        recommand_book_female = ['童话', '青春文学', '女性文学']
        recommand_book_none = '其他'
        age = int(age)
        if sex == '男':
            if age <= 15:
                return recommand_book_male[0]
            elif age <= 25:
                return recommand_book_male[1]
            else:
                return recommand_book_male[2]
        elif sex == '女':
            if age <= 15:
                return recommand_book_female[0]
            elif age <= 25:
                return recommand_book_female[1]
            else:
                return recommand_book_female[2]
        else:
            return recommand_book_none

    def solve_recommend_book2(self, age, sex):
        kind = self.get_kind(age,sex)
        ans = "猜测您可能喜欢"+kind+"类书籍,图书馆有"
        goods = Neo4jPrepare.get_entity_for_kind('精品',kind)
        for g in goods:
            ans += g['office_name']+",存放在"
            room = Neo4jPrepare.get_relation(g['office_name'],'馆室')
            ans += room[0]['office_name']+"\n"
        return ans

    def solve_recommend_book(self, age, sex):
        kind = self.get_kind(age,sex)
        ans = "猜测您可能喜欢"+kind+"类书籍,图书馆有"
        goods = Neo4jPrepare.get_entity_for_kind('精品', kind)
        good_index = random.randint(0, len(goods) - 1)
        g = goods[good_index]
        ans += g['office_name'] + ",存放在"
        room = Neo4jPrepare.get_relation(g['office_name'], '馆室')
        ans += room[0]['office_name'] + "\n"
        return ans


    def solve_recommend_book_other(self):

        ans = "推荐你借阅图书馆的"
        goods = Neo4jPrepare.get_entity_for_kind('精品','其他')
        good_index = random.randint(0, len(goods)-1)
        g = goods[good_index]
        ans += g['office_name']+",存放在"
        room = Neo4jPrepare.get_relation(g['office_name'],'馆室')
        ans += room[0]['office_name']+"\n"
        return ans

    """
    是否提供服务
    """
    def solve_service_exit(self, entity):
        #print(entity)
        service = entity['service']
        #res = Neo4jPrepare.get_property(service)
        ans = "\n"
        if len(service)>0:
            ans += "国家图书馆提供"+service[0]+"\n"
            room = Neo4jPrepare.get_relation(service[0], "馆室")
            ans = "\n" + "您可以去"
            for r in room[:-1]:
                ans += r['office_name'] + ","
            ans += room[-1]['office_name'] + "接受该服务\n"
        else:
            ans += "很抱歉，国家图书馆不提供该服务"
        return ans

    """
    馆室是否提供服务
    """

    def solve_service_exit(self, entity):
        # print(entity)
        service = entity['service']
        # res = Neo4jPrepare.get_property(service)
        ans = "\n"
        if len(service) > 0:
            ans += "国家图书馆提供" + service[0] + "\n"
            room = Neo4jPrepare.get_relation(service[0], "馆室")
            ans = "\n" + "您可以去"
            for r in room[:-1]:
                ans += r['office_name'] + ","
            ans += room[-1]['office_name'] + "接受该服务\n"
        else:
            ans += "很抱歉，国家图书馆不提供该服务"
        return ans




    """
    资源借阅，描述存放的馆室以及进入馆室的条件
    """
    def solve_res_read(self, entity):
        resource  = entity['res'][0]
        res = Neo4jPrepare.get_relation(resource,'馆室')

        ans = "\n"+resource+"存放在"
        for r in res[:-1]:
            ans += r['office_name']+","

        ans += res[-1]['office_name']+"\n"
        card = Neo4jPrepare.get_relation(res[-1]['office_name'],'证件')

        for c in card:
            ans += "年龄"+c['age']+"可持"+c['office_name']+"进入馆室\n"
        return ans

    """
    资源借阅，描述存放的馆室以及进入馆室的条件
    """

    def solve_restype_read(self, entity):
        restype = entity['restype'][0]
        res = Neo4jPrepare.get_relation(restype, '馆室')

        ans = "\n" + restype + "存放在"
        for r in res[:-1]:
            ans += r['office_name'] + ","

        ans += res[-1]['office_name'] + "\n"
        card = Neo4jPrepare.get_relation(res[-1]['office_name'], '证件')

        for c in card:
            ans += "年龄" + c['age'] + "可持" + c['office_name'] + "进入馆室\n"
        return ans

    """
    作废了
    """
    def solve_money_back(self):
        res = Neo4jPrepare.get_property('退押金')
        card = res['card']
        card_arr = card.split(u"，")
        ans = "\n请到相应阅览室/服务点还清所借图书，确认无欠款后，持"
        for c in card_arr[:-2]:
            ans += c+","
        ans += card_arr[len(card_arr)-2]
        ans += "到办证处办理退押金手续\n"
        return ans


    def solve_money_back_no(self):
        res = Neo4jPrepare.get_property('退押金')
        card = res['card']
        card_arr = card.split(u"，")
        ans = "\n请到相应阅览室/服务点还清所借图书，确认无欠款后，持"
        for c in card_arr[:-1]:
            ans += c+","
        ans += card_arr[len(card_arr)-1]
        ans += "到办证处办理退押金手续\n"
        return ans

    """
    馆区的资源是否可以外借，考虑该馆区的所有的馆室，得到可以外借的馆室是哪一些，可以复制或扫描的馆室是哪一些，哪些馆室的资源仅供借阅
    """
    def solve_area_borrow(self,entity):
        area = entity['area'][0]
        ans = "\n"

        room_res = Neo4jPrepare.get_reverse_relation(area,'馆室')
        borrow_room = []
        borrow_floor = []
        copy_room = []
        copy_floor=[]
        copy = []
        for r in room_res:
            #print(r['borrow'])
            if r['borrow'] == '1':
                room_name = r['office_name']
                #print(room_name)
                borrow_room.append(room_name)
                borrow_floor.append(r['floor'])
            elif r['borrow'] == '2':
                room_name = r['office_name']
                copy_room.append(room_name)
                copy_floor.append(r['floor'])
            elif '复制处' in r['variant_name']:
                if r['floor'] in copy:
                    continue
                if r['floor'].find("，")!=-1:
                    floor_arr = r['floor'].split("，")
                    for sub_floor in floor_arr:
                        copy.append(sub_floor)
                else:
                    copy.append(r['floor'])
        copy = np.unique(copy)
        if len(borrow_room)>0:
            for b in range(len(borrow_room)-1):
                ans += borrow_floor[b]+"的"+borrow_room[b]+","
            ans += borrow_floor[-1]+"的"+borrow_room[-1]+"的书籍材料资源可以外借\n"
        if len(copy_room)>0:
            for c in range(len(copy_room)-1):
                ans += copy_floor[c]+"的"+copy_room[c]+","
            ans += copy_floor[-1]+"的"+copy_room[-1]+"的书籍材料资源不可以外借，但可以复制或扫描\n"

            for f in copy[:-1]:
                #print(f)
                ans += f + ","
            ans += copy[-1]
            ans += "提供复制处，可携带读者卡前往该楼层复制处复制或扫描\n"
        if ans == "\n":
            ans += area + "的资源不可外借或复制\n"
        else:
            ans += "剩余馆室的资源不可复制或外借\n"
        #print(ans)

        return ans

    """
    馆室的资源是否可以外借
    """
    def solve_room_borrow(self,entity):
        room = entity['room'][0]
        room_name = room
        if room.find("_")!=-1:
            room_name=room.split("_")[2]

        ans = "\n"

        res = Neo4jPrepare.get_property(room)

        if res['borrow'] == 1:
            ans+=room_name+"的资源书籍均可以外借，外借书籍需去相应的馆室柜台预约\n"
        elif res['borrow'] == 2:
            ans += room_name + "的资源书籍均不允许外借，但可以复制与扫描\n"
        else:
            ans += room_name + "的资源书籍均不可以外借，仅供借阅\n"
        return ans

    """
    资源是否可以外借，通过查询馆室得到该馆室的资源是否可以外借来判断资源是否可以外借
    """
    def solve_res_borrow(self,entity):
        res = entity['res'][0]
        room_res = Neo4jPrepare.get_relation(res,'馆室')
        ans = "\n"
        if room_res[0]['borrow'] == 1:
            ans+=res+"可以外借\n"
        elif room_res[0]['borrow'] == 2:
            ans += res + "不可以外借，但可以复制与扫描\n"
        else:
            ans += res + "不可以外借，仅供借阅\n"
        return ans

    """
    某类资源是否可以外借，需先查出此类资源包括什么资源，具体某个资源是否可以外借（需借助馆室的外借信息）
    """
    def solve_restype_borrow(self,entity):
        restype = entity['restype'][0]
        res_res = Neo4jPrepare.get_reverse_relation(restype,'资源')
        #print(res_res)
        yes_room = []
        copy_room = []
        no_room = []

        for res in res_res:
            room_res = Neo4jPrepare.get_relation(res['office_name'],'馆室')
            for r in room_res:
                room = r['office_name']

                if r['borrow'] == 1:
                    yes_room.append(room)
                elif r['borrow'] == 2:
                    copy_room.append(room)
                else:
                    no_room.append(room)
                copy_room = np.unique(copy_room)
        ans = "\n"
        if len(yes_room)>0:
            ans += "存放在"
            for y in yes_room[:-1]:
                ans += y+","
            ans += yes_room[len(yes_room)-1]+"的"+restype+"可以外借\n"
        if len(copy_room)>0:
            ans += "存放在"
            for c in copy_room[:-1]:
                ans += c+","
            ans += copy_room[len(copy_room) - 1] + "的" + restype + "可以不外借，但可以复制和扫描\n"
        if len(no_room)>0:
            ans += "存放在"
            for y in no_room[:-1]:
                ans += y+","
            ans += no_room[len(no_room)-1]+"的"+restype+"不可以外借，仅供借阅\n"
        return ans

    #def solve_multype_borrow(self, entity):



    '''
    某层的资源是否可以外借（借助馆室的外借信息，查出该层的所有的馆室，得出可以外借资源的馆室有哪些，哪些馆室的资源可以复制和扫描，哪些仅供借阅）
    '''
    def solve_floor_borrow(self,entity):
        floor = entity['floor'][0]
        ans = "\n"

        room_res = Neo4jPrepare.get_reverse_relation(floor, '馆室')
        borrow_room = []
        copy_room = []
        for r in room_res:
            # print(r['borrow'])
            if r['borrow'] == '1':
                room_name = r['office_name']
                # print(room_name)
                borrow_room.append(room_name)
            elif r['borrow'] == '2':
                room_name = r['office_name']
                copy_room.append(room_name)
        if len(borrow_room) > 0:
            for b in range(len(borrow_room) - 1):
                ans += borrow_room[b] + ","
            ans += borrow_room[-1] + "的书籍材料资源可以外借\n"
        if len(copy_room) > 0:
            for c in range(len(copy_room) - 1):
                ans += copy_room[c] + ","
            ans += copy_room[-1] + "的书籍材料资源不可以外借，但可以复制或扫描\n"
        if ans == "\n":
            ans += floor+"的资源不可外借与复制\n"
        else:
            ans += "其余馆室不可复制或外借资源\n"
        return ans
        # print(ans)

    """
    还书手续
    """
    def solve_return_back_res(self,entity):
        resource = entity['res'][0]
        ans = "\n"
        res_res = Neo4jPrepare.get_relation(resource,'馆室')
        print(res_res)
        if len(res_res)>0:
            ans += resource+"存放于"+res_res[0]['office_name']+",请前往"+res_res[0]['office_name']+"归还书籍,同时你也可以前往总馆南区24小时自助还书处归还书籍\n"
        else:
            ans += '你可以前往总馆南区24小时自助还书处归还书籍\n'
        return ans

    """
    资源查找
    实体资源返回目录查询地点
    电子资源加上数字共享空间
    """
    def solve_res_search(self,entity):
        resource = entity['res'][0]

        ans = "\n国家图书馆提供目录查询服务，您可以前往目录查询区查询\n"
        room_res_search = Neo4jPrepare.get_relation('目录服务', '馆室')
        res_search = [x['office_name'] for x in room_res_search]
        room = Neo4jPrepare.get_relation(resource, '馆室')
        room_arr = [x['office_name'] for x in room]

        ans_arr=[]
        for sub_room in room_arr:
            if sub_room in res_search:
                ans_arr.append(sub_room)
        if '数字共享空间' in room_arr:
            ans_arr.append("数字共享空间")

        if len(ans_arr)>0:
            ans += "您还可以去:\n"
            for sub_ans in ans_arr[:-1]:
                ans += sub_ans+","
            ans += ans_arr[-1]+"进行目录查询\n"

        return ans

    def solve_get_card(self,entity_dict,age,sex):
        if age == None:
            return "对不起，并没有检测到您的年龄信息，请您前往办证处询问具体办证方式\n"
        age = int(age)
        if age>15:
            return "检测到您的年龄为"+str(age)+",性别为"+sex+",请持本人身份证件原件（包括身份证、户口簿、军人证、护照、港澳通行证、台胞回乡证）去办证处办理\n"
        elif age>12:
            return "检测到您的年龄为"+str(age)+",性别为"+sex+",请由监护人陪同，并持本人及监护人有效身份证件原件和复印件（包括身份证、户口簿、军人证、护照、港澳通行证、台胞回乡证）办理\n"
        else:
            return "检测到您的年龄为"+str(age)+",性别为"+sex+",请由监护人陪同，持本人及监护人有效身份证件原件和复印件（包括身份证、户口簿、学籍卡、军人证、护照、港澳通行证、台胞回乡证），到办证处填写《国家图书馆少年儿童馆读者卡申请表》即可办理少年儿童馆读者卡\n"


    def solve_borrow_card(self,age):
        if age == None:
            return "年龄满16岁的读者可以持国家图书馆读者卡或身份证借阅书籍\n年龄13-15岁的读者可以持国家图书馆读者卡借阅书籍\n年龄未满13岁的读者可以持少年儿童读者卡借阅书籍"
        age = int(age)
        if age>15:
            return "年龄满16岁的读者可以持国家图书馆读者卡或身份证借阅书籍\n"
        elif age>12:
            return "年龄13-15岁的读者可以持国家图书馆读者卡借阅书籍\n"
        else:
            return "年龄未满13岁的读者可以持少年儿童读者卡借阅书籍\n"














    '''
    办理读者卡
    solve__card_yes 中国籍满16岁
    solve__card_no 非中国籍满16岁
    solve__card_thirteen 13-15岁
    solve__card_twelve 未满十三岁
    '''
    def solve__card_yes(self):
        return "国家图书馆读者卡分人工办证和自助办证两种。\n人工办证：每日16：30之前在办证处办理；自助办证：总馆北区和南区办证处设有自助办证机，可于周一至周五9：00--21：00，周六和周日9：00--17：00自助办理。\n年满十六周岁的中国公民须持本人身份证件原件（包括身份证、户口簿、军人证、护照、港澳通行证、台胞回乡证）办理。\n"
    def solve__card_no(self):
        return "国家图书馆读者卡分人工办证和自助办证两种。\n人工办证：每日16：30之前在办证处办理；自助办证：总馆北区和南区办证处设有自助办证机，可于周一至周五9：00--21：00，周六和周日9：00--17：00自助办理。\n年满十六周岁的外籍人士需持护照原件办理。\n"
    def solve__card_thirteen(self):
        return "国家图书馆读者卡分人工办证和自助办证两种。\n人工办证：每日16：30之前在办证处办理；自助办证：总馆北区和南区办证处设有自助办证机，可于周一至周五9：00--21：00，周六和周日9：00--17：00自助办理。\n年满十三至十五周岁的中国公民和外籍人士，需由监护人陪同，并持本人及监护人有效身份证件原件和复印件（包括身份证、户口簿、军人证、护照、港澳通行证、台胞回乡证）办理\n"
    def solve__card_twelve(self):
        return "国家图书馆读者卡分人工办证和自助办证两种。\n人工办证：每日16：30之前在办证处办理；自助办证：总馆北区和南区办证处设有自助办证机，可于周一至周五9：00--21：00，周六和周日9：00--17：00自助办理。\n十二周岁及以下的中国公民和外籍人士，由监护人陪同，持本人及监护人有效身份证件原件和复印件（包括身份证、户口簿、学籍卡、军人证、护照、港澳通行证、台胞回乡证），到办证处填写《国家图书馆少年儿童馆读者卡申请表》即可办理少年儿童馆读者卡。\n"