from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include('haiku_app.urls')),
    url(r'^evenementen/', include('evenementen_app.urls')),
    url(r'^a/site/', admin.site.urls),
]
