#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import simplejson
from xml.etree import ElementTree as ET
import os
import re 
import string
import json
import math
import c 


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
    def post(self):
        datafromserver = simplejson.loads(self.request.body)
        
        nodes = datafromserver[0]
        links = datafromserver[1]
        agents = datafromserver[2]
        source = datafromserver[3]
        c.readModel(datafromserver)
        code =  c.main()
#        init()
#        createnodes()
#        createlinks()
#        final()
#        print "\n\n\n" 
        self.response.out.write(code)


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)
    


