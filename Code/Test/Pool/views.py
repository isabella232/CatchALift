from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    a = open('H:\Git\CatchALift\Code\Test\Pool\Test.html', 'r')
    return HttpResponse(a.read())


