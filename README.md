# Portfolio Website

This repo houses code for the Flask app that showcases my portfolio.

---

## Deployment

Currently, this app is being deployed on an instance of AWS Ubuntu 20.04. With the server spun up, you'll need to update/upgrade it, as well as install all the packages needed for deployment and use of the domain name. Clone the repo onto the server, and all the installs are taken care of with the following terminal commands:

`cd portfolio` <br>
`sudo apt install make` <br>
`make installs`

---

## Python Packages

Install the required Python packages with: 

`make env`

Note: I'm not using a virtual environment for this as it is the only thing running on this server.

