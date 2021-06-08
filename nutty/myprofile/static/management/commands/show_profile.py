from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from myprofile.models import Profile


class Command(BaseCommand):
    help = 'show my profile'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs=1, type=int)

    def handle(self, *args, **options):
        print(args)
        print(options)
        try:

            id = options.get("id")[0]
            print(id)
            profile = Profile.objects.get(id=id)
            print(profile.name)
            # print(profile.short_bio)
        except Exception:
            raise CommandError("Error!")
