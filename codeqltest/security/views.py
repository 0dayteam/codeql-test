from django.shortcuts import render
from django.http import HttpResponse

from django.template import  Context,Template

# Create your views here.

def ssti(request):
    template = Template("hello {name}".format(name=request.GET.get('name')))
    context = Context()
    return HttpResponse(template.render(context))
