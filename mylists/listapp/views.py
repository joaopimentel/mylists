from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from listapp.models import Link, Category


class LinkList(ListView):
    model = Link

    def get_queryset(self):
        """Order Links by date_added, desc."""
        return self.model.objects.filter(user=self.request.user)\
                                 .order_by('-date_added')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListView, self).dispatch(request, *args, **kwargs)


@login_required
def category_detail(request, tag=None):
    """Lists all Links from logged user tagged with given category.
    """
    link_list = Link.objects.select_related('category')\
                .filter(category__tag=tag,
                        user=request.user)
    t = loader.get_template('listapp/link_list.html')
    c = RequestContext(request, {
            'object_list': link_list,
    })
    return HttpResponse(t.render(c))


class CategoryList(ListView):
    model = Category

    def get_queryset(self):
        """Returns Categories for which the user has links, ordered by
        corresponding number of links."""
        return self.model.objects.select_related('link')\
                                 .filter(link__user=self.request.user)\
                                 .annotate(num_links=Count('link'))\
                                 .order_by('-num_links')\
                                 #.distinct()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListView, self).dispatch(request, *args, **kwargs)
