from django.contrib import admin
from .models import People
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(People)
class PeopleAdmin(TranslationAdmin):
    list_display = ( 'post',)