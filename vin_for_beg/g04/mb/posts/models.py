from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField(verbose_name = 'Сообщение')
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        #verbose_name_plural
    def __str__(self):
        return self.text[:50]

