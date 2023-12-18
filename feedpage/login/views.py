from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import usersForm
from registermod.models import Registermod

def form(request):
    f=usersForm()
    data1={'f':f,
          
          }
    x=''
    try:
        if request.method=="POST":
            uname=request.POST.get('uname')
            #c=Registermod(fn=uname)
            a=Registermod.objects.all()
            for i in a:
                if i.fn==uname:
                    url='feedpage/'
                    return HttpResponseRedirect(url)
                # elif i.fn!=uname:
                #     x='Invalid User Name'
                #     data1+={'x':x}                         
    except:
        pass
    return render(request,"login.html",data1)

# def registerinformation(request):
#     n=''
#     if request.method=="POST":
#         name=request.POST.get('name')
#         comment=request.POST.get('comment')
#         com=Comment1(comment1_n=name,comment1_d=comment)
#         com.save()
#         n="Comment inserted successfully"
#     return render(request,"feedpage.html",{'n':n}) 
# Create your views here.
