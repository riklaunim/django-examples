# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('removing', '0003_auto_20150524_1933'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
