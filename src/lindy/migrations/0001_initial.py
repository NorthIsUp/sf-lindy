# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('profile', markupfield.fields.MarkupField(rendered_field=True)),
                ('profile_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown')], max_length=30, editable=False, default='markdown')),
                ('_profile_rendered', models.TextField(editable=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
