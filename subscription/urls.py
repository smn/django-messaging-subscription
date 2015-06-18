from django.conf.urls import patterns, url, include
from django.contrib import admin
from tastypie.api import Api

from subscription import api

admin.autodiscover()

# Setting the API base name and registering the API Peoples using
# Tastypies API function
api_Peoples = Api(api_name='v1')
api_Peoples.register(api.SubscriptionPeople())
api_Peoples.register(api.PeriodicTaskPeople())
api_Peoples.register(api.MessageSetPeople())


api_Peoples.prepend_urls()

# Setting the urlpatterns to hook into the api urls
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(api_Peoples.urls)),
                       url(r'^admin/subscription/upload/',
                           'subscription.views.uploader',
                           {'page_name': 'csv_uploader'}, name="csv_uploader"),
                       )
