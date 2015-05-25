# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relateddeleted', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='relateddeleted.Category'),
        ),
        migrations.AddField(
            model_name='news',
            name='new_category',
            field=models.ForeignKey(null=True, blank=True, to='relateddeleted.NewCategory'),
        ),
    ]
