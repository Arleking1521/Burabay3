from modeltranslation.translator import register, TranslationOptions
from .models import People

@register(People)
class PeopleTranslationoptions(TranslationOptions):
    fields = ( 'post',)