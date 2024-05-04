from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/small')
    large_image = models.ImageField(upload_to='products/large')

    def __str__(self):
        return self.name

