from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    '''Topic model'''
    topic = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Returns a string representation'''
        return self.topic


class Comments(models.Model):
    '''User's comment'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Returns a string representation'''
        return self.comment
