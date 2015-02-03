# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150127_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='old',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
