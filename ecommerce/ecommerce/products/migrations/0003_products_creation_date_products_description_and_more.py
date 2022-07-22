# Generated by Django 4.0.6 on 2022-07-22 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='creation_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
