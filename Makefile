.PHONY: help installs env app

help:
	@echo ""
	@echo "setup: Creates a virtual environment and sets up server."
	@echo ""
	@echo "app: Run Flask app"

setup:
	sudo apt-get update
	sudo apt-get upgrade

	sudo apt-get -y install python3-pip
	pip3 install virtualenv
	cd portfolio && python3 -m virtualenv venv 
	cd portfolio && . venv/bin/activate
	cd portfolio && pip install -r requirements.txt
	

	sudo apt-get -y install apache2
	sudo apt-get -y install libapache2-mod-wsgi-py3 python-dev
	# sudo apt-get -y install mysql-server
	# sudo mysql_secure_installation
	# sudo apt -y install php libapache2-mod-php
	sudo ln -sT ~/portfolio /var/www/html/flaskapp
	sudo a2enmod wsgi
	sudo systemctl restart apache2

	@echo "Server configured!"
	@echo ""
	@echo "Now, refer to README.md for setting up the website configuration file."


app:
	python app/__init__.py
