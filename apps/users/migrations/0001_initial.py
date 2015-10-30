# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('organisation', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
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
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(max_length=32)),
                ('skills', models.TextField()),
                ('user', models.ForeignKey(to='users.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='userexperience',
            name='user',
            field=models.ForeignKey(to='users.UserInfo'),
        ),
        migrations.AddField(
            model_name='usereducation',
            name='user',
            field=models.ForeignKey(to='users.UserInfo'),
        ),
    ]
