from django.conf.urls import url
from . import views

app_name = 'commande'
urlpatterns = [
    url(r'^$', views.index,name='index')
    # url(r'^$', views.IndexView.as_view(),name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='commande'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='admin'),
]
