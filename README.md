===============================
sflindy
===============================

.. image:: https://img.shields.io/travis/NorthIsUp/sf-lindy.svg
        :target: https://travis-ci.org/NorthIsUp/sf-lindy

.. image:: https://img.shields.io/pypi/v/sf-lindy.svg
        :target: https://pypi.python.org/pypi/sf-lindy


SF Lindy portal site

* Free software: BSD license
* Documentation: https://sflindy.readthedocs.org.

Features
--------

* TODO

Contributing
============

#### Dev environment
- python 3.5 (I know it's' like the future)
- Docker

To set up with docker you simply run:

```
$ docker-compose up
```

To setup a local environment run:
```
$ pyvenv ~/.virtualenvs/sflindy
$ source ~/.virtualenvs/sflindy/bin/activate # or workon sflind if you have virtualenvwrapper installed
$ pip install -r requirements.txt
$ DJANGO_SETTINGS_MODULE=sflindy.settings python manage.py runserver
```

#### Style
- Use flake8/autopep8 before committing code, pep8 rules are configured in setup.py
- Use isort to keep imports in order, isort rules are configured in setup.py
- Use py.test, not unittest, for all tests
- Google Style doc strings
- Model names should not be plural
- use [fit-commit](https://github.com/m1foley/fit-commit) for git messages (this one is very hard for me...)

[![Build Status](https://travis-ci.org/NorthIsUp/sf-lindy.svg?branch=master)](https://travis-ci.org/NorthIsUp/sf-lindy)
