from django.conf.urls import url

from tesouro_direto.tesouro.Domain import services

urlpatterns = [
    url(r'^titulos/$', services.TituloList.as_view(), name='titulo-list'),
    url(r'^titulo/(?P<pk>[0-9]+)/$', services.TituloDetail.as_view(), name='titulo-detail'),

]