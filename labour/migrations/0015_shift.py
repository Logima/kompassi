# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0014_auto_20151108_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('hours', models.PositiveIntegerField()),
                ('notes', models.TextField()),
                ('job', models.ForeignKey(to='labour.Job')),
                ('signup', models.ForeignKey(to='labour.Signup')),
            ],
            options={
                'verbose_name': 'ty\xf6vuoro',
                'verbose_name_plural': 'ty\xf6vuorot',
            },
        ),
    ]
