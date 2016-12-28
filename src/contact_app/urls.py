from django.conf.urls import url

from . import views


app_name = 'contact_app'
urlpatterns = [
    url(r'^$', views.contact, name='contact'),
]
