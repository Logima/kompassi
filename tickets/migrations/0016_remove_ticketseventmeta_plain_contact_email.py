# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_auto_20160608_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketseventmeta',
            name='plain_contact_email',
        ),
    ]
