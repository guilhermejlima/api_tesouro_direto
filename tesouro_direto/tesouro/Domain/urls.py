from django.conf.urls import url

from tesouro_direto.tesouro.Domain import views

urlpatterns = [
    url(r'^titulos/$', views.TituloList.as_view(), name='titulo-list'),
    url(r'^titulo/(?P<pk>[0-9]+)/$', views.TituloDetail.as_view(), name='titulo-detail'),

]