# Generated by Django 4.1.7 on 2023-05-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_lease_explanations_alter_lease_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lease',
            name='explanations',
        ),
    ]