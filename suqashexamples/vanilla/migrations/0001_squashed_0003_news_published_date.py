# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    replaces = [('vanilla', '0001_initial'), ('vanilla', '0002_news_text'), ('vanilla', '0003_news_published_date')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField(default='')),
                ('published_date', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 24, 17, 26, 25, 326059, tzinfo=utc))),
            ],
        ),
    ]
