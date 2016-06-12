from django.conf.urls import url
from core.views import HomeView
from core.views import gallery

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^gallery/$', gallery.gallery_list),
    url(r'^gallery/(?P<pk>[0-9]+)/$', gallery.gallery_detail),
]
