# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151027_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('organisation', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('user_id', models.OneToOneField(to='users.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(max_length=32)),
                ('skill', models.TextField()),
                ('user_id', models.OneToOneField(to='users.UserInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='user_id',
            field=models.OneToOneField(to='users.UserInfo'),
        ),
    ]
