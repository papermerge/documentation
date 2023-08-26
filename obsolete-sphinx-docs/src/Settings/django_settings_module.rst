Django Settings Module
======================

|project| is written in `Django Web Framework`_. When you use Django, you have to tell it which settings you’re using. Do this
by using an environment variable, DJANGO_SETTINGS_MODULE.


``DJANGO_SETTINGS_MODULE``
--------------------------

The value of DJANGO_SETTINGS_MODULE should be in Python path syntax, e.g.
mysite.settings. Note that the settings module should be on the Python import
search path.
This value is Django specific and can be passed only as environment
variable.
For |project|::

    DJANGO_SETTINGS_MODULE=config.settings


.. _Django Web Framework: https://www.djangoproject.com/