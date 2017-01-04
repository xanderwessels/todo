from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'new/', views.new, name='new'),
    url(r'archived/',views.archived, name='archived'),
    url(r'^archive/(?P<id>\d+)/$', views.archive, name='archive'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]