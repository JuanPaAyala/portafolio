# Generated by Django 4.2.6 on 2023-10-12 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=90)),
                ('descripcion', models.CharField(max_length=2000)),
            ],
        ),
    ]
