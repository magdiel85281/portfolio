.PHONY: help installs env app

help:
	@echo ""
	@echo "installs: Updates and installs packages for Ubuntu server"
	@echo ""
	@echo "env: Install python packages"
	@echo ""
	@echo "app: Run Flask app"

installs:
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get -y install apache2
	sudo apt-get -y install libapache2-mod-wsgi python-dev
	# sudo apt-get -y install mysql-client mysql-server
	# sudo mysql_secure_installation
	sudo apt -y install php libapache2-mod-php
	sudo systemctl restart apache2
	sudo apt-get -y install python3-pip
	export PATH="$PATH:/home/ubuntu/.local/bin"

env:
	pip install -r requirements.txt

app:
	python app/__init__.py