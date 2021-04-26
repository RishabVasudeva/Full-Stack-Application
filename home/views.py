from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        "variable":"this is set"
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage")

def about(request):
   # return HttpResponse("This is about homepage")
   return render(request,'about.html')


def learn(request):
    #return HttpResponse("This is my learning homepage")
    return render(request,'learn.html')

def contact(request):
    if request.method == "POST":
        email =request.POST.get('email')
        password =request.POST.get('password')
        address= request.POST.get('address')
        city =request.POST.get('city')
        contact = Contact(email=email, password=password, address=address, city=city, date=datetime.today())
        contact.save()
    return render(request,'contact.html')


