# encoding: utf-8

from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models


app_label_params = dict(NONUNIQUE_SLUG_FIELD_PARAMS,
    verbose_name=_('app label'),
    help_text=_('Indicates the application this entry type belongs to.'),
)


EMPTY_PAYLOAD = dict(
    type="object",
    properties=dict(),
)


class Registry(object):
    def __init__(self, app_label):
        self.app_label = app_label
        self.entry_type_descriptors = []

    def declare_activity(self, key, template_you, template_other, payload_schema=EMPTY_PAYLOAD):
        self.entry_type_descriptors.append(EntryTypeDescriptor(

        ))


class EntryType(models.Model):
    app_label = models.CharField(**app_label_params)
    key = models.CharField(**key_params)

    template_you = models.TextField()
    template_other = models.TextField()

    payload_schema = JSONField()

    is_visible_to_app_admin = models.BooleanField(default=True)
    is_visible_to_target_user = models.BooleanField(default=True)


class Entry(models.Model):
    organization = models.ForeignKey('core.Organization')
    event = models.ForeignKey('core.event')
    entry_type = models.ForeignKey(EntryType)
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='+')
    payload_json = JSONField(blank=True, default=dict)

    def clean_payload_json():


    class Meta:
        index_together = [
            ('organization', 'created_at'),
            ('event', 'created_at'),
            ('target_user', 'created_at'),
        ]

        ordering = ('created_at',)
