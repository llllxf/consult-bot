# -*- coding: utf-8 -*-
"""
时间类问答模块
作者:lxf
"""
from model.kb_prepare.neo4j_prepare2 import Neo4jPrepare

class Task_time2():
    """
    馆室开放时间
    """
    def solve_room_time(self,entity):
        room = entity['room'][0]
        res = Neo4jPrepare.get_property(room)
        #print(res)
        open_day = res['open_date']
        ans = "\n"
        if open_day != 'nan':
            ans += room + "开放日为：" + open_day+"\n"
        workday_time = res['work_open']
        weekend_time = res['week_open']
        if workday_time != 'nan':

            ans += "工作日开放时间为："+workday_time+"\n"
        if weekend_time != 'nan':
            ans += "周末开放时间为："+weekend_time+"\n"
        if ans == "\n":
            ans += "很抱歉，没有"+room+"的时间信息\n"

        return ans
    """
    馆室的资源借阅时间
    """
    def solve_room_res_time(self,entity):
        room = entity['room'][0]
        #print(entity)
        res = Neo4jPrepare.get_property(room)
        #print("================================",res)
        workday_time = res['work_borrow']
        weekend_time = res['week_borrow']
        if workday_time == 'nan' and weekend_time == 'nan':
            return "很抱歉，"+room+"的资源材料不提供借阅\n"
        ans = "\n"+room+"的书籍材料借阅时间为："
        if workday_time != 'nan':
            ans += "\n工作日："+workday_time
        if weekend_time != 'nan':
            ans += "\n周未：" + weekend_time
        return ans+"\n"

    """
    资源借阅时间
    """
    def solve_res_time(self,entity):
        resource = entity['res'][0]
        #print(Neo4jPrepare.get_property(resource))
        room = Neo4jPrepare.get_property(resource)['room']
        res = Neo4jPrepare.get_property(room)
        workday_time = res['work_borrow']
        weekend_time = res['week_borrow']
        if workday_time == 'nan' and weekend_time == 'nan':
            return "很抱歉，"+room+"的资源材料不提供借阅\n"
        #ans = "\n" + resource + "的借阅时间为：\n工作日：" + workday_time + "\n周未：" + weekend_time + "\n"
        ans = "\n" + resource + "存放在"+room+","
        ans += room + "的借阅时间为："
        if workday_time != 'nan':
            ans += "\n工作日：" + workday_time
        if weekend_time != 'nan':
            ans += "\n周未：" + weekend_time
        return ans + "\n"

    """
    服务时间
    """
    def solve_service_time(self,entity):
        service = entity['service'][0]
        res = Neo4jPrepare.get_property(service)
        ans = "\n"
        if res['date']!='nan':
            ans += "服务日期："+res['date']+"\n"
        if res['worktime'] != 'nan':
            ans += "工作日服务时间为"+str(res['worktime'])+"\n"
        if res['weektime'] != 'nan':
            ans += "工作日服务时间为"+str(res['weektime'])+"\n"
        return ans

    """
    国家图书馆开放时间
    """
    def solve_library_time(self,entity):
        library = entity['library'][0]
        res = Neo4jPrepare.get_relation(library,'馆区')
        #print(res)
        ans = "\n"
        ans += library+"包括"+str(len(res))+"个馆区\n"
        for r in res:
            ans += r['office_name']+"开放日期为"+r['date']+"\n"
            ans += "工作开放时间为"+r['worktime']+"\n"
            ans += "周末开放时间为"+r['weektime']+"\n"
        return ans



    """
    馆区开放时间
    """
    def solve_area_time(self, entity):
        area = entity['area'][0]
        res = Neo4jPrepare.get_property(area)
        #print(res)
        ans = "\n"
        if res['date']!='nan':
            ans += area+"开放日期为"+res['date']+"\n"
        if res['worktime']!='nan':
            ans += "工作日开放时间为"+res['worktime']+"\n"
        if res['weektime']!='nan':
            ans += "周末开放是时间为"+res['weektime']+"\n"
        return ans
