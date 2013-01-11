from django.views.generic import ListView
from listapp.models import Link


class LinkList(ListView):
    model = Link
