from django.shortcuts import render
from lists.models import Item
#from django.contrib.redirects.models import Redirect
from django.http import HttpResponseRedirect
#from django.http import HttpResponse
# from django.core.context_processors import request
def home_page(request):
#     if request.method=='POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return  HttpResponseRedirect('/lists/the_only_list_in_the_world/')
    return render(request,'home.html')
#     items=Item.objects.all()
#     return render(request,'home.html',{'items':items})
# Create your views here.
def view_list(request):
    items=Item.objects.all()
    return render(request,'list.html',{'items':items})
def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return  HttpResponseRedirect('/lists/the_only_list_in_the_world/')
