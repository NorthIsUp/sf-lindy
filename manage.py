#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Standard Library
import sys
from os import path


sys.path.insert(0, path.abspath('./src'))

if __name__ == '__main__':
    from sflindy.manage import main

    main()
