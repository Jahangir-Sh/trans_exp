from django.contrib import admin
from django.contrib.admin.decorators import register
from modeltranslation.admin import TranslationAdmin

from tr.models import News


@register(News)
class NewsAdmin(TranslationAdmin):
    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
