# Generated by Django 4.2.1 on 2023-05-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_comment_branch'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
