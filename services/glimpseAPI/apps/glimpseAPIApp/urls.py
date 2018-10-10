from django.conf.urls import url, include
from . import views, models, resources
from .resources import UserResource, MediaResource, DeviceResource, EventResource

user_resource = UserResource()
media_resource = MediaResource()
device_resource = DeviceResource()
event_resource = EventResource()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^media$', views.mediaHome),
    url(r'^media/getAllImages$', views.getAllImages),
    url(r'^media/getAllVideos$', views.getAllVideos),
    url(r'^media/getAllUserImages/(?P<user_id>\d+)$', views.getAllUserImages),
    url(r'^media/getAllUserVideos/(?P<user_id>\d+)$', views.getAllUserVideos),
    url(r'^media/getAllEvents$', views.getAllEvents),
    url(r'^media/getSpecificEvent/(?P<event_id>\d+)$', views.getSpecificEvent),
    url(r'^media/getSpecificEvent/(?P<event_id>\d+)$', views.getSpecificEvent),
    url(r'^media/getAllImagesUserEvent/(?P<user_id>\d+)/(?P<event_id>\d+)$', views.getAllImagesUserEvent),
    url(r'^media/getAllVideosUserEvent/(?P<user_id>\d+)/(?P<event_id>\d+)$', views.getAllVideosUserEvent),
    url(r'^media/updateDatabase$', views.updateDatabase),
    url(r'^media/getMedia', include(media_resource.urls)),
    url(r'^media/getUser', include(user_resource.urls)),
    url(r'^media/getEvent', include(event_resource.urls)),
    url(r'^media/getDevice', include(device_resource.urls))
]  