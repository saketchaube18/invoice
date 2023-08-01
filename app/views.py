from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from . models import *
# Create your views here.

def home(request):
    return HttpResponse("eye of the tiger")

def register(request):
    if request.method =="POST":
        first_name=request.POST.get("fname",None)
        last_name=request.POST.get("lname",None)
        email_address=request.POST.get("email",None)
        password=request.POST.get("password",None)

        user= User.objects.create_user(username=email_address,email=email_address,first_name=first_name,last_name=last_name, password=password)
        return redirect("login")
    return render(request,"register.html")

def login(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user= authenticate(request,**{"username":username,"password":password})
        print(user)

        if not user:
            print("user not found, please register yourself")

        else:
            print("user found")
            print(request.user)
            return redirect('invoice')

    return render(request, 'login.html')  

def invoice(request):
    if request.method=="POST":
        invoice_date=request.POST.get("date")
        invoice_number=request.POST.get("invoice_n")
        customer_name=request.POST.get("name")
        invoice_duedate=request.POST.get("duedate")
        Product=request.POST.get("product")
        Quantity=request.POST.get("qty")
        Rate=request.POST.get("rate")
        Total=request.POST.get("total")

        Invoice.objects.create(invoice_date=invoice_date,invoice_number=invoice_number,customer_name=customer_name,invoice_duedate=invoice_duedate,Product=Product,Quantity=Quantity,Rate=Rate,Total=Total)
    return render(request,"invoice.html")

def viewinvoice(request):
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}
    print(invoices.first())

    return render(request,"viewinvoice.html",context)



def deleteinvoice(request,pk):
    Invoice.objects.filter(id=pk).delete()
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}
    print(invoices.first())

    return render(request,"viewinvoice.html",context)
        
