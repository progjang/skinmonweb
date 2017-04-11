from django.conf.urls import url

from . import views
from .views import HomeTV, AboutTV

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    #url(r'^$', HomeTV.as_view(), name='home'),
    #url(r'^about/$', AboutTV.as_view(), name='about'),
    #url(r'^$', HomeTV.as_view(), name='home'),

]