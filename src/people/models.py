from django.db import models

# Create your models here.

class People(models.Model):
    name=models.CharField(max_length=128, verbose_name='ФИО')
    post = models.CharField(max_length=128, verbose_name='Должность')
    image = models.ImageField(upload_to='people/', verbose_name='Фото')
    director = models.BooleanField(verbose_name='Руководитель')
    doctor=models.BooleanField(verbose_name='Врач')
    teacher=models.BooleanField(verbose_name='Педагог')

    def __str__(self) -> str:
        return f'{self.name}'