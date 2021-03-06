# encoding: utf-8



from django.db.models import Q
from django.shortcuts import render
from django.utils.timezone import now

from core.utils import groups_of_n, groupby_strict

from ..models import Event, Organization


def get_year(event):
    return event.start_time.year


def events(*args, **kwargs):
    return (
        Event.objects.filter(*args, **kwargs)
            .order_by('-start_time')
            .select_related('venue')
            .select_related('enrollmenteventmeta')
            .select_related('ticketseventmeta')
            .select_related('laboureventmeta')
            .select_related('programmeeventmeta')
    )


def core_frontpage_view(request):
    t = now()

    past_events = events(public=True, end_time__lte=t)
    current_events = events(public=True, start_time__lte=t, end_time__gt=t)
    future_events = events((Q(start_time__gt=t) | Q(start_time__isnull=True)) & Q(public=True)).order_by('start_time')

    organizations = Organization.objects.filter(public=True)

    past_events_rows_by_year = [(year, list(groups_of_n(year_events, 4))) for (year, year_events) in groupby_strict(past_events, get_year)]

    vars = dict(
        future_events_rows=list(groups_of_n(future_events, 4)),
        current_events_rows=list(groups_of_n(current_events, 4)),
        past_events_rows_by_year=past_events_rows_by_year,
        organizations_rows = list(groups_of_n(organizations, 4)),
    )

    return render(request, 'core_frontpage_view.jade', vars)
