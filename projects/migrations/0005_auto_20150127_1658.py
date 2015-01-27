# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150127_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
