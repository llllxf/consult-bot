# -*- coding: utf-8 -*-
# File: similar_question_bot.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-21
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)


from model.nlp import zhcnSeg
#from nlp import Sentence
from model.nlp import SentenceSimilarity


class similarQuestionBot():
    """
    通过检索相似问题的方式回复
    """

    @classmethod
    def __init__(cls):
        """
        初始化，加载问答列表
        """
        cls.qa_pair_dict = {}
        cls.q_list = []
        with open('../../resource/pair_for_reading_qa.txt', 'r', encoding='utf8') as in_file:
        #with open('../resource/pair_for_reading_qa.txt', 'r', encoding='utf8') as in_file:
            for line in in_file.readlines():
                q_str = line.split('\t')[0]
                a_str = line.split('\t')[-1].strip()
                #print(q_str,"====",a_str)
                cls.q_list.append(q_str)
                cls.qa_pair_dict[q_str] = a_str
        """
        with open('../../resource/pair_for_banzheng.txt', 'r', encoding='utf8') as in_file:
        #with open('../resource/pair_for_reading_qa.txt', 'r', encoding='utf8') as in_file:
            for line in in_file.readlines():
                q_str = line.split('\t')[0]
                a_str = line.split('\t')[-1].strip()
                #print(q_str,"====",a_str)
                cls.q_list.append(q_str)
                cls.qa_pair_dict[q_str] = a_str
        with open('../../resource/pair_for_jieyue.txt', 'r', encoding='utf8') as in_file:
        #with open('../resource/pair_for_reading_qa.txt', 'r', encoding='utf8') as in_file:
            for line in in_file.readlines():
                q_str = line.split('\t')[0]
                a_str = line.split('\t')[-1].strip()
                #print(q_str,"====",a_str)
                cls.q_list.append(q_str)
                cls.qa_pair_dict[q_str] = a_str
        """

        zhcn_seg = zhcnSeg()
        cls.sent_sim = SentenceSimilarity(zhcn_seg)
        cls.sent_sim.set_sentences(cls.q_list)
        # 默认用tfidf
        cls.sent_sim.TfidfModel()
        #cls.sent_sim.LsiModel()
        #cls.sent_sim.LdaModel()

    def answer_question(self, question_str):
        """
        返回与输入问句最相似的问句的固定回答
        :param question_str:
        :return:
        """
        most_sim_questions = self.sent_sim.similarity_top_k(question_str, 3)
        answer_list = []
        for item in most_sim_questions:
            answer = self.qa_pair_dict[item[0]]
            answer_list.append({"question": item[0], "answer": answer, "score": str(item[1])})
        return answer_list

if __name__ == '__main__':
    test_bot = similarQuestionBot()
    #print(test_bot.answer_question('怎么办证？'))
    #print(test_bot.answer_question('什么是OPAC系统？'))
    #print(test_bot.answer_question('如何利用国家图书馆网站检索国内外图书馆的公共书目？'))
    print(test_bot.answer_question('书怎么借？'))#0.6
    #print(test_bot.answer_question('实体资源的查找方法？'))
    #print(test_bot.answer_question('在哪里查阅工具书？'))



















