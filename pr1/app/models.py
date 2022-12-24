from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец статьи', blank = True, null = True )
    title = models.CharField('Имя человека:', max_length=50)
    full_text = models.TextField('Вид смерти:')
    date = models.DateTimeField('Дата смерти:')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
