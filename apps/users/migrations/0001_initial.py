# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('info', models.TextField()),
                ('city', models.CharField(max_length=32)),
                ('data_birth', models.DateField()),
                ('family', models.CharField(max_length=32)),
                ('phone_number', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('skype', models.CharField(max_length=16)),
            ],
        ),
    ]
