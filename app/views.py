from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def silk(request):
    return HttpResponse('<h1><marquee>We are not Talking about Diary Milk Silk</h1></marquee>')
