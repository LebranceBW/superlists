# from django.shortcuts import render
from django.http import HttpResponse
# from django.core.context_processors import request
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
# Create your views here.
