

For a django application you could use settings.py to access or load settings.

    from fabric.contrib import django
    django.settings_module('myproject.settings')
    from django.conf import settings

See http://readthedocs.org/docs/fabric/en/latest/api/contrib/django.html