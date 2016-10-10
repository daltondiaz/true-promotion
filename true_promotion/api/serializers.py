from rest_framework import serializers
from web.models import Product

class ProductSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	description = serializers.CharField(required=False, allow_blank=True)
	measure = serializers.CharField(required=True)
	price = serializers.FloatField()