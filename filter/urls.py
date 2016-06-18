from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from filter.views import FilterView, FilterList, FilterDetail

urlpatterns = [
    url(r'^$', FilterView.as_view(), name='filter'),
	url(r'^all/$', FilterList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', FilterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
