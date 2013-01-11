from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import ListView
from listapp.models import Link


class LinkList(ListView):
    model = Link


def category_detail(request, tag=None):
    """Lists all Links tagged with given category.
    """
    link_list = Link.objects.select_related('category')\
                .filter(category__tag=tag)
    t = loader.get_template('listapp/link_list.html')
    c = RequestContext(request, {
            'object_list': link_list,
    })
    return HttpResponse(t.render(c))
