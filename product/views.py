from django.shortcuts import render

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet



class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer