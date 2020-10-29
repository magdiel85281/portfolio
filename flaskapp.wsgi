#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"~/portfolio/app")

from FlaskApp import app as application
application.secret_key = 'asdfa7asgltg4439n9ujfasdh04n'