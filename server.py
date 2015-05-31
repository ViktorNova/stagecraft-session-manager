#!/usr/bin/env python2
#  Using http://www.codestance.com/tutorials-archive/python-tornado-web-server-with-websockets-part-i-441
#  as a starting point
# http://www.tornadoweb.cn/en/documentation#module-index
import tornado.ioloop
import tornado.web
import time
import liblo
import jack

from tornado.options import define, options, parse_command_line


define("port", default=7777, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Tornado webserver is running, yo!")
        self.finish()


print("Derpy doo")


client = jack.Client("Stagecraft Show Manager")
client.activate()

print("Running as JACK Client: ", client)
print("Listing Ports:")

#for port in client.get_ports():
#    IndexHandler.write(port.name)

app = tornado.web.Application([
    (r'/', IndexHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
