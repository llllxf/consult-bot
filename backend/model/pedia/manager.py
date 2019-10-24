# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
print("manager",project_path)
sys.path.append(project_path)
import requests, json
from model.nlp import NLPUtil


class TaskManager(object):
    NLPUtil("ltp_data_v3.4.0")
    """
    给模版匹配对应的函数
    """
    @classmethod
    def task_response(cls, task, words, arcs_dict,postags,hed_index):
        answer = ""
        if task == 'task_SBV_ATT_POB':
            answer = cls.answer_SBV_ATT_POB(words, arcs_dict,postags,hed_index)
        if task == 'task_HED':
            answer = cls.answer_HED(words, arcs_dict,postags,hed_index)
        if task == 'task_SBV':
            answer = cls.answer_SBV(words, arcs_dict,postags,hed_index)
        if task == 'task_ATT_HED':
            answer = cls.answer_ATT_HED(words, arcs_dict,postags,hed_index)
        if task == 'task_SBV_VOB':
            answer = cls.answer_SBV_VOB(words, arcs_dict,postags,hed_index)
        if task == 'task_SBV_POB':
            answer = cls.answer_SBV_POB(words, arcs_dict,postags,hed_index)
        if task == 'task_SBV_ATT_VOB':
            answer = cls.answer_SBV_ATT_VOB(words, arcs_dict,postags,hed_index)
        """
        if task == 'task_SBV_ADV':#未实现
            answer = cls.answer_SBV_ADV(words, arcs_dict,postags,hed_index)
        if task == 'task_SBV_VOB_COO':#未实现
            answer = cls.answer_SBV_VOB_COO(words, arcs_dict,postags,hed_index)
        """
        if task == 'task_ATT_SBV_POB':
            answer = cls.answer_ATT_SBV_POB(words, arcs_dict,postags,hed_index)
        if task == 'task_ATT_SBV_VOB':
            answer = cls.answer_ATT_SBV_VOB(words, arcs_dict,postags,hed_index)
        if task == 'task_ATT_ADV_VOB':
            answer = cls.answer_ATT_ADV_VOB(words, arcs_dict, postags, hed_index)
        if task == 'task_SBV_HED_SBV_VOB':
            answer = cls.answer_SBV_HED_SBV_VOB(words, arcs_dict, postags, hed_index)
        """
        if task == 'task_ADV_SBV_HED':
            answer = cls.answer_ADV_SBV_HED(words, arcs_dict, postags, hed_index)
        """
        """
        if task == 'task_ADV_HED_DBL_VOB':
            answer = cls.answer_ADV_HED_DBL_VOB(words, arcs_dict, postags, hed_index)
        """
        """
        if task == 'task_ADV_SBV_ADV_HED':
            answer = cls.answer_ADV_SBV_ADV_HED(words, arcs_dict, postags, hed_index)
        """
        """
        if task == 'task_SBV_ADV_HED':
            answer = cls.answer_SBV_ADV_HED(words, arcs_dict, postags, hed_index)
        """
        return answer

    """
    @classmethod
    def answer_SBV_ADV(cls,words, arcs_dict,postags,hed_index):
        return None

    @classmethod
    def answer_SBV_VOB_COO(cls,words, arcs_dict,postags,hed_index):
        return None
    """


    """
    SBVHEDADVVOBRAD
    希特勒是怎么死的
    """

    """
    提取出主语，状语和核心词汇（主语状态）
    eg.恐龙会灭绝吗
    """
    """
    @classmethod
    def answer_SBV_ADV_HED(cls, words, arcs_dict, postags, hed_index):
        hed = words[hed_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]

        subj = words[subj_index]
        if subj in ['你','你们','我们','我']:
            return None
        if 'ADV' not in arcs_dict[hed_index].keys():
            return None
        adv_idnex = arcs_dict[hed_index]['ADV'][0]
        adv = words[adv_idnex]

        return cls.get_judge(subj,adv,hed)
    """

    """
    问句提取出状语（疑问代词），主语以及第二状语（表达状态）和核心词汇（主语的状态）
    eg.为什么恐龙会灭绝
    """
    """
    @classmethod
    def answer_ADV_SBV_ADV_HED(cls, words, arcs_dict, postags, hed_index):
        pass
    """

    """
    问句提取出状语（疑问代词），主语以及核心词汇（动词）和兼语（动词第一对象）宾语（动词第二对象）
    eg.怎么使恐龙灭绝
    """
    """
    @classmethod
    def answer_ADV_HED_DBL_VOB(cls, words, arcs_dict, postags, hed_index):
        pass
    """

    """
    问句提取出状语，主语和核心词汇
    问句的含义是问询主语与核心词汇之间的关系
    eg.为什么恐龙灭绝了
    """
    """
    @classmethod
    def answer_ADV_SBV_HED(cls,words, arcs_dict, postags, hed_index):
        pass
    """

    """
    提取出问句的第一主语和第二主语，以及他们之间的关系（VOB）
    问句的含义是问询第二主语
    eg.红豆是谁唱的
    
    存在的问题：分词问题
    
    """
    @classmethod
    def answer_SBV_HED_SBV_VOB(cls,words, arcs_dict, postags, hed_index):
        hed = words[hed_index]

        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        sbv_index = arcs_dict[hed_index]['SBV'][0]
        sbv = words[sbv_index]
        if 'VOB' not in arcs_dict[hed_index].keys():
            return None
        vob_index = arcs_dict[hed_index]['VOB'][0]
        vob = words[vob_index]
        if 'SBV' not in arcs_dict[vob_index].keys():
            return None
        subj_index = arcs_dict[vob_index]['SBV'][0]
        subj = words[subj_index]

        if sbv in ['你','你们','我们','我'] or subj in ['你','你们','我们','我']:
            return None
        if subj == '谁':
            ans = cls.get_attr(sbv,"者")
            if ans == None:
                ans = cls.get_attr(sbv,"手")
                if ans == None:
                    ans = cls.get_desc(sbv)
                    return ans
                else:
                    return ans
            else:
                return ans
        else:
            ans = cls.get_attr(sbv,vob)
            if ans == None:
                ans = cls.get_desc(sbv)
                return ans
            else:
                return ans
        return ans



    """
    问句仅提取出代词，主语，动宾
    询问代词的主语属性
    eg.中国的首都是什么
    eg.美丽的首都是什么
    """
    @classmethod
    def answer_ATT_SBV_VOB(cls, words, arcs_dict, postags, hed_index):
        verb = words[hed_index]
        if 'VOB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['VOB'][0]
        obj = words[obj_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]
        subj = words[subj_index]
        if 'ATT' not in arcs_dict[subj_index].keys():
            return None
        att_index = arcs_dict[subj_index]['ATT'][0]
        att = words[att_index]

        if subj in ['你','你们','我们','我']:
            return None
        if postags[att_index] in NLPUtil.noun_for_pedia:
            #print("===============1")
            ans = cls.get_attr(att,subj)
            print(att)
            #print(ans)
            if ans == None:
                print(subj)
                ans = cls.get_desc(att)
                return ans
            else:
                return ans
        else:
            return cls.get_desc(subj)

    """
    问句仅提取出代词，主语，动宾
    询问代词的主语属性
    eg.世界上有什么**
    """

    @classmethod
    def answer_ATT_ADV_VOB(cls, words, arcs_dict, postags, hed_index):
        verb = words[hed_index]
        if 'VOB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['VOB'][0]
        obj = words[obj_index]
        if 'ADV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['ADV'][0]
        subj = words[subj_index]
        if 'ATT' not in arcs_dict[subj_index].keys():
            return None
        att_index = arcs_dict[subj_index]['ATT'][0]
        att = words[att_index]
        return cls.get_desc(obj)

    """
    问句仅提取出代词，主语，介宾
    询问代词的主语属性
    eg.暂时没有想到
    """

    @classmethod
    def answer_ATT_SBV_POB(cls, words, arcs_dict, postags, hed_index):
        prep = words[hed_index]
        if 'POB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['POB'][0]
        obj = words[obj_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]
        subj = words[subj_index]
        if 'ATT' not in arcs_dict[subj_index].keys():
            return None
        att_index = arcs_dict[subj_index]['ATT'][0]
        att = words[att_index]
        if subj in ['你', '你们', '我们', '我'] or obj in ['你', '你们', '我们', '我']:
            return None

        if postags[att_index] in ['n', 'nh', 'ni', 'nl', 'ns', 'nz', 'nt', 'i']:
            ans = cls.get_attr(att,subj)
            if ans == None:
                ans = cls.get_desc(att)
                return ans
            else:
                return ans
        else:
            return cls.get_desc(subj)

    """
    问句仅提取出核心词汇，以及该核心词的修饰词
    问句的意图:
    1.当ATT为名词性词汇时询问的是att的核心词汇属性
    eg.中国的首都
    2.当ATT非名词性时，询问的是核心词汇的介绍
    eg.美丽的中国
    """

    @classmethod
    def answer_ATT_HED(cls, words, arcs_dict, postags, hed_index):

        word = words[hed_index]

        if 'ATT' not in arcs_dict[hed_index].keys():
            return None
        att_index = arcs_dict[hed_index]['ATT'][0]

        att = words[att_index]
        if word in ['你','你们','我们','我']:
            return None
        if postags[att_index] in NLPUtil.noun_for_pedia:
            ans = cls.get_attr(att,word)
            if ans == None:
                ans = cls.get_desc(word)
                return ans
            else:
                return ans
        else:
            ans =  cls.get_desc(word)
        """
        if ans == None:
            ans = "很抱歉，暂时没有办法回答相关问题\n"
        """
        return ans

    """
    问句仅提取出核心词汇
    问句的意图为介绍核心词汇
    eg.中国
    """
    @classmethod
    def answer_HED(cls, words, arcs_dict, postags, hed_index):
        word = words[hed_index]
        if postags[hed_index] in NLPUtil.noun_for_pedia:

            return cls.get_desc(word)
        return None


    """
    解释存在的名词主语成分
    """

    @classmethod
    def answer_SBV(cls, words, arcs_dict, postags, hed_index):
        print(arcs_dict,hed_index)
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV']
        for sub_index in subj_index:
            word = words[sub_index]
            print(word,postags[sub_index])
            if postags[sub_index] in NLPUtil.noun_for_pedia:
                return cls.get_desc(word)
        return None

    """
    问句提取出主语、谓语和宾语
    
    1.宾语词性为疑问代词->介绍主语
    eg.iphone是什么
    2.宾语是名词性词汇->确定主语是否有宾语这一属性
    eg.五星红旗是国旗吗
    """
    @classmethod
    def answer_SBV_VOB(cls, words, arcs_dict, postags, hed_index):
        verb = words[hed_index]
        if 'VOB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['VOB'][0]
        obj = words[obj_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]
        subj = words[subj_index]
        if subj in ['你', '你们', '我们', '我'] or obj in ['你', '你们', '我们', '我']:
            return None
        #print(obj,subj, postags[obj_index])
        if obj in NLPUtil.Interrogative_pronouns:
            print("cls.get_desc(subj)")
            return cls.get_desc(subj)
        elif postags[obj_index] in NLPUtil.noun_for_pedia and postags[subj_index] in NLPUtil.noun_for_pedia:
            print("cls.get_judge(subj,verb,obj)")
            return cls.get_judge(subj,verb,obj)
        elif postags[obj_index] == 'a' and postags[subj_index] in NLPUtil.noun_for_pedia:
            print("cls.get_judge(subj,verb,obj)")
            return cls.get_judge(subj,verb,obj)
        elif subj in NLPUtil.Interrogative_pronouns:
            print("cls.get_desc(obj)")
            return cls.get_desc(obj)

    """
    问句提取出主语、介词和宾语

    1.宾语词性为疑问代词->询问属性
    eg.北京在哪（有错）
    2.宾语是名词性词汇->确定主语是否有宾语这一属性
    eg.北京在中国吗

    """

    @classmethod
    def answer_SBV_POB(cls, words, arcs_dict, postags, hed_index):
        prep = words[hed_index]
        if 'POB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['POB'][0]
        obj = words[obj_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]
        subj = words[subj_index]
        if subj in ['你', '你们', '我们', '我'] or obj in ['你', '你们', '我们', '我']:
            return None
        if obj in NLPUtil.Interrogative_pronouns:
            return cls.get_desc(subj)
        elif postags[obj_index] in NLPUtil.noun_for_pedia and postags[subj_index] != 'r':
            return cls.get_judge(subj,prep,obj)
        elif subj in NLPUtil.Interrogative_pronouns:
            return cls.get_desc(obj)


    """
    提取出问句的主语、介词和介词宾语
    问句含义：询问主语的动宾属性
    eg:红豆是谁的歌
    """

    @classmethod
    def answer_SBV_ATT_VOB(cls, words, arcs_dict, postags, hed_index):
        verb = words[hed_index]
        if 'VOB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['VOB'][0]
        obj = words[obj_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]
        subj = words[subj_index]
        if 'ATT' not in arcs_dict[obj_index].keys():
            return None
        att_index = arcs_dict[obj_index]['ATT'][0]
        att = words[att_index]
        if subj in ['你', '你们', '我们', '我']:
            return None
        print(subj,att,obj)
        if att in NLPUtil.Interrogative_pronouns:
            #红豆是谁的歌
            ans = cls.get_attr(subj,obj)
            """
            凡是得不到属性的属性提问都返回描述
            """
            if ans == None:
                ans = cls.get_desc(subj)
            return ans

        elif postags[att_index] in NLPUtil.noun_for_pedia:
            #五星红旗是中华人民共和国国旗吗
            print(att)
            return cls.get_judge_att(subj,verb,att,obj,att)
        elif postags[obj_index] in NLPUtil.noun_for_pedia:
            #五星红旗是中华人民共和国国旗吗
            print(att)
            return cls.get_judge(subj,verb,obj)


    """
    提取出问句的主语、介词和介词宾语
    问句含义：询问主语的介宾属性
    """

    @classmethod
    def answer_SBV_ATT_POB(cls, words, arcs_dict, postags, hed_index):
        pron = words[hed_index]
        if 'POB' not in arcs_dict[hed_index].keys():
            return None
        obj_index = arcs_dict[hed_index]['POB'][0]
        obj = words[obj_index]
        if 'SBV' not in arcs_dict[hed_index].keys():
            return None
        subj_index = arcs_dict[hed_index]['SBV'][0]
        subj = words[subj_index]
        if 'ATT' not in arcs_dict[obj_index].keys():
            return None
        att_index = arcs_dict[obj_index]['ATT'][0]
        att = words[att_index]
        print(att,subj,pron)
        if att in NLPUtil.Interrogative_pronouns:
            ans = cls.get_attr(subj,obj)
            print(ans)
            if ans == None:
                ans = cls.get_desc(subj)
                return ans
            else:
                return ans
        elif postags[att_index] in NLPUtil.noun_for_pedia:
            return cls.get_judge_att(subj,pron,att,obj,att)

    @classmethod
    def get_attr(cls, target, attr):
        uri = "https://api.ownthink.com/kg/knowledge?entity=" + target
        r = requests.post(uri)

        if r.json()['message'] == 'success':
            try:
                ans_dict = dict(r.json()['data']['avp'])
                keys = ans_dict.keys()
                print(keys)
                ans = NLPUtil.get_similarity(attr, keys)
                if ans != None:
                    return target+"的"+ans+"为"+ans_dict[ans]+"\n"
            except Exception as e:
                print(r.json())
                print(e)
        else:
            return "对不起，我不太明白你在说什么\n"

    @classmethod
    def get_desc(cls,target):
        uri = "https://api.ownthink.com/kg/knowledge?entity=" + target
        r = requests.post(uri)
        if r.json()['message'] == 'success':
            try:
                ans = dict(r.json())['data']['desc']
                if ans != None:
                    return ans
            except Exception as e:
                print(r.json())
                print(e)
        else:
            return "对不起，我不太明白你在说什么\n"

    @classmethod
    def get_judge(cls, subj, hed, obj):
        hed_arr = []
        if len(hed) > 2 and '不' in hed:
            hed_arr = hed.split("不")
            hed = hed_arr[len(hed_arr)-1]
        print(subj, hed, obj)
        uri = "https://api.ownthink.com/kg/knowledge?entity=" + subj
        r = requests.post(uri)
        print(r.json())

        if r.json()['message'] == 'success':
            try:

                ans_list = list(r.json()['data']['avp'])
                #print(ans_list)
                values = [x[1] for x in ans_list]
                ans = NLPUtil.get_similarity(obj, values)
                if ans != None:
                    return "是的，" + subj + hed + obj + "\n"
                elif hed == '有':
                    return "很抱歉，" + subj + "没" + hed +obj + "\n"
                else:
                    return "很抱歉，" + subj + "不" + hed +obj + "\n"
            except Exception as e:
                print(r.json())
                print(e)


    @classmethod
    def get_judge_att(cls, subj, hed, att, obj, attr):
        uri = "https://api.ownthink.com/kg/knowledge?entity=" + subj
        r = requests.post(uri)

        if r.json()['message'] == 'success':
            try:
                ans_list = list(r.json()['data']['avp'])
                values = [x[1] for x in ans_list]
                ans = NLPUtil.get_similarity(attr, values)
                if ans != None:
                    return "是的，" + subj + hed + att + obj + "\n"
                elif hed == '有':
                    return "很抱歉，" + subj + "没" + hed + att + obj + "\n"
                else:
                    return "很抱歉，" + subj + "不" + hed + att + obj + "\n"
            except Exception as e:
                print(e)
                print(r.json())



