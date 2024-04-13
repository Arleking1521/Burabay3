from django.contrib import admin
from .models import PostCeo
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(PostCeo)
class PostAdmin(TranslationAdmin):
    list_display = ( 'title', 'content', 'date')
    fields = ('author', 'title', 'date', 'content')