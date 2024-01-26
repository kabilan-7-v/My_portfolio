from django.shortcuts import render,redirect
from portfolio.models import Contact
from django.contrib import messages
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def handleblog(request):
    return render(request,'handleblog.html')
def resume(request):
    return render(request,'resume.html')
def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thank for contacting we wil get by you soon!")


        return redirect('/contact')

    return render(request,'contact.html')
