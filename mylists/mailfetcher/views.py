from django.http import HttpResponse

from models import MailBox
import utils


def get_links(request):
    """View to manually fetch emails."""
    mailbox = MailBox.objects.all()[0]
    num_links = utils.fetchmails(mailbox)
    return HttpResponse('%d links created.' % num_links)
