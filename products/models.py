from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products"
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    pdf = models.FileField(upload_to="products-pdf/", blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_products",
        blank=True,
        null=True,
    )

    @property
    def rating(self):
        return self.product_reviews.aggregate(Avg("rating"))["rating__avg"]

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reviews"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_reviews"
    )
    body = models.TextField()
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
    )
    helpful = models.ManyToManyField(User, blank=True, related_name="user_helpful")
    unhelpful = models.ManyToManyField(User, blank=True, related_name="user_unhelpful")
    report = models.ManyToManyField(User, blank=True, related_name="user_report")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.rating}"

    class Meta:
        unique_together = ("user", "product")
