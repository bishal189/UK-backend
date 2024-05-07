from django.db import models
from store.models import Product
# Create your models here.

class Review(models.Model):
    name=models.TextField()
    email=models.TextField()
    review_title=models.TextField(blank=True,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_content=models.TextField()
    created_at=models.DateField(auto_now_add=True)



