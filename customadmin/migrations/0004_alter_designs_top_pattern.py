# Generated by Django 4.2.4 on 2023-09-22 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0003_designs_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designs',
            name='top_pattern',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='top_pattern', to='customadmin.toppattern'),
        ),
    ]