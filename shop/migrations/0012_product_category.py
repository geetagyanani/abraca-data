# Generated by Django 2.1.5 on 2020-06-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200615_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
