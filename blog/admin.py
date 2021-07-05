from django.contrib import admin
from .models import blogpost, CommentModel

# Register your models here.
admin.site.register(blogpost)
admin.site.register(CommentModel)