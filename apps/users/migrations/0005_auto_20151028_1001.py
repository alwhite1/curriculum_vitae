# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151028_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userskill',
            old_name='skill',
            new_name='skills',
        ),
    ]
