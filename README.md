Butler
======
Butler is for automating Python app deployments to AWS EC2.
Currently it installs everything on one machine. As the build process lasts about a minute it makes scaling up and down very simple.
It tries to be as easy as Heroku but you are in full control.


Quickstart
==========
1. Download this package to your disk.
2. cd to the download directory
3. Change the env.hosts and env.key_filename to reflect your own
4. fab build

This builds everything and you should soon have a working deployment.


Default stack
=====
* NGINX
* uWSGI
* MySQL
* Memcached


TODO
====
1.
* Apache installation and configuration
* Gunicorn installatiin and configuration
* Postgres installation and configuration
* Varnish installation and configuration

2.
* AWS instance spawning automation with Boto

3.
* Currently there is a default stack but this will change in the near future when you'll have the option of choosing your stack.
* Make it possible to deploy the DB and the application of separate machines with optional replication.
* Possibility of running a load balancer in front of your web servers. (HAproxy)
* Background workers with celery or redis queues

4.
* Build a optional UI for deployment and monitoring with stats from CloudWatch


Settings
========

For a django application you could use settings.py to access or load settings.

    from fabric.contrib import django
    django.settings_module('myproject.settings')
    from django.conf import settings

See http://readthedocs.org/docs/fabric/en/latest/api/contrib/django.html

Requirements
============

* Fabric - https://github.com/fabric/fabric by Christian Vest Hansen and Jeffrey E. Forcier
* git - http://git-scm.com/
* Boto - https://github.com/boto/boto by Mitch Garnaat