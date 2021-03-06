# -*- coding: utf-8 -*-

import random, requests, json, urllib

class Plugin:
    vk = None
	
    plugin_type = 'command args'

    def __init__(self, vk):
        self.vk = vk
        print('Поиск по вики')

    def getkeys(self):
        keys = [u'вики', u'wiki', u'wikipedia', u'википедия']
        ret = {}
        for key in keys:
            ret[key] = self
        return ret

    def call(self, msg, args=None):

    	if len(args) >= 1:
    		for arg in args[1:]:
    			
                query = ' '.join(args)
                wiki_api  = 'http://ru.wikipedia.org/w/api.php?'  # А что если нужна не русская вики? очевидно русская, потому что аудитория вк только русская. для гурманов можно ссылку на англ версию при желании
                wiki_main = 'http://ru.wikipedia.org/wiki/'
                pars = {
                    'action': 'query',
                    'list': 'search',
                    'format': 'json',
                    #no ' '
                    'srsearch': query,
                    'srprop': 'snippet',
                    'srlimit': '3'
                }
                
                try:
                    r = requests.get(wiki_api, params=pars)  #А что если он не ответит?
                except requests.exceptions.ConnectionError:
                    self.vk.respond(msg, {'message': u'Не могу достучатсья до вики.'})
                    return
                query      = json.loads(r.text)
                query      = query['query']
                searchinfo = query.get('searchinfo')
                
                if not searchinfo.get('suggestion') is None:
                    self.vk.respond(msg, {'message': u'Вы имели в виду ' + unicode(searchinfo.get('suggestion')) + u'?'})
					
                search = query.get('search')  #А что если он ответит криво? как?
                if len(search) == 0:
                    self.vk.respond(msg, {'message': u'Ошибка в запросе.'})
                title = search[0].get('title')
                if not title:
                    self.vk.respond(msg, {'message': u'Ошибка в запросе.'})
                pars = {
                    'action': 'query',
                    'prop': 'extracts',
                    'format': 'json',
                    'titles': title,
                    'exintro': '',
                    'explaintext': '',
                    'indexpageids': ''
                }
                r = requests.get(wiki_api, params=pars)
                query = r.json()
                query = query['query']['pages'][query['query']['pageids'][0]]
                #Добаить ф-цию запроса всего 'extract' сначала нужно понять, почему даже это не работает
                # it doesnt work because of the limit for the length of the message.
                answer = '\n' + wiki_main + urllib.quote(title.replace(' ', '_').encode('utf-8')) 
                self.vk.respond(msg, {'message': answer})
    	else:
			self.vk.respond(msg, {'message': 'Что искать?'})
