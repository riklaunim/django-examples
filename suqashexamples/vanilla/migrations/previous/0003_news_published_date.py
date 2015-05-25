# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vanilla', '0002_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 24, 17, 26, 25, 326059, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
