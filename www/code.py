#!/usr/bin/env python
import web
import time, calendar
import json
from jsonrpc import ServiceProxy

# Uncomment this and make it false if you want to turn off browser debugging (important for release!)
web.config.debug = True


urls = (
	'/', 'index',
)

app = web.application(urls, locals())
db = json.load(open("/home/dac/well/db.access"))
rpc = json.load(open("/home/dac/well/rpc.access"))
db = web.database(dbn=str(db['type']), db=str(db['name']), user=str(db['user']), pw=str(db['pass']))

if web.config.get('_session') is None:
	store = web.session.DBStore(db, 'sessions')
	session = web.session.Session(app, store, initializer={'active_page':'index'})
	web.config._session = session
else:
	session = web.config._session

# set session parameters
web.config.session_parameters.update(cookie_name="tasty_cookie", cookie_domain="dacwell.com")

render = web.template.render('templates', base='base', globals={})

def create_render():
	return web.template.render('templates', base='base' )
		
class index:
	def GET(self):
		return "<h1>I'm alive!!!</h1>"

if __name__ == "__main__":
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()
