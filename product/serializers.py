from rest_framework import serializers
from .models import Product, History
from categories.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'quantity']

    @staticmethod
    def validate_category(value):
        try:
            return Category.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category does not exist.")

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = self.validate_category(category_name)
        validated_data['category'] = category
        return Product.objects.create(**validated_data)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['old_quantity', 'new_quantity', 'date_changed']


class ProductDetailSerializer(serializers.ModelSerializer):
    quantity_changes = HistorySerializer(many=True, read_only=True, source='history_set')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'quantity_changes']
