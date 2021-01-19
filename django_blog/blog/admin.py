from django.contrib import admin
from .models import ArticleModel

# Register your models here.


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    """
    docstring
    """
    list_display = ('title', 'author', 'creation_date')
