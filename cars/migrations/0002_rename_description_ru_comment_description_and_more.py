# Generated by Django 4.2.1 on 2023-06-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description_ru',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='description_uz',
        ),
    ]