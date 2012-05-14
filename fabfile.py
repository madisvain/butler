#coding: utf-8

import time

from fabric.api import env, run

from utils import make_password


# Settings
env.hosts = ['ec2-46-137-36-192.eu-west-1.compute.amazonaws.com']
env.user = 'ec2-user'
env.key_filename = '~/.ssh/aws.pem'
#env.password = None


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
    sudo('yum -y update')

def free_memory():
    run('free -m')

# Software installation commands
def install_requirements():
    sudo('easy_install pip')
    sudo('yum -y install gcc-c++')
    sudo('yum -y install python-devel')
    sudo('yum -y install libxml2-python libxml2-devel')

def install_http_server():
    sudo('yum -y install nginx')
    sudo('service nginx start')

def install_wsgi_server():
    sudo('pip install uwsgi')

def install_db():
    password = make_password(10)
    
    sudo('yum -y install mysql-server mysql mysql-devel')
    sudo('service mysqld start')
    
    # Scure the mysql installation
    run('mysqladmin -u root password ' + password)
    run('mysql -uroot -p' + password + ' -e \"DROP USER \'\'@\'localhost\';\"')
    run('mysql -uroot -p' + password + ' -e \"DROP DATABASE test;\"')
    run('mysql -uroot -p' + password + ' -e \"FLUSH PRIVILEGES;\"')
    #run('mysql_secure_installation') # Secure the mysql installation

# Environment setup commands
def python_requirements():
    run('pip install -r templates/requirements.txt')

def virtualenv():
    pass
    
def repository():
    pass
