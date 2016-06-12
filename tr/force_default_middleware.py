class ForceDefaultLanguageMiddleware(object):
    def process_request(self, request):
        if request.META.get('HTTP_ACCEPT_LANGUAGE'):
            del request.META['HTTP_ACCEPT_LANGUAGE']
