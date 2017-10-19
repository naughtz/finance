import tornado.ioloop
from tornado.options import define, options
import preparation
from urls import application

define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
	preparation.readTodayInfo()
	application.listen(options.port)
	print("Starting development server at http://127.0.0.1:"+str(options.port))
	print("Quit the server with CONTROL-C.")
	tornado.ioloop.IOLoop.instance().start()