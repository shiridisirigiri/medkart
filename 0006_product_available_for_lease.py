# Generated by Django 4.1.7 on 2023-05-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_for_lease',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
