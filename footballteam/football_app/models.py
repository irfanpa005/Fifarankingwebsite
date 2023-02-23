from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    point = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
