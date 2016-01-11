# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150203_1233'),
        ('blog', '0004_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.ForeignKey(to='projects.Project', null=True),
            preserve_default=True,
        ),
    ]
