from django.conf.urls import url
from filter.views import FilterView

urlpatterns = [
    url(r'^$', FilterView.as_view(), name='sync'),
]
