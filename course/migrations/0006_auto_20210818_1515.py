# Generated by Django 3.0.6 on 2021-08-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20210818_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='required',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
