from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from listapp.models import Link


class LinkList(ListView):
    model = Link

    def get_queryset(self):
        """Order Links by date_added, desc."""
        return self.model.objects.order_by('-date_added')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListView, self).dispatch(request, *args, **kwargs)


@login_required
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
