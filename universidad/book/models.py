from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50)
    create_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
