# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('institution', models.TextField()),
                ('speciality', models.TextField()),
                ('name_id', models.ForeignKey(to='users.UserInfo')),
            ],
        ),
    ]
