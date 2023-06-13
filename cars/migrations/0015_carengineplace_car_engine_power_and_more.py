# Generated by Django 4.2.1 on 2023-06-13 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_alter_cardefect_image1_alter_cardefect_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarEnginePlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='engine_power',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardefect',
            name='image1',
            field=models.ImageField(upload_to='CarDefectImages'),
        ),
        migrations.AlterField(
            model_name='cardefect',
            name='image2',
            field=models.ImageField(upload_to='CarDefectImages'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.carengineplace'),
        ),
    ]
