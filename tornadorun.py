#!flask/bin/python

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8000)
IOLoop.instance().start()
