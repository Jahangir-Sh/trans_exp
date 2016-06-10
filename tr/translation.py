from modeltranslation.translator import register, TranslationOptions
from tr.models import News


@register(News)
class NewsTranslator(TranslationOptions):
    fields = ('title', 'content')
