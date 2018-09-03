#!/home/cadilla1/virtualenv/acaciastrain.cadillacabe.com_web__flask/3.6/bin/python
''' runs flask app in WSGIServer '''
import sys
sys.path.insert(0, '~/virtualenv/acaciastrain.cadillacabe.com_web__flask/3.6/lib/python3.6/site-packages')

from flup.server.fcgi import WSGIServer
from flaskapp import *

class ScriptNameStripper(object):
     def __init__(self, app):
         self.app = app

     def __call__(self, environ, start_response):
         environ['SCRIPT_NAME'] = ''
         return self.app(environ, start_response)

app = ScriptNameStripper(app)

if __name__ == '__main__':
    WSGIServer(app).run()
    sys.exit()
