# Generated by Django 2.2.3 on 2019-11-07 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
