from rest_framework import serializers
from web.models import Product


class ProductSerializer(serializers.ModelSerializer):
	"""
	Class with serializer entity Product
	"""
	
	# ModelSerializer are simply shortcut for creating serializer class
	# An automatically determined set of fields.
	# Simple default implementations for the create() and update() methods.
	class Meta:
		model = Product
		fields = ('id','name','description','measure','price')