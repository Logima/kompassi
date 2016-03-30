# encoding: utf-8

from __future__ import unicode_literals

from activity.models import Registry


registry = Registry('core')

registry.declare_activity(
    'logged_in',
    'You logged in from {{ ip_address }}.',
    '{{ target_user.get_full_name }} logged in from {{ ip_address }}.',
)

registry.declare_activity(
    'logged_out',
    'You logged out.',
    '{{ target_user.get_full_name }} logged out.',
)

registry.declare_activity(
    'signed_up',
    'You signed up.',
    '{{ target_user.get_full_name }} signed up.',
)
