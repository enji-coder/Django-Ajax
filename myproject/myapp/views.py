from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def index(request):
    data=User.objects.values()
    alldata=list(data)
    allproduct=Product.objects.all()
    context={
        'udata':alldata,
        'allproduct':allproduct,
    }
    return render(request,"myapp/index.html",{'context':context})

def register_user(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        uid=User.objects.create(name=name,email=email,contact=contact)
        res="Successfully added"
        status="save"
        data=User.objects.values()
        alldata=list(data)
        context={
            'status':status,
            'msg':res,
            'udata':alldata,
        }
        return JsonResponse({'context':context})
    else:
        res="Error - plz check data"
        status="error"
        data=User.objects.values()
        alldata=list(data)
        context={
            'status':status,
            'msg':res,
            'udata':alldata,
        }
        return JsonResponse({'context':context})
    
def search_user(request):
    name=request.POST['searchname']
    print(len(name))
    if len(name)!=0:
        print("---------------->",name)
        data=User.objects.filter(name=name)
        data=list(data.values())
        print("------------->",data)
        if data:
            status="result found"
        else:
            status="no result found"    
    else:
        data=User.objects.values()
        data=list(data)
        if data:
            status="result found"
        else:
            status="no result found"   
    context={
        'data':data,
        'status':status,
    }
    return JsonResponse({'context':context})

def del_user(request):
    id=request.POST['id']
    print("--------------->id",id)
    uid=User.objects.get(id=id)
    uid.delete()
    data=User.objects.values()
    data=list(data)
    return JsonResponse({'data':data})

def get_brand(request):
    name=request.POST['selected']
    print("------------->selected value ",name)
    pid=Product.objects.get(name=name)
    branddetails=Brand.objects.filter(pid=pid)
    data=list(branddetails.values())
    context={
        'data':data,
    }
    print("------------------------>context :",data)
    return JsonResponse({'context':context})

def javascript_validation_page(request):
    return render(request,'myapp/javascript_validation_register.html')