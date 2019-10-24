# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.config.base_config import GraphBaseConfig
from model.kb_prepare.neo4j_prepare import Neo4jPrepare
import time
import matplotlib.pyplot as plt
#from skimage import io
import numpy as np

class neo4jBot():
    """
    对应问题模式在知识图谱中查找答案
    目前包括馆室位置，馆室开放日，馆室开放时间，馆室联系方式，资源馆室
    """

    @classmethod
    def task_response(cls, task, entity_dict):
        """
        响应hub指派的回答任务，也就是对graphQA类的问题分intent处理
        :param task:
        :return:
        """

        answer = "GraphQA 什么也没说！"
        if task == 'task_res_pos':
            answer = cls.answer_res_pos(entity_dict)
        elif task == 'task_room_pos':
            answer = cls.answer_room_pos(entity_dict)
        elif task == 'task_room_res':
            answer = cls.answer_room_res_a(entity_dict)

        return answer


    @classmethod
    def form_answern(self,cursor):
        mark_list=[]
        dis_list=[]
        x_list=[]
        y_list=[]
        dir_list=[]
        while cursor.forward():

            record = cursor.current()
            #print(record['x_list'])
            res1 = dict(record['b'])
            mark_list.append(res1)
            res2 = dict(record['r'])
            dis_list.append(res2['dis'])
            dir_list.append(res2['dir'])
            #print("?",record['x_list'])

            if record['x_list'].find("；")!=-1:
                x_list=record['x_list'].split("；")
                y_list=record['y_list'].split("；")
            else :
                x_list=record['x_list']
                y_list = record['y_list']

        #print("??", mark_list, dis_list, x_list, y_list)
        return mark_list,dis_list,x_list,y_list,dir_list

    @classmethod
    def form_answern_list(self,cursor):
        path_list=[]
        dis_list=[]
        while cursor.forward():
            record = cursor.current()
            path_list = record['p']
            #print("?",path_list,record['p'])
            dis_dir_list = record['r']
            #print("dis_list",dis_dir_list)

        return path_list,dis_dir_list

    @classmethod
    def draw_pic_1(cls,x,y,dx,dy):
        x=432
        y=543
        dx='336'
        dy='251'
        nx='432，336'
        ny='411，411'
        #x = int(float(rdfPrepare.rdf_query_navi_propertiy_pic(machine, 'pro_sx', graph)[0]))
        #y = int(float(rdfPrepare.rdf_query_navi_propertiy_pic(machine, 'pro_sy', graph)[0]))
        #dx = rdfPrepare.rdf_query_navi_propertiy_pic(machine, 'pro_x', graph)
        #dy = rdfPrepare.rdf_query_navi_propertiy_pic(machine, 'pro_y', graph)
        img = None
        img = io.imread('../data/1.png')
        # io.imshow(img)

        # print(int(dy[final_des_index]))
        # plt.plot([x, int(dx[final_des_index])], [y, int(dy[final_des_index])])
        '''
        if dx.find('，') != -1:
            arrx = dx.split('，')
            mindx = min(int(arrx[0]), int(arrx[1]))
            maxdx = max(int(arrx[0]), int(arrx[1]))
            arry = dy.split('，')
            mindy = min(int(arry[0]), int(arry[1]))
            maxdy = max(int(arry[0]), int(arry[1]))
            sy = min(min(mindy, int(ny)), y)
            sx = min(min(mindx, int(nx)), x)
            ey = max(max(maxdy, int(ny)), y)
            ex = max(max(maxdx, int(nx)), x)
        else:
            sy = min(min(int(dy), int(ny)), y)
            sx = min(min(int(dx), int(nx)), x)
            ey = max(max(int(dy), int(ny)), y)
            ex = max(max(int(dx), int(nx)), x)
        '''
        if nx.find('，') != -1:
            arrx = nx.split('，')
            mindx = min(int(arrx[0]), int(arrx[1]))
            maxdx = max(int(arrx[0]), int(arrx[1]))
            arry = ny.split('，')
            mindy = min(int(arry[0]), int(arry[1]))
            maxdy = max(int(arry[0]), int(arry[1]))
            sy = min(min(mindy, int(dy)), y)
            sx = min(min(mindx, int(dx)), x)
            ey = max(max(maxdy, int(dy)), y)
            ex = max(max(maxdx, int(dx)), x)
        else:
            sy = min(min(int(dy), int(ny)), y)
            sx = min(min(int(dx), int(nx)), x)
            ey = max(max(int(dy), int(ny)), y)
            ex = max(max(int(dx), int(nx)), x)
        if sx - 100 >= 0:
            left = sx - 100
        else:
            left = 0
        if sy - 100 >= 0:
            up = sy - 100
        else:
            up = 0
        if ex + 100 <= img.shape[1]:
            right = ex + 100
        else:
            right = img.shape[1]
        if ey + 100 <= img.shape[0]:
            down = ey + 100
        else:
            down = img.shape[0]
        # print(x,ex,left,right)
        print(up,down,left,right)
        print(img.shape,img.shape[0],img.shape[1])
        img = img[up:down, left:right]
        io.imshow(img)
        # plt.axis('off')
        plt.figure()
        plt.axis('off')

        if nx.find('，') != -1:
            arrx = nx.split('，')
            arry = ny.split('，')


            plt.plot([x - left, int(arrx[0]) - left, int(arrx[1]) - left, int(dx) - left],
                     [y - up, int(arry[0]) - up, int(arry[1]) - up, int(dy) - up])
        else:

            plt.plot([x - left, int(nx) - left, int(dx) - left],
                     [y - up, int(ny) - up, int(dy) - up])
        io.imshow(img)
        plt.savefig('../../resource/2.png')
        return

    @classmethod
    def draw_pic(cls,x,y):

        img = None
        img = io.imread('../../resource/1.png')
        print(x,y)
        x = np.array(x,dtype='int')
        y = np.array(y,dtype='int')
        sy = y.min()
        sx = x.min()
        ey = y.max()
        ex = x.max()
        if sx - 100 >= 0:
            left = sx - 100
        else:
            left = 0
        if sy - 100 >= 0:
            up = sy - 100
        else:
            up = 0
        if ex + 100 <= img.shape[1]:
            right = ex + 100
        else:
            right = img.shape[1]
        if ey + 100 <= img.shape[0]:
            down = ey + 100
        else:
            down = img.shape[0]
        #print(up,down,left,right)
        #print(img.shape,img.shape[0],img.shape[1])
        img = img[up:down, left:right]
        io.imshow(img)
        # plt.axis('off')
        plt.figure()
        plt.axis('off')
        dx=[]
        dy=[]
        for sub_x in x:
            temp = sub_x-left
            dx.append(temp)
        for sub_y in y:
            temp = sub_y-up
            dy.append(temp)
        plt.plot(dx,dy)
        io.imshow(img)
        plt.savefig('../../resource/2.png')
        return

    @classmethod
    def navi(cls,entity):
        responds = ''
        machine = '拐角'
        #desroom = 'A'
        desroom = entity
        ans_desroom = desroom
        if desroom.find("_")!= -1:
            arr = desroom.split("_")
            ans_desroom = arr[2]
        #print(desroom)
        cursor = Neo4jPrepare.graph.run("MATCH (a {office_name:{a}})-[r:相邻]->(b) return a.des_x as x_list ,a.des_y as y_list,b,r",a=desroom)
        destination_mark,dis_mark,x_list,y_list,dir_list = cls.form_answern(cursor)
        #print(destination_mark,dis_mark,x_list,y_list)

        des_name=[]
        for i in range(len(destination_mark)):
            des_name.append(destination_mark[i]['name'])

        if machine in des_name:
            m_index = des_name.index(machine)
            dx=[]
            dy=[]

            arr = destination_mark[m_index]['self_site'].split("；")


            dx.append(int(arr[0]))
            dy.append(int(arr[1]))
            f_x = x_list[len(x_list) - m_index - 1]
            f_y = y_list[len(y_list)-m_index-1]
            if f_x.find("，")!=-1:
                arr = f_x.split("，")
                for i in arr:
                    dx.append(int(i))
            else:

                dx.append(int(f_x))
            if f_y.find("，") != -1:
                arr = f_y.split("，")
                for i in arr:
                    dy.append(int(i))
            else:

                dy.append(int(f_y))
            dir = dir_list[m_index]
            #print(dir)
            if dis_mark[m_index].find("，")!=-1:
                arr = dis_mark[m_index].split("，")
                responds += '先向'+dir[0]+'走'+str(int(arr[0]))+"米\n"
                #print('先向'+dir[0]+'走'+str(int(arr[0]))+"米")
                for i in range(1,len(arr)):
                    responds += "接着向"+dir[i]+'走'+str(int(arr[i]))+"米\n"
                    #print("接着向"+dir[i]+'走'+str(int(arr[i]))+"米")
                #print("您就能找到")
                responds += "您就能找到"+desroom+"。\n"

            else:
                responds +="走" + str(int(dis_mark[m_index])) + "米您就能找到" + ans_desroom+"。\n"
                #print("走" + str(int(dis_mark[m_index])) + "米您就能找到" +desroom)
            cls.draw_pic(dx, dy)
            return responds;
        #print(des_name,dis_mark)
        min_path_list=[]
        min_dis_list=[]
        for sub in range(len(des_name)):
            min_path = 10
            min_index = 0
            a = time.time()
            cursor = Neo4jPrepare.graph.run("MATCH p=(a {office_name:{a}})-[r:互连*..5]->(b {office_name:{b}}) return nodes(p) as p,r,size(nodes(p)) as s order by s limit 1",
                                    a=machine, b=des_name[sub])
            b = time.time()
            #print(b - a)
            path_list,dis_list = cls.form_answern_list(cursor)

            min_path_list.append(path_list)
            min_dis_list.append(dis_list)

        final_index=0
        final_sum=1000000000000000

        for i in range(len(min_dis_list)):

            tmp_sum = int(dis_mark[i])
            for j in min_dis_list[i]:
                temp_sub = 0
                if dict(j)['dis'].find("，")!=-1:
                    arr = dict(j)['dis'].split("，")
                    for sub_arr in arr:
                        temp_sub += int(sub_arr)
                else:
                    temp_sub += int(dict(j)['dis'])
                tmp_sum += temp_sub
                #print(i,temp_sub,tmp_sum,final_sum)
            if tmp_sum<final_sum:
                final_index = i
                #print(final_index,"final")
                final_sum = tmp_sum

            #print(final_index)
        dx=[]
        dy=[]
        #print("min_path_list",min_path_list)

        #####################################################

        arr = min_path_list[final_index][0]['self_site'].split("；")
        #print(arr)
        dx.append(arr[0])
        dy.append(arr[1])

        #####################################################
        dir = min_dis_list[final_index]
        #print(dir,"dir")
        #dx.append(min_path_list[final_index])
        #print(min_path_list[final_index])
        if len(min_path_list)>1:
            for i in range(1,len(min_path_list[final_index])):
                dis = dict(min_dis_list[final_index][i-1])['dis']
                dir = min_dis_list[final_index][i-1]['dir']
                #print(dir)
                if dis.find("，")!= -1:
                    arr = dis.split("，")
                    responds += "先向" + dir[0]+"走" + arr[0]+"米\n"
                    #print("先向" + dir[0]+"走" + arr[0]+"米")
                    for arr_index in range(1,len(arr)):
                        responds += "接着先向" + dir[arr_index] + "走" + arr[arr_index] + "米到"+dict(min_path_list[final_index][i])['name']+"\n"
                        #print("接着先向" + dir[arr_index] + "走" + arr[arr_index] + "米到"+dict(min_path_list[final_index][i])['name'])
                else:
                    responds += "向"+min_dis_list[final_index][i-1]['dir']+"走"+str(int(dict(min_dis_list[final_index][i-1])['dis']))+"米到"+dict(min_path_list[final_index][i])['name']+"\n"

                    #print("向"+min_dis_list[final_index][i-1]['dir']+"走"+str(int(dict(min_dis_list[final_index][i-1])['dis']))+"米到"+dict(min_path_list[final_index][i])['name'])
                #####################################################

                if dict(min_dis_list[final_index][i-1])['x'] != '':
                    dx.append(int(dict(min_dis_list[final_index][i-1])['x']))
                    #print(dict(min_dis_list[final_index][i-1])['x'])

                    #print(dict(min_dis_list[final_index][i-1])['x'])
                if dict(min_dis_list[final_index][i-1])['y'] != '':
                    dy.append(dict(min_dis_list[final_index][i-1])['y'])

                site = dict(min_path_list[final_index][i])['self_site'].split("；")
                dx.append(site[0])
                dy.append(site[1])

                #####################################################
            des_index = des_name.index(dict(min_path_list[final_index][i])['name'])
            #print("qqq",modify_index,final_index)
            responds += "最后向"+dir_list[des_index]+"走"+str(int(dis_mark[des_index]))+"就能到"+ans_desroom+"\n"
            #print("最后向"+dir_list[des_index]+"走"+str(int(dis_mark[des_index]))+"就能到"+desroom)
            dx.append(x_list[1])
            dy.append(y_list[1])
        #print(dx,dy)
        #####################################################
        cls.draw_pic(dx,dy)
        #####################################################
        #print(dx,dy)
        return responds

    @classmethod
    def answer_room_res_a(cls, entity):
        response = ""
        e = ""
        if entity['room']:
            e = entity['room'][0]


        elif entity['floor']:
            e = entity['floor'][0]

        ans = Neo4jPrepare.get_reverse_relation_mul(e, '资源')
        if len(ans) == 0:
            return "未找到资源\n"
        response += e + "具有如下资源：\n"

        for i in ans:
            # print(i)
            response += i['office_name'] + "\n"

        return response

    @classmethod
    def answer_res_pos(cls,entity):
        response = "\n"
        res = entity['res'][0]
        ans = Neo4jPrepare.get_relation(res,'馆室')
        ans_room = ans[0]['office_name']
        if ans[0]['office_name'].find("_")!=-1:
            arr = ans[0]['office_name'].split("_")
            ans_room = arr[2]
        response += res + "存放于" + ans_room + "\n"
        #print(ans)
        response += cls.navi(ans[0]['office_name'])
        return response

    @classmethod
    def answer_room_pos(cls,entity):
        response = "\n您当前在总馆北区一层\n"
        room = entity['room'][0]
        #print(room)
        ans_room = room
        if room.find("_")!=-1:
            arr = room.split("_")
            ans_room = arr[2]
        area = Neo4jPrepare.get_relation(room,'馆区')

        #print(area)
        if area[0]['office_name'] != '总馆北区':
            response += ans_room+'在'+ area[0]['office_name'] + "，位于"+area[0]['position']+"\n"
            return response
        floor = Neo4jPrepare.get_relation(room,'楼层')

        #print(floor)
        if floor[0]['office_name'] != '总馆北区一层':
            response += ans_room+'在'+ floor[0]['office_name']+", 直走340米您就能找到最近的电梯。\n"
            return response

        response += cls.navi(room)
        return response














