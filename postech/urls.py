"""postech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles import storage
from django.conf import settings
from django.conf.urls.static import static

from O2O.views import index, sign_up, login, file_upload, feedback_upload


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('O2O.urls')),
    url(r'^O2O/', include('O2O.urls')),
    url(r'^index$', index),
    url(r'^sign_up$', sign_up),
    url(r'^login$', login),
    url(r'^file_upload$', file_upload),
    url(r'^feedback_upload$', feedback_upload),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)