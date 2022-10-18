from django.db import models
from djongo import models as mongo_models

from .postgres_models import Post


class Comment(models.Model):
    _id = mongo_models.ObjectIdField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        _db = 'nonrel'
        ordering = ("-created_at", )

    def __str__(self):
        return self.message
