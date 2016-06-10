from django.shortcuts import render_to_response
from django.template.context_processors import csrf


def index(request):
    return render_to_response('index.html', csrf(request))
