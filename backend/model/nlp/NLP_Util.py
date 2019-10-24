# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
print("nlp",project_path)
sys.path.append(project_path)
from model.kb_prepare import Neo4jPrepare
from model.pedia import CilinSimilarity
from pyltp import Segmentor, Postagger, Parser
import jieba

"""
NLP工具类
"""
class NLPUtil(object):

    @classmethod
    def __init__(cls,model_path):
        """
        1.获取字典
        2.加载结巴的自定义文档
        3.定义停用词
        """
        cls.model_path = model_path

        cls.neo_util = Neo4jPrepare()
        cls.room_list, cls.room_alias_list, cls.floor_list, cls.floor_alias_list, cls.area_list, cls.area_alias_list, cls.resource_list, cls.resource_alias_list, cls.restype_list, cls.restype_alias_list, cls.card_list, cls.card_alias_list, cls.library, cls.library_alias_list, cls.service_list, cls.service_alias_list,cls.task_list, cls.task_alias_list, cls.multype_list,cls.multype_alias_list,cls.ttype_list,cls.ttype_alias_list,cls.goods_list,cls.goods_alias_list = cls.neo_util.get_all_varname()

        cls.stopwords = ['什么', '哪里', '怎么', '有', '走', '去', '可以', '如何', '怎样', '的', '地', '得']
        cls.cilin = CilinSimilarity()

        """
        分词
        """
        cls.segmentor = Segmentor()
        path_for_model = os.path.abspath(os.path.join(os.getcwd(), "../../../../"))
        cls.segmentor.load(path_for_model + "/" + cls.model_path + "/cws.model")

        """
        词性标注
        """
        cls.postagger = Postagger()
        cls.postagger.load(path_for_model + "/" + cls.model_path + "/pos.model")
        """
        句法依存分析
        """
        cls.parser = Parser()
        cls.parser.load(os.path.join(path_for_model+"/"+cls.model_path+"/parser.model"))

        """
        疑问代词
        """
        cls.Interrogative_pronouns = ['哪里', '什么', '怎么', '哪', '为什么', '啥','谁']
        cls.noun_for_pedia = ['n', 'nh', 'ni', 'nl', 'ns', 'nz', 'nt','i']
        cls.clear_word = ['嗯','噫','啊','哦']

        jieba.load_userdict("../../resource/guotu_dict.txt")

    @classmethod
    def clear_question(cls, question):

        question = question.replace('。', '')
        question = question.replace('.', '')
        question = question.replace('?', '')
        question = question.replace('？', '')
        question = question.replace('!', '')
        question = question.replace('！', '')
        question = question.replace('，', '')
        question = question.replace(',', '')
        for c_word in cls.clear_word:
            question = question.replace(c_word, '')
        question = question.rstrip()
        question = question.lstrip()
        return question




    '''
    抽取出句子中的实体，同时将实体替换为模版符号：ROOM,AREA,FLOOR,CARD,AREA,SERVICE,RES
    SERVICE实体比较特别，他们的统一属性通过转为SERVICE查询，但是他们有具有个性，所以最终生成两个替换后的句子，
    一个将服务实体替换为SERVICE，一个不替换，优先匹配不替换的，如果不替换的找不到对应的模板则再匹配替换的。
    '''
    @classmethod
    def repalce_question(cls, question_n):
        question_s = question_n
        question_first = question_n
        if '国图' in question_first:
            question_first = question_first.replace('国图','')
        if '国家图书馆' in question_first:
            question_first = question_first.replace('国家图书馆','')
        if '图书馆' in question_first:
            question_first = question_first.replace('图书馆','')

        entity_dict = {}
        word_list = jieba.cut(question_n, cut_all=False)
        room_entity = []
        resource_entity = []
        floor_entity = []
        area_entity = []
        restype_entity = []
        multype_entity = []
        ttype_entity = []
        card_entity = []
        library_entity = []
        service_entity = []
        task_entity = []
        goods_entity = []

        for word in word_list:
            #print(word)

            if word in cls.stopwords:
                continue

            for (room_alias, room) in zip(cls.room_alias_list, cls.room_list):
                if word in room_alias:
                    room_entity.append(room)
                    question_first = question_first.replace(word, 'ROOM')
                    question_n = question_n.replace(word, 'ROOM')
                    question_s = question_s.replace(word, 'ROOM')
                    break
            for (resource_alias, resource) in zip(cls.resource_alias_list, cls.resource_list):
                if word in resource_alias:
                    resource_entity.append(resource)
                    question_first = question_first.replace(word, 'RES')
                    question_n = question_n.replace(word, 'RES')
                    question_s = question_s.replace(word, 'RES')
                    break
            for (goods_alias, goods) in zip(cls.goods_alias_list, cls.goods_list):
                if word in goods_alias:
                    goods_entity.append(goods)
                    question_first = question_first.replace(word, 'GOODS')
                    question_n = question_n.replace(word, 'GOODS')
                    question_s = question_s.replace(word, 'GOODS')
                    break
            for (floor_alias, floor) in zip(cls.floor_alias_list, cls.floor_list):
                if word in floor_alias:
                    floor_entity.append(floor)
                    question_first = question_first.replace(word, 'FLOOR')
                    question_n = question_n.replace(word, 'FLOOR')
                    question_s = question_s.replace(word, 'FLOOR')
                    break
            for (restype_alias, restype) in zip(cls.restype_alias_list, cls.restype_list):
                #print(restype_alias)
                if word in restype_alias:
                    restype_entity.append(restype)
                    question_first = question_first.replace(word, 'RTYPE')
                    question_n = question_n.replace(word, 'RTYPE')
                    question_s = question_s.replace(word, 'RTYPE')
                    break
            for (multype_alias, multype) in zip(cls.multype_alias_list, cls.multype_list):
                if word in multype_alias:
                    multype_entity.append(multype)
                    #question_first = question_first.replace(word, 'MTYPE')
                    #question = question.replace(word, 'MTYPE')
                    question_s = question_s.replace(word, 'MTYPE')
                    break
            #print(cls.ttype_alias_list,cls.ttype_list)
            for (ttype_alias, ttype) in zip(cls.ttype_alias_list, cls.ttype_list):
                if word in ttype_alias:
                    #print(word)
                    ttype_entity.append(ttype)
                    question_first = question_first.replace(word, 'TTYPE')
                    question_n = question_n.replace(word, 'TTYPE')
                    #question2 = question2.replace(word, 'TTYPE')
                    break
            for (area_alias, area) in zip(cls.area_alias_list, cls.area_list):
                if word in area_alias:
                    area_entity.append(area)
                    question_first = question_first.replace(word, 'AREA')
                    question_n = question_n.replace(word, 'AREA')
                    question_s = question_s.replace(word, 'AREA')
                    break
            for (card_alias, card) in zip(cls.card_alias_list, cls.card_list):
                if word in card_alias:
                    card_entity.append(card)
                    question_s = question_s.replace(word, 'CARD')
                    break
            for library_alias in cls.library_alias_list:
                if word in library_alias:
                    library_entity.append(cls.library)

                    question_n = question_n.replace(word, 'LIBRARY')
                    question_s = question_s.replace(word, 'LIBRARY')
                    break

            for (service_alias, service) in zip(cls.service_alias_list, cls.service_list):
                if word in service_alias:
                    service_entity.append(service)
                    #print("service_entity",service_entity)
                    """
                    由于借书需要优先考虑为借书，所以优先不替换service
                    """
                    question_first = question_first.replace(word, 'SERVICE')
                    question_n = question_n.replace(word, 'SERVICE')

                    break
            for (task_alias, task) in zip(cls.task_alias_list, cls.task_list):

                if word in task_alias:
                    task_entity.append(task)
                    """
                    由于借书需要优先考虑为借书，所以优先不替换service
                    """
                    #question_first = question_first.replace(word, 'TASK')
                    question_s = question_s.replace(word, 'TASK')
                    break

        """
        如果句子不存在除了国家图书馆以外的实体，则将国家图书馆考虑为实体处理
        """
        """
        if len(room_entity) < 1 and len(floor_entity) < 1 and len(area_entity) < 1 and len(restype_entity) < 1 and len(
                card_entity) < 1 and len(ttype_entity)<1\
                and len(resource_entity) < 1 and len(service_entity) < 1 and len(task_entity) < 1:
            for library_alias in cls.library_alias_list[0]:
                if question2.find(library_alias) != -1:
                    question2 = question2.replace(library_alias, "LIBRARY")
                    library_entity.append(cls.library)
        """

        entity_dict['room'] = room_entity
        entity_dict['res'] = resource_entity
        entity_dict['floor'] = floor_entity
        entity_dict['area'] = area_entity
        entity_dict['restype'] = restype_entity
        entity_dict['multype'] = multype_entity
        entity_dict['ttype'] = ttype_entity
        entity_dict['card'] = card_entity
        entity_dict['service'] = service_entity
        entity_dict['library'] = library_entity
        entity_dict['task'] = task_entity
        entity_dict['goods'] = goods_entity

        origin_question = list(question_first)
        origin_question.reverse()
        question_first = "".join(origin_question)

        origin_question = list(question_n)
        origin_question.reverse()
        question_n = "".join(origin_question)

        origin_question = list(question_s)
        origin_question.reverse()
        question_s = "".join(origin_question)

        return question_first,question_n,question_s, entity_dict

    """
    :describe 词语语义相似度
    :arg 词
    """

    @classmethod
    def get_score(cls, word,arr):
        score = cls.cilin.sim2016(word,arr)
        return score
    """
    :describe 分词
    :arg 句子
    """

    @classmethod
    def cut_sentence(cls, sentence):
        words = list(jieba.cut(sentence))
        return words

    """
    :describe 词性分析
    :arg 分词列表
    """

    @classmethod
    def get_postag(cls, words):
        postags = cls.postagger.postag(words)
        return postags

    """
    :describe 句法依存
    :arg 分词列表, 词性列表
    """

    @classmethod
    def get_parse(cls, words, postags):
        parse = cls.parser.parse(words, postags)
        return parse

    """
    :describe 词汇相似度计算
    :arg word 代匹配的词
    entity 匹配的词列表

    """

    @classmethod
    def get_similarity(cls, word, entity):

        for sub_attr in entity:

            if word in sub_attr or sub_attr in word:
                return sub_attr
            e = 0
            for w in range(len(word)):
                if word[w] == sub_attr[e]:
                    e = e + 1
                    if e == len(sub_attr):
                        return sub_attr
            w = 0
            for e in range(len(sub_attr)):
                if sub_attr[e] == word[w]:
                    w = w + 1
                    if w == len(word):
                        return sub_attr

        for sub_attr in entity:

            attr_arr = jieba.cut(sub_attr)
            # print(list(attr_arr))
            max_score = 0
            max_attr = ""
            for a in attr_arr:
                #print(word,a,attr_arr)
                score = cls.get_score(word,a)
                #print(word, a, score)
                if score > max_score:
                    max_score = score
                    max_attr = sub_attr
                    # print(max_score,a,max_attr)
            if max_score > 0.8:
                return max_attr

    """
    :describe 
    得到问题对应的模版
    1.先对问题分词
    2.得到每个分词对应的词性
    3.得到句法依存分析树

    :arg 句子
    """

    @classmethod
    def get_sentence_pattern(cls, sentence):
        #print("pattern",cls.__dict__)
        words = cls.cut_sentence(sentence)
        postags = cls.get_postag(words)
        arcs = cls.parser.parse(words, postags)
        arcs_dict = cls._build_sub_dicts(words, arcs)
        hed_index = 0

        # for i in range(len(words)):
        # print(words[i],postags[i],arcs_dict[i])
        pattern = ""
        for i in range(len(arcs)):
            sub_arc = arcs[i]
            if sub_arc.relation == 'HED':
                hed_index = i

        for i in range(len(words)):
            if i == hed_index:
                pattern += 'HED'
            for sub_dict in arcs_dict:
                keys = sub_dict.keys()
                for k in keys:
                    if i in sub_dict[k]:
                        pattern += k
                        break
        # print(pattern)
        return words, pattern, arcs_dict, postags, hed_index


    """
    :decription: 为句子中的每个词语维护一个保存句法依存儿子节点的字典
    :args:
    words: 分词列表
    postags: 词性列表
    arcs: 句法依存列表
    """

    @classmethod
    def _build_sub_dicts(cls, words, arcs):
        sub_dicts = []
        for idx in range(len(words)):
            sub_dict = dict()
            for arc_idx in range(len(arcs)):
                """
                如果这个依存关系的头节点是该单词
                """
                if arcs[arc_idx].head == idx + 1:
                    if arcs[arc_idx].relation in sub_dict:
                        sub_dict[arcs[arc_idx].relation].append(arc_idx)
                    else:
                        sub_dict[arcs[arc_idx].relation] = []
                        sub_dict[arcs[arc_idx].relation].append(arc_idx)
            sub_dicts.append(sub_dict)

        return sub_dicts

    """
    :decription:完善识别的部分实体
    """

    def _fill_ent(self, words, postags, sub_dicts, word_idx):
        sub_dict = sub_dicts[word_idx]
        prefix = ''
        if 'ATT' in sub_dict:
            for i in range(len(sub_dict['ATT'])):
                prefix += self._fill_ent(words, postags, sub_dicts, sub_dict['ATT'][i])

        postfix = ''
        if postags[word_idx] == 'v':
            if 'VOB' in sub_dict:
                postfix += self._fill_ent(words, postags, sub_dicts, sub_dict['VOB'][0])
            if 'SBV' in sub_dict:
                prefix = self._fill_ent(words, postags, sub_dicts, sub_dict['SBV'][0]) + prefix

        return prefix + words[word_idx] + postfix


if __name__=='__main__':
    pass
