from django.http import HttpResponse
from django.shortcuts import render
from comment1.models import Comment1
from django.core.paginator import Paginator
from registermod.models import Registermod
def mainpage(request):
    comment1Data=Comment1.objects.all()
    paginator1=Paginator(comment1Data,6)
    page_number=request.GET.get('page')
    Comment1Datafinal=paginator1.get_page(page_number)
    if request.method=="GET":
        st=request.GET.get('comment1n')
        r=request.GET.get('r')
        if st!=None:
            Comment1Datafinal=Comment1.objects.filter(comment1_d__icontains=st)[:6]
        
        if r=="1":
            Comment1Datafinal=Comment1.objects.all().order_by('comment1_n')[:6]
        elif r=="2":
            Comment1Datafinal=Comment1.objects.all().order_by('-comment1_n')[:6] 
        data={
        #'comment1Data':comment1Data,
        'Comment1Datafinal':Comment1Datafinal,
    }
    return render(request,"feedpage.html",data)
def savecomment(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        comment=request.POST.get('comment')
        com=Comment1(comment1_n=name,comment1_d=comment)
        com.save()
        n="Comment inserted successfully"
    return render(request,"feedpage.html",{'n':n}) 
def registerform(request):
    # rf=registersForm()
    # data1={'rf':rf}
    return render(request,"register.html")
def registerinformation(request):
    n1=''
    if request.method=="POST":
        fn=request.POST.get('fn')
        ea=request.POST.get('ea')
        pa=request.POST.get('pa')
        c=Registermod(fn=fn,ea=ea,pa=pa)
        c.save()
        n="Comment inserted successfully"
    return render(request,"register.html",{'n':n}) 
    
def delete(request,id1):
    s=Comment1.objects.get(id=id1)
    s.delete()
    return render(request,"feedpage.html")
def like(request):
    return render(request,"feedpage.html")
