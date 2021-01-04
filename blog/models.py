from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.author} : {self.title}'
