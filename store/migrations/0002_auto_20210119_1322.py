# Generated by Django 3.1.5 on 2021-01-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
