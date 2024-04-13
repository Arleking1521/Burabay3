from django.db import models
import os
from django.utils import timezone
from logRegisPages.models import CustomUser

class PostCeo(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='Автор')
    title = models.CharField(max_length = 128, verbose_name='Title')
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField(verbose_name='Content')

    def __str__(self) -> str:
        return f'{self.title}: {self.content} ({self.date})'
# Create your models here.

class PostAttachment(models.Model):
    file = models.FileField(upload_to='images/')
    post = models.ForeignKey(PostCeo, on_delete=models.CASCADE)
    type = models.CharField(max_length = 6, blank=True, null=True )

    def save(self, *args, **kwargs):
        file_extension = self.file.name.split('.')[-1].lower()
        print(file_extension)
        if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
            self.type = 'img'
        else:
            self.type = 'doc'
        
        super().save(*args, **kwargs)