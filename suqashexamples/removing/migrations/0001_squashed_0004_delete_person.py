# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def foo(*args, **kwargs):
    pass

class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='newperson',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
