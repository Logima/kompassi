# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('core', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsEventMeta',
            fields=[
                ('event', models.OneToOneField(related_name='paymentseventmeta', primary_key=True, serialize=False, to='core.Event')),
                ('checkout_password', models.CharField(max_length=255)),
                ('checkout_merchant', models.CharField(max_length=255)),
                ('checkout_delivery_date', models.CharField(max_length=9)),
                ('admin_group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'verbose_name': 'tapahtuman maksunv\xe4litystiedot',
                'verbose_name_plural': 'tapahtuman maksunv\xe4litystiedot',
            },
            bases=(models.Model,),
        ),
    ]
