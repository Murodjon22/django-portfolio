from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    data = models.DateTimeField()


    def __str__(self):
        return self.title