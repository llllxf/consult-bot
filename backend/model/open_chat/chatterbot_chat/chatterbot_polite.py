from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
class ChatterPolite():

    @classmethod
    def create_chatterbot(cls):
        bot = ChatBot(
            'libot',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': '很抱歉我还在学习中，暂时回答不了这个问题',
                    'maximum_similarity_threshold': 0.70
                }
            ]
        )

        trainer = ListTrainer(bot)


        trainer.train([
            '你好',
            '你好',
            '你叫什么',
            '我叫libot',
            '你可以干嘛',
            '我可以提供图书馆咨询服务'
        ])
        return bot
