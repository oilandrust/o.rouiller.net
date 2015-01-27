# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
