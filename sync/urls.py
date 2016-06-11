from django.conf.urls import url
from sync.views import SyncView

urlpatterns = [
    url(r'^$', SyncView.as_view(), name='sync'),
]
