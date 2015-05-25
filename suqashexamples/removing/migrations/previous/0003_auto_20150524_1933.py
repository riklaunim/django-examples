# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def foo(*args, **kwargs):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('removing', '0002_auto_20150524_1933'),
    ]

    operations = [
        migrations.RunPython(foo)
    ]
