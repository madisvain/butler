#coding: utf-8

import time

from fabric.api import env, run


# Settings
env.hosts = ['ec2-46-137-138-67.eu-west-1.compute.amazonaws.com']
env.user = 'ec2-user'
env.key_filename = '~/.ssh/aws.pem'
env.password = None


'''
Master commands
'''
def install():
    install_requirements()
    install_http_server()
    install_wsgi_server()
    install_db()

def build():
    update()
    install()
    virtualenv()


'''
Commands
'''

# System commands
def update():
    print("Udating system software")
    run('sudo yum update')

def free_memory():
    run('free -m')

# Software installation commands
def install_requirements():
    run('sudo easy_install pip')
    run('sudo yum install gcc-c++')
    run('sudo yum install python-devel')
    run('sudo yum install libxml2-python libxml2-devel')

def install_http_server():
    run('sudo yum install nginx')
    run('sudo service nginx start')

def install_wsgi_server():
    run('sudo pip install uwsgi')

def install_db():
    run('sudo yum install mysql-server mysql mysql-devel')
    run('sudo service mysqld start')
    run('mysql_secure_installation') # Secure the mysql installation

# Environment setup commands
def python_requirements():
    run('pip install -r templates/requirements.txt')

def virtualenv():
    pass
    
def repository():
    pass
