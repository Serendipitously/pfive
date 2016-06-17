from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import HomeView
from core.views import GalleryList, GalleryDetail

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^gallery/$', GalleryList.as_view()),
    url(r'^gallery/(?P<pk>[0-9]+)/$', GalleryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
