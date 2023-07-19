from django.db import models
from products.models import Product

class Translation(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('JA', 'Japanese'),
        ('DE', 'German'),
        ('IT', 'Italian'),
        ('ES', 'Spanish'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        unique_together = ('product', 'language')

    def __str__(self):
        return f'{self.product.title} ({self.get_language_display()})'
