from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    '''Модель темы'''
    topic = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Возвращает строковое представление'''
        return self.topic


class Comments(models.Model):
    '''Комментарий пользователя'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Возвращает строковое представление'''
        return self.comment
