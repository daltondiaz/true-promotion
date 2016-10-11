from django.shortcuts import render
from rest_framework import viewsets
from web.models import Product
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

	"""
	This endpoint presents code API.

	"""

	queryset = Product.objects.all()
	serializer_class =  ProductSerializer
	
