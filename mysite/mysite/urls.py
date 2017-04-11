""" ..\..\PycharmEnv\djangobook2\Scripts\activate

mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from profiles import views as profiles_views
from photo import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.HomeTV.as_view(), name='home'),
    url(r'^about$', profiles_views.AboutTV.as_view(), name='about'),
    url(r'^profile/', profiles_views.userProfile, name='profile'),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^photo/', include('photo.urls', namespace='photo')),

    #url(r'^$', views.home, name='home'),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # static/static-only
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # static/media