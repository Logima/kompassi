# encoding: utf-8
from django.conf import settings
from django.core.management import call_command, get_commands
from django.core.management.base import BaseCommand, make_option


class Command(BaseCommand):
    args = ''
    help = 'Setup all the things'

    option_list = BaseCommand.option_list + (
        make_option('--test',
            action='store_true',
            dest='test',
            default=False,
            help='Setup all the things for testing'
        ),
    )

    def handle(self, *args, **options):
        test = options['test']

        commands = get_commands()
        events = [app_name.split(".")[-1] for app_name in settings.INSTALLED_APPS if app_name.startswith("events.")]
        event_commands = [command for command in ("setup_%s" % event for event in events) if command in commands]

        management_commands = [
            (('collectstatic',), dict(interactive=False)),
            (('migrate',), dict()),
            (('setup_core',), dict(test=test)),
            (('setup_labour_common_qualifications',), dict(test=test)),
            (('setup_api_v2',), dict(test=test)),
            (('setup_access',), dict(test=test)),
        ] + [((command,), dict(test=test)) for command in event_commands]

        if test:
            management_commands.extend((
                (('test', 'core', 'labour', 'labour_common_qualifications', 'programme', 'tickets'), dict()),
                (('behave',), dict()),
            ))

        for pargs, opts in management_commands:
            call_command(*pargs, **opts)
