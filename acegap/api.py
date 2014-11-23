from tastypie.models import ApiKey
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.resources import ModelResource

from django.contrib.auth import get_user_model

User = get_user_model()

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		fields = ["first_name", "last_name", "email", "username"]
		allowed_method = ['get']
		resource_name = 'user'
		authorization = DjangoAuthorization()
		authentication = BasicAuthentication()

	def dehydrate(self, bundle):
		print(bundle.data)
		username = bundle.data.get('username')
		bundle.data['api_key'] = "Hello %s" % (username)
		return bundle
