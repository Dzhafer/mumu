from django.db import models

# Create your models here.

#verbose_name_plural = 'Объявления'
#verbose_name = 'Объявление'

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name = 'Автор',)
    body = models.TextField(verbose_name = 'Тело сообщения')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Сообщение блога'
        verbose_name_plural = 'Сообщения блога'