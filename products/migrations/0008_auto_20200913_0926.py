# Generated by Django 3.1.6 on 2023-01-03 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_best_selling_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Best_selling_product',
            new_name='Top_selling_product',
        ),
    ]
