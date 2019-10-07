from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('tesouro_direto.tesouro.urls')),
    url(r'^admin/', admin.site.urls),

]