# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from django.db import migrations, models

from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    UserModel = get_user_model()

    UserModel.objects.create_superuser(
        username='admin',
        email='admin@admin.admin',
        password='admin',
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]

