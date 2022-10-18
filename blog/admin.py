from django.contrib import admin

from .models.mongo_models import Comment
from .models.postgres_models import Post

admin.site.register(Post)
admin.site.register(Comment)

