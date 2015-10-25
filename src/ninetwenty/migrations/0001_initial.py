# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import migrations, models

from lindy.models import Teacher


def create_users(apps, schema_editor):
    UserModel = get_user_model()

    for user in (
        {
            'username':'ann',
            'email':'ann.mony@gmail.com',
            'first_name': 'ann',
            'last_name': 'mony',
        },
        {
            'username': 'adam',
            'email': 'adam@northisup.com',
            'first_name': 'adam',
            'last_name': 'hitchcock',
        },
        {
            'username': 'ryan',
            'email': 'ryan@wherever',
            'first_name': 'ryan',
            'last_name': 'calloway',
        },
    ):
        UserModel.objects.get_or_create(**user)

    for teacher in (
        {
            'username': 'ann',
            'profile': (
                '* hi\n'
                '* ho\n'
                '* silver\n'
                '\n'
                '# header\n'
            )
        },
        {
            'username': 'ryan',
            'profile': (
                '* hi\n'
                '* ho\n'
                '* silver\n'
                '\n'
                '# header\n'
            )
        },
    ):
        user = UserModel.objects.get(
            username=teacher.pop('username')
        )
        Teacher.objects.get_or_create(
            user=user,
            **teacher
        )

class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(create_users),
    ]

