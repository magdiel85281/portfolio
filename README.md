# Portfolio Website
This repo houses code and instructions for the Flask app that showcases my portfolio. The purpose of maintaining the code here is to create something deployable and easily repeatable.

---

## Deployment
Currently, this website is designed to be deployed on an instance of AWS Ubuntu 20.04. Deployment consists of 4 steps:

1. Initial Setup and Virtual Environment
2. Apache2 Setup
3. Python Installs
4. Modifications to DNS Settings to Use Domain Name

---

## Initial Setup and Virtual Environment
Spin up the server and connect to the instance using the ssh command. First, add the following to `~/.bashrc`:

`export PATH=$PATH:/home/ubuntu/.local/bin`

Once you've saved the changes:

`source ~/.bashrc`

Then, clone the repo and install the initial packages with the following:

`git clone https://github.com/magdiel85281/portfolio.git`<br>
`cd portfolio` <br>
`sudo apt install make` <br>
`make setup`

Once complete, activate the virtual environment with:

`. venv/bin/activate`

---

## Apache2 Setup
To install and enable Apache2, first: 

`make installs`

Once this has completed successfully, you should get the message that instructs you to refer to README.md for setting up the configuration file. Edit this file with:

`sudo vim /etc/apache2/sites-enabled/000-default.conf`

Then, add the following after `DocumentRoot /var/www/html`

        WSGIDaemonProcess flaskapp threads=5
        ServerName mdelgadillo.com
        WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi

        <Directory app>
                WSGIProcessGroup flaskapp
                WSGIApplicationGroup %{GLOBAL}
                Order deny,allow
                Allow from all
        </Directory>


Next, restart the Apache2 server with:

`sudo service apache2 restart`

---

## Modifications to DNS Settings to Use Domain Name
Finally, at your domain name host (i.e. Namecheap), modify the DNS settings to include two separate A records with the server's Public IPv4 Address (i.e. 52.35.189.229) as the value. For the Host on each, set one to `@` and the other to `*`. 

---

## Future State
Already partially written out is a `Contact Me` button that pops up a modal for entering information and a message. My thoughts for this are to create a database that will store the information and messages, and an admin page that will be able to display this. Alternatively (additionally?), set up a trigger or a cron job that will send these message to my email address.

Right now, the projects are hard-coded into `main.html`. As I get more projects under my belt, it would make more sense to use a content manager in tandem with a Python script that will write the html file for the main page. 

