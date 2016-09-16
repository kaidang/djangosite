from django.conf.urls import url

from blog.views import ArticlePublishView
from blog.views import ArticleListView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='blog_index'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
]