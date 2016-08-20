from django.shortcuts import render
#from django.http import HttpResponse
# from django.core.context_processors import request
def home_page(request):
    return render(request,'home.html')
# Create your views here.
