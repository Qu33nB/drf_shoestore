# Generated by Django 3.0.7 on 2020-06-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoestore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoecolor',
            name='color_name',
            field=models.CharField(max_length=10),
        ),
    ]