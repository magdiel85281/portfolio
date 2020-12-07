.PHONY: help setup installs env run_debug_mode

help:
	@echo ""
	@echo "setup: Update/update server. Install pip and virtualenv and create dir venv."
	@echo "        After this command is complete, activate virtual environment."
	@echo ""
	@echo "installs: Installs packages for server configuration, configures, and restarts"
	@echo "        Apache2 server. After this command is complete, refer to README.md for"
	@echo "        next step."
	@echo ""
	@echo "env: Install Python packages."
	@echo ""
	@echo "run_debug_mode: Run on localhost:5000 with debug=True."
	@echo ""
	@echo ""
	@echo ""
	@echo ""
setup:
	sudo apt-get update
	sudo apt-get upgrade

	sudo apt-get -y install python3-pip
	pip3 install virtualenv
	python3 -m virtualenv venv 
	
	@echo ""
	@echo "Initial setup complete. Activate the virtual environment with:"
	@echo ""
	@echo "    . venv/bin/activate"
	@echo ""
	@echo "Then, continue setting up the server with:"
	@echo ""
	@echo "    make installs"
	@echo ""
	@echo ""


installs:
	sudo apt-get -y install apache2 apache2-dev
	sudo apt-get -y install libapache2-mod-wsgi-py3 python-dev
	# sudo apt-get -y install mysql-server
	# sudo mysql_secure_installation
	# sudo apt -y install php libapache2-mod-php
	sudo ln -sT ~/portfolio /var/www/html/flaskapp
	sudo a2enmod wsgi
	sudo service apache2 restart

	@echo "Server configured!"
	@echo ""
	@echo "Now, refer to README.md for setting up the website configuration file."

env:
	pip install -r requirements.txt
	
run_debug_mode:
	python app/__init__.py
