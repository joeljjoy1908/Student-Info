# Generated by Django 2.2.3 on 2019-11-07 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_auto_20191107_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.Studentdetails'),
        ),
    ]
