from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import contact
# Create your views here.
def home(request):
    if request.method=="POST":
        project= request.POST.get('project','')
        Name = request.POST.get('project','')
        phone = request.POST.get('phone Number','')
        Address = request.POST.get('Address Name','')
        Email = request.POST.get('Email','')
        if project and Name and phone and  Address and Email:
            contact= contact(project=project,Name=Name,phone=phone,Address=Address,Email=Email)
            contact.save()
        else:
            return HttpResponse(" Enter the all detail")

    return render(request,"index.html")