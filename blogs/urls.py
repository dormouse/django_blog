from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blogs/
    url(r'^$', views.index, name='index'),
    # ex: /blogs/2/
    url(r'^(?P<entry_id>[0-9]+)/$', views.detail, name='detail'),
]
