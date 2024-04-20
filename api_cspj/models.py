# myapp/models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Specify the app_label for the model
        app_label = 'api_cspj'