from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Bag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True)
    coupon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username + ' ordered ' + self.item.name
