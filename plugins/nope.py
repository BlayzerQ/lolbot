# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None
	
    plugin_type = 'command'

    def __init__(self, vk):
        self.vk = vk
        print('Nope')

    def getkeys(self):
        keys = [u'нет', u'неа', u'nope', u'видосик']
        ret = {}
        for key in keys:
            ret[key] = self
        return ret

    def call(self, msg):
        answer = []

        answer.append(u'&#127770;')

        self.vk.respond(msg, {'message': answer,
            'attachment': 'video174811191_170020157'})
