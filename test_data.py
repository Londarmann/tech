import os
import random

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from categories.models import Category
from product.models import Product


def test_data():
    categories_data = [
        {"name": "Electronics", "description": "Smartphones and other stuff"},
        {"name": "Clothing", "description": "t-shirts"},
        {"name": "Books", "description": "Dostoevski, Strugatsky, etc"},
        {"name": "Home Decor", "description": "Decoration items for home"},
        {"name": "Sports & Fitness", "description": "Equipment and gear for sports and fitness"}
    ]
    categories = []
    for category_data in categories_data:
        category = Category.objects.create(**category_data)
        categories.append(category)

    for category in categories:
        for i in range(1, 11):
            product_name = f"{category.name} Product {i}"
            product_description = f"Description for {category.name} Product {i}"
            product_price = round(random.uniform(10, 1000))
            product_quantity = random.randint(10, 100)
            Product.objects.create(
                name=product_name,
                description=product_description,
                price=product_price,
                quantity=product_quantity,
                category=category
            )
