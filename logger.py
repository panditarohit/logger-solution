from flask import Flask, render_template, Response, request
from loguru import logger
import os
from time import sleep
import paramiko
import datetime 


APP = Flask(__name__, static_folder="app/static/", template_folder="app/static/")
def flask_logger(projectpath,ip,username):
    host = ip
#    user = 'rohitpandita'
    user = username
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')  # Define key path
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    s.connect(host, 22, user, pkey=mykey, timeout=5)
    sftp_client = s.open_sftp()
    remote_file = sftp_client.open(projectpath)
    while(1):
           for line in remote_file:
                yield line.encode()
                sleep(1)

    s.close()


@APP.route("/", methods=["GET"])
def root():
    """index page"""
    return render_template("index.html")
@APP.route("/log_stream", methods=["POST","GET"])
def stream():
    """returns logging information"""
    ip= request.form['ip']
    projectpath= request.form['projectFilepath']
    username= request.form['username']
    return Response(flask_logger(projectpath,ip,username), mimetype="text/plain", content_type="text/event-stream")
if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=80, threaded=True)
