#!/usr/bin/env python2
#  Using http://www.codestance.com/tutorials-archive/python-tornado-web-server-with-websockets-part-i-441
#  as a starting point
# http://www.tornadoweb.cn/en/documentation#module-index
from rdflib.plugins.parsers.pyRdfa.rdfs.process import subPropertyOf
import tornado.ioloop
import tornado.web
import os
from os.path import expanduser
import subprocess

import liblo
import jack

from tornado.options import define, options, parse_command_line

define("port", default=7777, help="run on the given port", type=int)

nsmd_port = "7000"

home = expanduser("~")
session_root = home + '/NSM Dev Sessions'

nsmd = subprocess.Popen(['nsmd',
                         '--osc-port', nsmd_port,
                         '--session-root', session_root],
                        stdout=subprocess.PIPE)
pid = nsmd.pid

print("Started nsmd daemon with pid ", repr(pid))

# Pipe all output from the nsmd subprocess and show it on the python console
nsmd_output = iter(nsmd.stdout.readline, b"")

# Note: using http://tornado.readthedocs.org/en/branch4.0/guide/templates.html

# ######## INDEX HANDLER ######## #
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        sessions = ["Fake session 1", "Fake session DERP 2", "Fake session boink 3"]
        # ToDo: Get a list of NSM sessions and print it out
        # http://non.tuxfamily.org/nsm/API.html#n:1.2.7.cd pytho
        self.write("Tornado webserver is running, dawg!")
        self.render("famous_template.html", title="Stagecraft", sessions=sessions)


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
#    app.listen(7777)
    tornado.ioloop.IOLoop.instance().start()
