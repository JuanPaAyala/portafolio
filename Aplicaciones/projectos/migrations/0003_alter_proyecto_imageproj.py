# Generated by Django 4.2.1 on 2023-10-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectos', '0002_proyecto_date_proyecto_imageproj_proyecto_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imageproj',
            field=models.FileField(null=True, upload_to='projects/'),
        ),
    ]
