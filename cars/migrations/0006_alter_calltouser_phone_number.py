# Generated by Django 4.2.1 on 2023-07-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_calltouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltouser',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]