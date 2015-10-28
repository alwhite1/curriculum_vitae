# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usereducation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usereducation',
            old_name='name_id',
            new_name='user_id',
        ),
    ]
