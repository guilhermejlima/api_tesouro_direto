from django.conf.urls import url

from tesouro_direto.tesouro import views

urlpatterns = [
    url(r'^titulos/$', views.TituloViewSet.as_view(), name='titulos'),

]