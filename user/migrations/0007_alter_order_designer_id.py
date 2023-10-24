# Generated by Django 4.2.4 on 2023-10-24 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_order_designer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='designer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer_orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
