# Generated by Django 4.1.2 on 2024-07-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_user_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicehascart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
