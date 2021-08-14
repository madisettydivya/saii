from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_hello(request):
    return HttpResponse('app2_hello is a view function')