#!/usr/bin/env python3
#  Using http://www.stavros.io/tutorials/python/
# as a starting point
import tornado.ioloop
import tornado.web
import liblo
from tornado.options import define, options, parse_command_line


define("port", default=7777, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Tornado webserver is running, yo!")
        self.finish()

app = tornado.web.Application([
    (r'/', IndexHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
