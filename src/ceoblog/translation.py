from modeltranslation.translator import register, TranslationOptions
from .models import PostCeo

@register(PostCeo)
class PostTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')