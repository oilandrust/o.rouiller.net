# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subtitle',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
