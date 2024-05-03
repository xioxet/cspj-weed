# models.py
from django.db import models

class Comment(models.Model):
    text = models.TextField()
    user = models.TextField()

    def __str__(self):
        return f'Comment: {self.text}'
    
    class Meta:
        app_label = 'polls'
