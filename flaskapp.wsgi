activate_this = '/home/ubuntu/portfolio/venv/bin/activate_this.py'
with open(activate_this) as f:
	exec(f.read(), dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/flaskapp/app")

from __init__ import app as application
application.secret_key = 'asdfa7asgltg4439n9ujfasdh04n'
