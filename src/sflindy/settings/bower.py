# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Module Local Library
from .env import PROJECT_ROOT

BOWER_COMPONENTS_ROOT = PROJECT_ROOT / 'vendor'

BOWER_INSTALLED_APPS = (
    'underscore',
    'react-bootstrap',
)
