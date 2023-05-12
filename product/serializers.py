from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class ChildCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name",)


class ChildProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    child_category_obj = ChildCategorySerializer(source='child_product',
                                                 many=True, read_only=True)
    product_obj = ChildProductSerializer(source='product_relate',
                                         many=True, read_only=True)

    class Meta:
        model = Category
        fields = "id", "name", "parent", "child_category_obj", "product_obj",


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"