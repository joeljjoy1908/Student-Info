# Generated by Django 2.2.3 on 2019-11-07 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_auto_20191107_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='course_name',
            new_name='course',
        ),
    ]
