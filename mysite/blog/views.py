from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

#def blog_index(request):
#   return HttpResponse("Hello, world.您好,欢迎!")

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.views.generic.list import ListView


from blog.models import Article

class ArticleListView(ListView):
    template_name = 'blog_index.html'

    def get_queryset(self, **kwargs):
        object_list = Article.objects.all().order_by(F('created').desc())[:100]
        paginator = Paginator(object_list, 10)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            object_list = paginator.page(paginator.num_pages)
        return object_list


from django.views.generic.edit import FormView

from blog.forms import ArticlePublishForm


class ArticlePublishView(FormView):
    template_name = 'article_publish.html'
    form_class = ArticlePublishForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(ArticlePublishView, self).form_valid(form)