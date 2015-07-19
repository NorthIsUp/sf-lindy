# -*- coding: utf-8 -*-

from __future__ import absolute_import

# External Libraries
from django.shortcuts import render


def index(request):
    render(request, 'index.html')
