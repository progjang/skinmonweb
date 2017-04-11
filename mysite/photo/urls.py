from django.conf.urls import url
from photo.views import *

urlpatterns = [
	# Example: /
	url(r'^$',AlbumLV.as_view(), name='index'),

	# /album/, same as /
	url(r'^album/$', AlbumLV.as_view(), name='album_list'),

	# /album/10/
	url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

	# /photo/10/
	url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
]