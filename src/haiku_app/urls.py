from django.conf.urls import url

from . import views

urlpatterns = [
    # URL for displaying the HomePage
    url(r'^$', views.index, name='HomePage'),
    # URL for displaying any page from the Haiku Model, DetailedPage
    url(r'^content/(?P<title_obj>[\w\-]+)/$', views.detailed, name='DetailedPage'),
]
