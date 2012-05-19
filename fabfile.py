#coding: utf-8

from time import time, localtime, strftime

from fabric.api import env, run
from fabric.colors import green, red

from utils import make_password, delta


# Settings
env.hosts = ['ec2-46-137-36-192.eu-west-1.compute.amazonaws.com']
env.user = 'ec2-user'
env.key_filename = '~/.ssh/aws.pem'


"""
Master commands
"""
def deploy():
    """
    Deployes the application.
    """
    upload_repository()

def install():
    """
    Installs the required software required for serving the application
    """
    install_requirements()
    install_http_server()
    install_cache()
    install_wsgi_server()
    install_db()

def build():
    """"
    Builds the complete environment and deployes the application into it.
    """
    
    start_time = time()
    print('time' + '\t\t' + 'delta' + '\t' + 'message')
    print(strftime("%H:%M:%S", localtime()) + '\t' + delta(start_time) + '\t' + green('Starting build process...'))
    
    #update()
    #install()
    #virtualenv()
    #deploy()

    print(strftime("%H:%M:%S", localtime()) + '\t' + delta(start_time) + '\t' + green('Your build is complete sir!'))

"""
Commands
"""

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
    sudo('chkconfig nginx on')

def install_cache():
    sudo('yum -y install memcached')

def install_wsgi_server():
    sudo('pip install uwsgi')

def install_db():
    password = make_password(10)
    
    sudo('yum -y install mysql mysql-server MySQL-python')
    sudo('service mysqld start')
    sudo('chkconfig mysqld on')
    
    # Scure the mysql installation
    run('mysqladmin -u root password ' + password)
    run('mysql -uroot -p' + password + ' -e \"DROP USER \'\'@\'localhost\';\"')
    run('mysql -uroot -p' + password + ' -e \"DROP DATABASE test;\"')
    run('mysql -uroot -p' + password + ' -e \"FLUSH PRIVILEGES;\"')

    # Write the output file
    


# Environment setup commands
def python_requirements():
    run('pip install -r templates/requirements.txt')

def virtualenv():
    pass
    
def repository():
    pass
