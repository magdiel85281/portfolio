# Portfolio Website

This repo houses code for the Flask app that showcases my portfolio.

---

## Deployment

Currently, this app is designed to be deployed on an instance of AWS Ubuntu 20.04. With the server spun up, you'll need to update/upgrade it, as well as install all the server and Python packages needed for deployment and use of the domain name. To do this, connect to the instance using the ssh command and perform the following:

First, add the following to `~/.bashrc`:

`export PATH=$PATH:/home/ubuntu/.local/bin`

Once you've saved the changes:

`source ~/.bashrc`

Then, clone the repo and install the packages with:

`git clone https://github.com/magdiel85281/portfolio.git`<br>
`cd portfolio` <br>
`sudo apt install make` <br>
`make setup`

Once this has completed successfully, you should get the message `Server configured!`

---

## Use Domain Name
To use your domain name, you'll need to make some changes to the Apache2 default configuration file and with your domian name host. For the former, use vim to modify it with:

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

Finally, at your domain name host (i.e. Namecheap), modify the DNS settings to include the following: 
- Type: A Record
- Host: @
- Value: the server's Public IPv4 Address (i.e. 52.35.189.229)

