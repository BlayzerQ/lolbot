# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None

    def __init__(self, vk):
        self.vk = vk
        print('Помощь')

    def getkeys(self):
        keys = [u'помощь', u'помоги', u'команды', u'commands', u'help', u'хелп']
        ret = {}
        for key in keys:
            ret[key] = self
        return ret

    def call(self, msg):
        commands = []

        commands.append(u'Все доступные команды: \n мемы \n сиськи \n музыка \n шар \n двач \n шкуры \n время \n курс \n др \n привет \n рандом \n плагины')

        self.vk.respond(msg, {'message': commands})