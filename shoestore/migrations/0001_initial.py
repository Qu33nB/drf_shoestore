# Generated by Django 3.0.7 on 2020-06-17 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('RED', 'Red'), ('ORG', 'Orange'), ('YLW', 'Yellow'), ('GRN', 'Green'), ('BLU', 'Blue'), ('IND', 'Indigo'), ('VLT', 'Violet'), ('WHT', 'White'), ('BLK', 'Black')], default='RED', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('fasten_type', models.CharField(max_length=50)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shoestore.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='shoestore.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoe_type', to='shoestore.ShoeType')),
            ],
        ),
    ]
