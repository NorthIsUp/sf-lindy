# -*- coding: utf-8 -*-

from __future__ import absolute_import

# External Libraries
from path import path


SFLINDY_DIR = path(__file__).abspath().dirname()
PROJECT_ROOT = (SFLINDY_DIR / '..' / '..' / '..').abspath()
