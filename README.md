# Logger-solution
Description : Tail Logs from a remote server

## Prerequisites 
Install all the required python modules using pip3: 
- flask 
- loguru
- os
- time
- paramiko
- datetime 


Once you have cloned the repo... you need make sure you have access on the remote servers. We will be accessing the servers using ssh keys <br />
Run the application using the following command: <br />
##### python3 logger.py

Your application will be accessible on http://localhost/  <br />
You need to enter the IP of the remote server and the location of the file you can want to tail and the username with which you want to ssh into the server.  <br />

## Deployment
All the code is managed in Git. So for Deployment you need to follow the following steps:  <br />

1. Run the script deploy.sh in deployment folder for rollingout the latest changes:  <br />
sh deployment/deploy.sh


## Basic Smoke Test
1. You can append a line to the existing logfile and check if the changes are reflected in the browser.
