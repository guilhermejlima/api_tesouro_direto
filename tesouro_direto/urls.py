from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    url(r'^', include('tesouro_direto.tesouro.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view),

]






