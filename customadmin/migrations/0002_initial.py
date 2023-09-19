# Generated by Django 4.2.4 on 2023-09-18 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customadmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='designs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bottompattern',
            name='dress_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customadmin.dresstype'),
        ),
    ]