# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='type',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
