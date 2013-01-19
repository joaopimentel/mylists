from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import utils


@login_required
def get_links(request):
    """View to manually fetch emails."""
    mailbox = request.user.userprofile.mailbox
    num_links = utils.fetchmails(mailbox)
    return HttpResponse('%d links created.' % num_links)
