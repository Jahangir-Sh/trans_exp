from django.conf.urls import url
from tr.views import index

urlpatterns = [
    url(r'^$', index)
]