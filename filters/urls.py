from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from filters.views import FilterList, FilterDetail, CriteriaList, CriteriaDetail

urlpatterns = [
    url(r'^$', FilterList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', FilterDetail.as_view()),
    url(r'^criteria/$', CriteriaList.as_view()),
    url(r'^criteria/(?P<pk>[0-9]+)/$', CriteriaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
