from rest_framework import serializers, permissions


from .models import Category



class CategoryListSerializer(serializers.ModelSerializer):
    brief_description = serializers.SerializerMethodField()
    number_of_products = serializers.SerializerMethodField()

    def get_brief_description(self, obj):
        return obj.description[:100] if obj.description else ''

    def get_number_of_products(self, obj):
        return obj.product_set.count()

    class Meta:
        model = Category
        fields = ['id', 'name', 'brief_description', 'number_of_products']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']