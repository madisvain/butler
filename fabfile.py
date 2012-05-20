#coding: utf-8

import os
from time import time, localtime, strftime

from fabric.api import env, run, sudo, local, put
from fabric.utils import puts
from fabric.colors import blue, cyan, green, magenta, red, white, yellow

from utils import make_password, delta, message


# Settings
env.hosts = ['ec2-46-137-20-135.eu-west-1.compute.amazonaws.com']
env.key_filename = '~/.ssh/aws.pem'

# Optional settings
env.user = 'ec2-user'
env.start_time = time()
env.project_name = os.path.basename(os.getcwd())
env.release = strftime('%Y%m%d%H%M%S')

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
    install_pip()
    install_nginx()
    install_memcached()
    install_uwsgi()
    install_mysql()

def build():
    """"
    Builds the complete environment and deployes the application into it.
    """
    
    message('Starting build process ...', color=green)
    
    update()
    install()
    virtualenv()
    upload_release()

    message('Your build is complete!', color=green)

"""
Commands
"""

# System commands
def update():
    message('Udating system software ...', color=yellow)
    sudo('yum -y update')

def upgrade():
    message('Upgrading system software ...', color=yellow)
    sudo('yum -y upgrade')

def free_memory():
    message('Outputting free memory:', color=yellow)
    run('free -m')

def restart_stack():
    message('Restarting everything', color=yellow)
    sudo('service nginx restart')
    sudo('service mysqld restart')
    # stopping uwsgi deamons
    #kill -INT `cat /tmp/uwsgi.pid`

def reload_stack():
    message('Reloading everything ...', color=yellow)
    sudo('service nginx reload')
    sudo('service mysqld restart')


# Software installation commands
def install_pip():
    message('Installing PIP for python ...', color=yellow)
    sudo('easy_install pip')

''' Web servers
'''
def install_nginx():
    message('Installing NGINX ...', color=yellow)
    sudo('yum -y install nginx')
    sudo('service nginx start')
    sudo('chkconfig nginx on')
    #returns number of cores
    #cat /proc/cpuinfo | grep processor | wc -l

def install_apache():
    pass

''' Caching
'''
def install_memcached():
    message('Installing Memcached ...', color=yellow)
    sudo('yum -y install memcached')
    
def install_varnish():
    pass

''' WSGI servers
'''
def install_uwsgi():
    message('Installing uWSGI ...', color=yellow)
    # requirements for uWSGI
    sudo('yum -y install gcc-c++')
    sudo('yum -y install python-devel')
    sudo('yum -y install libxml2-python libxml2-devel')
    # install uWSGI
    sudo('pip install uwsgi')

def install_gunicorn():
    pass

''' Databases
'''
def install_mysql():
    message('Installing & configuring MySQL ...', color=yellow)
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

def install_postgres():
    pass

''' Python environment commands
'''
def python_requirements():
    message('Installing required python packages ...', color=yellow)
    run('source /srv/%(project_name)s/env/bin/activate' % env)
    # Read the file in a forloop and print out what gets installed
    run('pip install -r templates/requirements.txt')

def virtualenv():
    sudo('pip install virtualenv')
    sudo('mkdir -p /srv/%(project_name)s && chown ec2-user:ec2-user /srv/%(project_name)s' % env)
    run('virtualenv --distribute env')

''' Git repository commands
'''
def upload_release():
    message('Creating an archive from the current Git master branch and uploading it ..', color=yellow)
    local('git archive --format=tar master | gzip > release.tar.gz')
    sudo('mkdir -p /srv/%(project_name)s/releases/%(release)s && chown -R ec2-user:ec2-user /srv/%(project_name)s' % env)
    put('release.tar.gz' % env , '/srv/%(project_name)s/releases/%(release)s.tar.gz' % env)
    run('cd /srv/%(project_name)s/releases/%(release)s && tar zxf /srv/%(project_name)s/releases/%(release)s.tar.gz' % env)
    run('rm /srv/%(project_name)s/releases/%(release)s.tar.gz' % env)
    