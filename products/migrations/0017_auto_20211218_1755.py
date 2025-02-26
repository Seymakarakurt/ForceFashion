# Generated by Django 3.1.6 on 2023-01-03 15:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_review_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='helpful',
            field=models.ManyToManyField(blank=True, related_name='user_helpful', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='unhelpful',
            field=models.ManyToManyField(blank=True, related_name='user_unhelpful', to=settings.AUTH_USER_MODEL),
        ),
    ]
