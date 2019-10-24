# -*- coding: utf-8 -*-
from model.kb_prepare.neo4j_prepare2 import Neo4jPrepare

class Task_condition():
    def solve_room_card_a(self, entity):
        room = entity['room'][0]
        res = Neo4jPrepare.get_property(room)
        ans = "\n"
        if res['card'] != '':
            ans += "进"+room+"需要满足的条件为：\n"
            if res['card'].find(u"，") != -1:
                card_arr = res['card'].split("，")
                for card in card_arr:
                    card_res = Neo4jPrepare.get_property(card)
                    ans += "年龄"+card_res['age']+"的读者可以持"+card_res['office_name'] + "进入"+room+"\n"
            else :
                card_res = Neo4jPrepare.get_property(res['card'])
                ans += "年龄" + card_res['age'] + "的读者可以持" + card_res['office_name'] + "进入" + room + "\n"
        else:
            ans += "进入该馆室无需证件\n"
        return ans












