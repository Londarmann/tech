from datetime import datetime

from django.db import models

from django.core.validators import MinLengthValidator

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50,
                            validators=[MinLengthValidator(5, message="Product should be at least 5 charactes")])
    description = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the object is being updated
            old_product = Product.objects.get(pk=self.pk)
            if old_product.quantity != self.quantity:
                History.objects.create(
                    product=self,
                    old_quantity=old_product.quantity,
                    new_quantity=self.quantity,
                    date_changed=datetime.now()
                )
        super().save(*args, **kwargs)


class History(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    date_changed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.date_changed}"
