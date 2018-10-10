from tastypie.resources import ModelResource
from .models import User, Device, Event, Media

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        resource_name = 'media'
class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'device'
class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'