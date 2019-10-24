# -*- coding: utf-8 -*-
# File: chatterbot_chat.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-07
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import logging
# logging.basicConfig(level=logging.INFO)

class ChatterbotChat():
    @classmethod
    def create_chatterbot(cls):
        """
        用语料训练一个chatbot
        :return:
        """
        cn_chatter = ChatBot("National Lib Chatter",
                             #input_adapter='chatterbot.input.TerminalAdapter',
                             #output_adapter='chatterbot.output.TerminalAdapter',
                             logic_adapters=[
                                 {
                                     'import_path': 'chatterbot.logic.BestMatch',
                                     'default_response': '很抱歉，我还在学习中，暂时无法解答这个问题',
                                     'maximum_similarity_threshold': 0.80
                                 }
                             ]

        )
        trainer = ChatterBotCorpusTrainer(cn_chatter)
        trainer.train("chatterbot.corpus.chinese.greetings")

        #trainer.train()

        # trainer.export_for_training('./my_export.json')

        return cn_chatter
    @classmethod
    def load_chatterbot(cls):
        """
        加载训练好的bot
        :return:
        """
        cn_chatterbot = ChatBot('National Lib Chatter',
                                #storage_adapter='chatterbot.storage.SQLStorageAdapter',
                                #input_adapter = 'chatterbot.input.TerminalAdapter',
                                #output_adapter = 'chatterbot.output.TerminalAdapter',

                                logic_adapters=[
                                    {
                                        'import_path': 'chatterbot.logic.BestMatch',
                                        'default_response': '很抱歉，我还在学习中，暂时无法解答这个问题',
                                        'maximum_similarity_threshold': 0.75
                                    }
                                ]
                                #database = './db.sqlite3'

        )
        return cn_chatterbot



if __name__ == '__main__':
    test_chatter = ChatterbotChat.create_chatterbot()
    test_chatter = ChatterbotChat.load_chatterbot()
    while True:
        try:
            user_input = input('USER:')
            response = test_chatter.get_response(user_input)
            print('BOT:', response)
        # 直到按ctrl-c 或者 ctrl-d 才会退出
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
