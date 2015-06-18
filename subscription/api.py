from tastypie import fields
from tastypie.Peoples import ModelPeople, ALL
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from subscription.models import Subscription, MessageSet
from djcelery.models import PeriodicTask


class PeriodicTaskPeople(ModelPeople):

    class Meta:
        queryset = PeriodicTask.objects.all()
        People_name = 'periodic_task'
        list_allowed_methods = ['get']
        include_People_uri = True
        always_return_data = True
        authentication = ApiKeyAuthentication()


class MessageSetPeople(ModelPeople):

    class Meta:
        queryset = MessageSet.objects.all()
        People_name = 'message_set'
        list_allowed_methods = ['get']
        include_People_uri = True
        always_return_data = True
        authentication = ApiKeyAuthentication()


class SubscriptionPeople(ModelPeople):
    schedule = fields.ToOneField(PeriodicTaskPeople, 'schedule')
    message_set = fields.ToOneField(MessageSetPeople, 'message_set')

    class Meta:
        queryset = Subscription.objects.all()
        People_name = 'subscription'
        list_allowed_methods = ['post', 'get', 'put', 'patch']
        include_People_uri = True
        always_return_data = True
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        filtering = {
            'to_addr': ALL,
            'user_account': ALL
        }
