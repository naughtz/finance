import os
import tornado.web
from webAPI import indexHandler,loginHandler,ifLoginHandler,todayInfoHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    "template_path": os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(BASE_DIR, "static"),
    "cookie_secret": 'dtyijt3eri7fegraeyfrytrftey5e',
}

HANDLERS = [
    (r"/", indexHandler),
    (r"/ajax/ifLogin", ifLoginHandler),
    (r"/ajax/todayInfo", todayInfoHandler),
    (r"/ajax/login", loginHandler)
]

UI_MODULES={
	
}

application = tornado.web.Application(
    handlers = HANDLERS,
    ui_modules=UI_MODULES,
**SETTINGS)