from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'new/', views.new, name='new'),
    url(r'archived/',views.archived, name='archived'),
    url(r'^archive/(?P<id>\d+)/$', views.archive, name='archive'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/v1/items/$', views.item_collection, name='item_collection'),
    url(r'api/v1/items/(?P<pk>[0-9]+)$', views.item_element, name='item_element'),
]