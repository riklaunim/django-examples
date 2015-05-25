# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('removing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='newperson',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
