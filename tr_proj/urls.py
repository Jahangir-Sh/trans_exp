from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('tr.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
]
