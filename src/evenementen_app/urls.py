from django.conf.urls import url

from . import views

urlpatterns = [
    # URL for displaying the Main Page
    url(r'^$', views.index, name='EvenementenIndex'),
    # URL for displaying an Evenement
    url(r'^(?P<title_obj>[\w\-]+)/$', views.detailed, name='EvenementDetailed'),
    # URL to Sign Up for an Evenement
    url(r'^(?P<title_obj>[\w\-]+)/inschrijven/$', views.detailed, name='InschrijvenEvenement'),

]
