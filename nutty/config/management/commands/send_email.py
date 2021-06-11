from django.core.management.base import BaseCommand, CommandError
from myprofile.models import Subscriberlist
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'send email to my subcriber'

    def send_email_subscriber(self, subscriberlist):
        try:
            send_mail(
                'Thankyou for Subscribe',
                'Hope you enjoy.',
                'nutsrk@odds.team',
                subscriberlist,
                fail_silently=False,
            )
        except Exception as e:
            raise CommandError(e)

    def handle(self, *args, **options):
        subscriberlist = Subscriberlist.objects.all()
        emaillist = []
        for sub in subscriberlist:
            emaillist.append(sub.email)
        self.send_email_subscriber(emaillist)
