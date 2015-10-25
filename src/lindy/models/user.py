# -*- coding: utf-8 -*-
from __future__ import absolute_import

# External Libraries
from django.contrib.auth.models import User
from django.db import models
from markupfield.fields import MarkupField


class Teacher(models.Model):
    user = models.ForeignKey(User)
    profile = MarkupField(markup_type='markdown')
    avatar = models.URLField(default='')

    def __str__(self):
        return self.user.get_full_name() or self.user.username
