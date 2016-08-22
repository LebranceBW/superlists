from django.shortcuts import render
from lists.models import Item,List
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
def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    return render(request,'list.html',{'list':list_})
def new_list(request):
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return  HttpResponseRedirect('/lists/%d/'%(list_.id,))
def add_item(request,list_id):
    list_=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return  HttpResponseRedirect('/lists/%d/'%(list_.id,))
