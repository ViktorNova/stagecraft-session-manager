#!/usr/bin/env python2
#  Using http://www.codestance.com/tutorials-archive/python-tornado-web-server-with-websockets-part-i-441
#  as a starting point
# http://www.tornadoweb.cn/en/documentation#module-index
from rdflib.plugins.parsers.pyRdfa.rdfs.process import subPropertyOf
import tornado.ioloop
import tornado.web
import os
import subprocess

import liblo
import jack

from tornado.options import define, options, parse_command_line

define("port", default=7777, help="run on the given port", type=int)

nsmd_port = "7000"
session_root = "/home/stagecraft/NSM Dev Sessions"
nsmd = subprocess.Popen(['nsmd',
                         '--osc-port', nsmd_port,
                         '--session-root', session_root],
                        stdout=subprocess.PIPE)
pid = nsmd.pid

print("Started nsmd daemon with pid ", repr(pid))

# Pipe all output from the nsmd subprocess and show it on the python console
nsmd_output = iter(nsmd.stdout.readline, b"")
for line in nsmd_output:
    print(line)  # yield line


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
