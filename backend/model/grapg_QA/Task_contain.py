# -*- coding: utf-8 -*-
from model.kb_prepare.neo4j_prepare2 import Neo4jPrepare
import numpy as np
from model.config import GraphBaseConfig
class Task_contain():

    """
    统计某层馆室数量
    """
    def solve_floor_count_room(self, entity):
        floor = entity['floor'][0]
        res = Neo4jPrepare.get_reverse_relation(floor, '馆室')
        l = len(res)
        ans = "\n" + floor + "一共有" + str(l) + "间馆室\n"
        return ans

    """
    查出楼层是否有某一间馆室
    """
    def solve_floor_room_a(self,entity):
        floor = entity['floor'][0]
        res = Neo4jPrepare.get_reverse_relation(floor,'馆室')
        ans = "\n"+floor+"有馆室"
        for r in res[:-1]:
            room_name = r['office_name']
            if room_name.find(u"_")!=-1:
                room_name = room_name.split("_")[2]
            ans += room_name+","
        room_name = res[-1]['office_name']
        if room_name.find(u"_") != -1:
            room_name = room_name.split("_")[2]
            ans += room_name + "\n"

        return ans

    """
    查出楼层所有的馆室
    """
    def solve_room_floor(self,entity):
        floor = entity['floor'][0]
        room = entity['room'][0]
        res = Neo4jPrepare.get_relation(room,'楼层')
        ans = "\n"
        room_name = room
        if room.find("_")!=-1:
            room_name = room.split("_")[2]
        if res[0]['office_name'] == floor:
            ans += room_name+"在"+floor
        else:
            ans += room_name+"不在"+floor+"\n"+room_name+"在"+res[0]['office_name']+"\n"
        return ans

    """
    处理资源是否在某个楼层的问题，查询资源所在的馆室以及馆室所在的楼层来得到判断结果
    """
    def solve_res_floor(self, entity):
        resource = entity['res'][0]
        floor = entity['floor'][0]
        res = Neo4jPrepare.get_relation(resource,'馆室')
        room_name = res[0]['office_name']
        if room_name.find("_")!=-1:
            room_name = res[0]['office_name'].split("_")[2]
        des_floor = Neo4jPrepare.get_relation(res[0]['office_name'],'楼层')
        ans = "\n"
        if floor == des_floor[0]['office_name']:
            ans += resource+"存放在"+floor
            ans += self.solve_count_res(entity)
        else:
            ans += resource+"不存放在"+floor+"\n"+resource+"存放在"+des_floor[0]['office_name']+"的"+room_name
        return ans

    """
    楼层包括什么资源，通过查询楼层包含馆室的资源类型来汇总得到楼层包含的资源类型
    """
    def solve_res_floor_a(self, entity):

        floor = entity['floor'][0]
        res = Neo4jPrepare.get_reverse_relation(floor,'馆室')
        resource_arr = []
        for r in res:
            res_arr = Neo4jPrepare.get_reverse_relation(r['office_name'],'资源')
            for sub_r in res_arr:
                resource_arr.append(sub_r['belong'])

        resource_arr = np.unique(resource_arr)

        ans = "\n"
        ans += floor+"存放有"
        for sub_r in resource_arr[:-1]:
            ans += sub_r+","
        ans += resource_arr[-1]+"等类型的资源\n"
        return ans

    """
    查出馆室是否有某个资源
    """
    def solve_res_room(self, entity):
        room = entity['room'][0]

        resource = entity['res'][0]
        res = Neo4jPrepare.get_relation(resource, '馆室')
        ans = "\n"
        if res[0]['office_name'] == room:
            ans += resource+"存放在"+room
            ans += self.solve_count_res(entity)
        else:
            des_room = res[0]['office_name']
            if res[0]['office_name'].find(u"_")!=-1:
                des_room = res[0]['office_name'].split("_")[2]
            ans += resource+"不存放在"+room+"\n"+resource+"存放在"+des_room+"\n"
        return ans

    """
    查出馆室是否有某种资源的
    """
    def solve_restype_room(self, entity):

        room = entity['room'][0]
        restype = entity['restype'][0]
        res = Neo4jPrepare.get_relation_mul(restype, '馆室')
        ans = "\n"
        room_arr = [r['office_name'] for r in res]
        print(room_arr)

        if room in room_arr:
            ans += room + "存有" + restype
            ans += self.solve_count_res(entity)
        else:
            ans += restype + "不存放在" + room + "\n" + restype + "存放在"
            for r in room_arr[:-1]:
                ans += r +","
            ans += room_arr[-1]+"\n"

        return ans

    """
    查出馆区是否有某种资源的
    """

    def solve_restype_area(self, entity):
        ans = "\n"
        area = entity['area'][0]

        restype = entity['restype'][0]

        resource = Neo4jPrepare.get_reverse_relation(restype,'资源')
        resource_arr = [x['office_name'] for x in resource]
        ans += restype+"包括"
        for sub_res in resource_arr:
            ans += sub_res+","
        res = Neo4jPrepare.get_relation_triple(restype, '馆区')

        area_arr = [r['office_name'] for r in res]

        if area in area_arr:
            ans += area + "存有" + restype+"\n"

        else:
            ans += restype + "不存放在" + area + "\n" + restype + "存放在"
            for r in area_arr[:-1]:
                ans += r + ","
            ans += area_arr[-1] + "\n"

        return ans

    """
    查出国图是否有某种资源的
    """

    def solve_restype_library(self, entity):
        ans = ""
        entity['area'] = ['总馆北区']
        temp = self.solve_restype_area(entity)
        ans += temp.split("\n")[0]
        if '不' in temp.split("\n")[1]:
            pass
        else:
            ans += temp.split("\n")[1]
            return ans

        entity['area'] = ['总馆南区']
        temp = self.solve_restype_area(entity)
        if '不' in temp.split("\n")[1]:
            pass
        else:
            ans += temp.split("\n")[1]
            return ans

        entity['area'] = ['文津楼']
        temp = self.solve_restype_area(entity)
        if '不' in temp.split("\n")[1]:
            pass
        else:
            ans += temp.split("\n")[1]
            return ans

        entity['area'] = ['临琼楼']
        temp = self.solve_restype_area(entity)
        if '不' in temp.split("\n")[1]:
            pass
        else:
            ans += temp.split("\n")[1]
            return ans

        return ans


    """
    查出馆区是否有某种资源的（中级）
    """

    def solve_multype_area(self, entity):

        area = entity['area'][0]
        multype = entity['multype'][0]
        restype_res = Neo4jPrepare.get_reverse_relation(multype, '资源类型')

        restype_arr_orgin = [x['office_name'] for x in restype_res]
        restype_arr = restype_arr_orgin
        ans = multype+"包括"

        for restype in restype_arr[:-1]:

            ans+=restype+","

        ans += restype_arr[-1]+"\n"
        yes_restype = []
        for restype in restype_arr:
            res = Neo4jPrepare.get_relation_triple(restype, '馆区')
            area_arr = [x['office_name'] for x in res]
            if area in area_arr:
                yes_restype.append(restype)
        if len(yes_restype)>0:

            ans += '其中'
            for r in yes_restype[:-1]:
                ans += r+","
            ans += yes_restype[-1]+"在"+area+"\n"
        return ans

    """
    查看某馆区时候有什么大类资源
    """
    def solve_ttype_area(self, entity):

        area = entity['area'][0]
        ttype = entity['ttype'][0]
        restype_res = Neo4jPrepare.get_reverse_relation(ttype, '资源类型')

        restype_arr_orgin = [x['office_name'] for x in restype_res]
        restype_arr = restype_arr_orgin
        ans = ttype+"包括"

        for restype in restype_arr[:-1]:

            ans+=restype+","

        ans += restype_arr[-1]+"\n"
        yes_restype = []
        for restype in restype_arr:
            res = Neo4jPrepare.get_relation_triple(restype, '馆区')
            area_arr = [x['office_name'] for x in res]
            if area in area_arr:
                yes_restype.append(restype)
        if len(yes_restype)>0:

            ans += '其中'
            for r in yes_restype[:-1]:
                ans += r+","
            ans += yes_restype[-1]+"在"+area+"\n"
        else:
            ans += area + "没有" + ttype+"\n"
        return ans

    """
    查看国图有么有某中类
    """

    def solve_multype_library(self, entity):

        ans = ""
        entity['area'] = ['总馆北区']
        ans += self.solve_multype_area(entity)
        entity['area'] = ['总馆南区']
        temp = self.solve_multype_area(entity)
        temp = temp.split("\n")[1]
        ans += temp+"\n"
        entity['area'] = ['文津楼']
        temp = self.solve_multype_area(entity)
        temp = temp.split("\n")[1]
        ans += temp+"\n"
        entity['area'] = ['临琼楼']
        temp = self.solve_multype_area(entity)
        temp = temp.split("\n")[1]
        ans += temp
        return ans

    """
    查看国图有么有某中类
    """
    def solve_ttype_library(self, entity):

        ans = ""
        entity['area'] = ['总馆北区']
        ans += self.solve_ttype_area(entity)
        entity['area'] = ['总馆南区']
        temp = self.solve_ttype_area(entity)
        temp = temp.split("\n")[1]
        ans += temp+"\n"
        entity['area'] = ['文津楼']
        temp = self.solve_ttype_area(entity)
        temp = temp.split("\n")[1]
        ans += temp+"\n"
        entity['area'] = ['临琼楼']
        temp = self.solve_ttype_area(entity)
        temp = temp.split("\n")[1]
        ans += temp
        return ans

    """
    查看国图有么有某中类
    """

    def solve_res_library(self, entity):

        res = entity['res'][0]
        ans = GraphBaseConfig['place']+"的"+res+",存放在"
        room = Neo4jPrepare.get_relation(res,'馆室')
        room_arr = [x['office_name'] for x in room]
        for room_name in room_arr[:-1]:
            ans += room_name+","
        ans += room_arr[-1]+"\n"
        return ans

    def solve_goods_library(self, entity):

        goods = entity['goods'][0]
        ans = GraphBaseConfig['place']+"有"+goods+",存放在"
        room = Neo4jPrepare.get_relation(goods,'馆室')
        room_arr = [x['office_name'] for x in room]
        for room_name in room_arr[:-1]:
            ans += room_name+","
        ans += room_arr[-1]+"\n"
        return ans
    """
    查出馆室是否有某种资源的（中级）
    """

    def solve_multype_room(self, entity):

        room = entity['room'][0]
        multype = entity['multype'][0]
        restype_search = Neo4jPrepare.get_reverse_relation(multype, '资源类型')
        restype_arr = [x['office_name'] for x in restype_search]
        ans = "\n"
        if len(restype_arr) > 0:
            ans += multype + "包括"
        else:
            return "很抱歉，没有" + multype + "的具体信息\n"
        for restype in restype_arr[:-1]:
            ans += restype + ","
        ans += restype_arr[-1] + "\n"
        #print("===",restype_arr)
        for restype in restype_arr:
            #print(restype)
            res = Neo4jPrepare.get_relation_mul(restype, '馆室')
            #print(res)

            room_arr = [r['office_name'] for r in res]
            #print(room_arr)

            if room in room_arr:
                ans += room + "存有" + restype
                return ans

        ans += multype + "不存放在" + room + "\n"
        return ans

    """
    处理馆室所有资源的问题
    """
    def solve_room_res_a(self, entity):
        room = entity['room'][0]
        room_name = room
        if room.find(u"_")!=-1:
            room_name = room.split("_")[2]
        res = Neo4jPrepare.get_reverse_relation(room,'资源')
        res_dict = {}
        for r in res:
            res_dict[r['belong']]=[]
        res_type = list(res_dict.keys())
        #print(res_type)
        if res_type == []:
            return room_name+"不存放任何资源\n"
        ans = "\n"
        ans += room_name + "存放的资源类型包括："
        for t in res_type[:-1]:
            ans += t+","
        ans += res_type[-1]+"\n"

        for r in res:
            res_dict[r['belong']].append(r['office_name'])
        for t in res_type:
            ans += t+"："
            for r in res_dict[t][:-1]:
                ans += r+","
            ans += res_dict[t][-1] +"\n"
        return ans

    """
    资源数量问题
    """

    def solve_count_res(self, entity):
        resource = entity['res'][0]
        res = Neo4jPrepare.get_property(resource)
        ans = "\n"+resource+"存放在"
        room = Neo4jPrepare.get_relation(resource,'馆室')
        room_arr = [x['office_name'] for x in room]
        #print(room)

        for room_name in room_arr[:-1]:
            ans += room_name + ","
        ans += room_arr[-1] + "\n"

        if res['count']!='nan':
            ans += resource+"的数量是:"+str(res['count'])+"本（份）\n"
        else:
            ans += "很抱歉，"+resource+"暂时没有数据信息\n"
        return ans

    """
    某一类资源数量问题
    """
    def solve_count_restype(self, entity):
        restype = entity['restype'][0]
        #res = Neo4jPrepare.get_property(restype)
        ans = "\n"
        type = Neo4jPrepare.get_property(restype)

        if type['count'] != 'nan':
            ans += restype+"的数量是:"+str(int(float(type['count'])))+"本（份）\n"
        else:
            ans += "很抱歉，"+restype+"暂时没有数据信息\n"
        return ans

    def solve_count_multype(self, entity):
        multype = entity['multype'][0]
        restype_search = Neo4jPrepare.get_reverse_relation(multype, '资源类型')
        restype_arr = [x['office_name'] for x in restype_search]
        ans = "\n"
        if len(restype_arr) > 0:
            ans += multype + "包括"
        else:
            return "很抱歉，没有" + multype + "的具体信息\n"
        for restype in restype_arr[:-1]:
            ans += restype + ","
        ans += restype_arr[-1] + "\n"
        for restype in restype_arr:
            entity['restype'] = [restype]
            ans += self.solve_count_restype(entity)[1:]
        return ans

    """
    某资源是否是某类资源问题
    """
    def solve_res_res_h(self, entity):
        restype = entity['restype'][0]
        resource = entity['res'][0]
        res_arr = []
        res = Neo4jPrepare.get_reverse_relation(restype,'资源')
        ans = "\n"
        for r in res[:-1]:
            res_arr.append(r['office_name'])
        if resource in res_arr:

            ans += "是的,"+resource + "属于"+restype+"\n"
        else:
            ans += "很抱歉," + resource + "不属于" + restype + "\n"
        return ans

    """
    某资源是否是某类资源问题
    """

    def solve_mul_res_h(self, entity):
        restype = entity['restype'][0]
        multype = entity['multype'][0]
        res_arr = []
        res = Neo4jPrepare.get_reverse_relation(multype, '资源类型')
        ans = "\n"
        for r in res[:-1]:
            res_arr.append(r['office_name'])
        if restype in res_arr:

            ans += "是的," + restype + "属于" + multype + "\n"
        else:
            ans += "很抱歉," + restype + "不属于" + multype + "\n"
        return ans

    """
    某类资源包含的所有资源
    """
    def solve_res_res_a(self, entity):
        restype = entity['restype'][0]
        res = Neo4jPrepare.get_reverse_relation(restype,'资源')
        if len(res)<=0:
            return "很抱歉，暂时没有"+restype+"下属资源的信息\n"
        ans = "\n"+restype+"包含的资源有：\n"
        for r in res[:-1]:
            ans += r['office_name']+","
        ans += res[-1]['office_name'] + "\n"
        return ans

    """
    某类资源包含的所有资源
    """

    def solve_mul_res_a(self, entity):
        multype = entity['multype'][0]
        res = Neo4jPrepare.get_reverse_relation(multype, '资源类型')
        ans = "\n" + multype + "包含的资源有:"
        for r in res[:-1]:
            ans += r['office_name'] + ","
        ans += res[-1]['office_name'] + "\n"
        return ans


    """
    资源类型（资源的中级类别）属于哪一大类问题（资源的最高类别）
    """
    def solve_res_res_t(self, entity):
        restype = entity['restype'][0]
        res = Neo4jPrepare.get_property(restype)
        ans = "\n"+restype+"属于"+res['belong']
        return ans

    """
    馆室有几楼的
    """
    def solve_count_floor(self, entity):
        area = entity['area'][0]
        res = Neo4jPrepare.get_reverse_relation(area,'楼层')
        #print(res)
        l = len(res)
        ans = "\n"+area+"一共有"+str(l)+"层\n"
        return ans

    """
    国图有几个馆区
    """
    def solve_library_area(self):
        res = Neo4jPrepare.get_relation(GraphBaseConfig['place'],"馆区")
        print(res)
        ans = "\n"+GraphBaseConfig['place']+"包括"
        for r in res[:-1]:
            ans += r['office_name']+","
        ans += res[-1]['office_name']+"\n"
        return ans

    """
    国图包含哪些资源类型，查出所有的资源类别
    """

    def solve_library_res_a(self):
        area = Neo4jPrepare.get_entity("馆区")
        area_arr = [sub_area['office_name'] for sub_area in area]
        ans = GraphBaseConfig['place']+"各个馆舍在资源和服务方面各有侧重。\n"

        for sub_area in area_arr:
            resource_arr = Neo4jPrepare.get_area_resource_type(sub_area)
            if len(resource_arr)>0:
                ans += sub_area+": "
                for r in resource_arr[:-1]:
                    #print(r)
                    ans += r['office_name']+","
                ans += resource_arr[-1]['office_name']+"\n"
        return ans
    """
    国图是否提供某一服务
    """

    def solve_service_exit(self, entity):
        # print(entity)
        service = entity['service']
        # res = Neo4jPrepare.get_property(service)
        ans = "\n"
        if len(service) > 0:
            ans += GraphBaseConfig['place']+"提供" + service[0] + "\n"
            #print("aaa",ans)
            room = Neo4jPrepare.get_relation(service[0], "馆室")
            if len(room)<=0:
                return ans
            ans += "您可以去"
            for r in room[:-1]:
                ans += r['office_name'] + ","
            ans += room[-1]['office_name'] + "接受该服务\n"
        else:
            ans += "很抱歉，"+GraphBaseConfig['place']+"不提供该服务"
        return ans

    """
    国图是否提供某一业务
    """

    def solve_task_exit(self, entity):
        # print(entity)
        service = entity['task']
        # res = Neo4jPrepare.get_property(service)
        ans = "\n"
        if len(service) > 0:
            ans += GraphBaseConfig['place']+"提供" + service[0] + "\n"
            # print("aaa",ans)
            room = Neo4jPrepare.get_relation(service[0], "馆室")
            if len(room) <= 0:
                return ans
            ans += "您可以去"
            for r in room[:-1]:
                ans += r['office_name'] + ","
            ans += room[-1]['office_name'] + "办理该业务\n"
        else:
            ans += "很抱歉，"+GraphBaseConfig['place']+"不能办理该业务"
        return ans

    """
    国图提供什么服务
    """

    def solve_service_exit_all(self):

        res = Neo4jPrepare.get_entity('服务')
        ans = "\n"+GraphBaseConfig['place']+"提供的服务包括"
        for sub_result in res[:-1]:
            ans += sub_result['office_name']+","
        ans += res[-1]['office_name']+"\n"
        return ans

    def solve_service_area_all(self,entity):

        area = entity['area'][0]
        res = Neo4jPrepare.get_reverse_relation_mul(area, '服务')
        ans = "\n"
        if len(res) > 0:
            ans += area + "提供的服务包括"
            for r in res[:-1]:
                ans += r['office_name'] + ","
            ans += res[-1]['office_name'] + "\n"
        else:
            ans += area + "不提供任何服务\n"
        return ans


    """
    查出国图资源分布，即查出国图所有馆区所包含的资源
    """
    def solve_library_res(self):
        res = Neo4jPrepare.get_relation(GraphBaseConfig['place'],"馆区")
        ans = ""
        for r in res:
            area_dict = {'area':[r['office_name']]}
            ans += self.solve_area_res_a(area_dict)
        return ans

    """"
    馆区包含什么资源类型
    """
    def solve_area_res_a(self,entity):
        area = entity['area'][0]
        res = Neo4jPrepare.get_reverse_relation(area, '馆室')
        resource_arr = []
        for r in res:
            res_arr = Neo4jPrepare.get_reverse_relation(r['office_name'], '资源')
            for sub_r in res_arr:
                resource_arr.append(sub_r['belong'])

        resource_arr = np.unique(resource_arr)

        ans = "\n"
        ans += area + "存放有"
        for sub_r in resource_arr[:-1]:
            ans += sub_r + ","
        ans += resource_arr[-1] + "等类型的资源\n"
        return ans

    """
    馆室有什么服务
    """
    def solve_service_room_all(self,entity):
        room = entity['room'][0]
        res = Neo4jPrepare.get_reverse_relation(room, '服务')
        ans = "\n"
        if len(res)>0:
            ans += room+"提供的服务包括"
            for r in res[:-1]:
                ans+=r['office_name']+","
            ans += res[-1]['office_name']+"\n"
        else:
            ans += room+"不提供任何服务\n"
        return ans

    """
    馆室有没有某一服务
    """

    def solve_service_room_exit(self, entity):
        room = entity['room'][0]
        service = entity['service'][0]
        res = Neo4jPrepare.get_reverse_relation(room, '服务')
        ans = "\n"
        for r in res:
            if r['office_name'] == service:
                ans += room + "提供"+service+"\n"
                return ans

        ans += room + "不提供"+service+"\n"
        return ans

    """
    馆室有没有某一服务
    """

    def solve_service_area_exit(self, entity):
        area = entity['area'][0]
        service = entity['service'][0]
        res = Neo4jPrepare.get_reverse_relation_mul(area, '服务')
        ans = "\n"
        for r in res:
            if r['office_name'] == service:
                ans += area + "提供" + service + "\n"
                return ans

        ans += area + "不提供" + service + "\n"
        return ans

    """
    开架阅览室有哪些
    """

    def solve_open_room(self):
        res = Neo4jPrepare.get_entity('馆室')
        room_arr = []
        for r in res:
            if r['open'] == '1':
                room_arr.append(r['office_name'])
        ans = "\n开架阅览室包括"
        for sub_room in room_arr[:-1]:
            ans += sub_room + ","
        ans += room_arr[-1] + "\n"
        return ans
