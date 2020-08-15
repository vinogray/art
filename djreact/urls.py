
from django.contrib import admin

from django.conf.urls import include, url

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
    url('api/', include('articles.api.urls'))
]
