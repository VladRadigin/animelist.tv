from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from django.template import loader

def index(request):
    template = loader.get_template('myList/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
