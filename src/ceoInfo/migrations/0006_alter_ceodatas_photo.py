# Generated by Django 5.0.2 on 2024-03-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceoInfo', '0005_ceodatas_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceodatas',
            name='photo',
            field=models.FileField(upload_to='images/', verbose_name='Фото руководителя'),
        ),
    ]
