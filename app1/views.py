from django.shortcuts import render
from django.http import HttpResponse
from .models import detail,stud
# Create your views here.

def page1(request):
    return HttpResponse("HELLO WORLD")

def page2(request):
    return HttpResponse("WELCOME")
def page_html(request):
    string="HELLO WELCOME CUSTOMERS"
    l = ["BENZ","AUDI","THAR","RANGEROVER","INNOVA","BMW","JEEP"]
    return render(request,"first.html",{'k1':string,'l1':l})
def page_table(request):
    p1=detail()
    p1.id=1
    p1.name="ABHILASH"
    p1.age=21
    p1.place="SHORANUR"
    p1.email="abhi4226@gmail.com"

    p2=detail()
    p2.id=2
    p2.name="AMIT"
    p2.age=21
    p2.place="PATTAMBI"
    p2.email="amit@gmail.com"

    p3=detail()
    p3.id=3
    p3.name="SHIJU"
    p3.age=22
    p3.place="PATTAMBI"
    p3.email="shijubal@gmail.com"

    p4=detail()
    p4.id=4
    p4.name="AKHIL"
    p4.age=21
    p4.place="PATTAMBI"
    p4.email="akhil2@gmail.com"
    l=[p1,p2,p3,p4]
    return render(request,"table.html",{"detail":l})

def forms(request):
    if request.method == "POST":
        number1 = request.POST['num1']
        number2 = request.POST['num2']
        if 'add' in request.POST:
            result= int(number1) + int(number2)
            return render(request,"form.html",{'OUTPUT':result})
    return render(request,"form.html")

def form2(request):
    if request.method=="POST":
        if request.POST.get("n")and request.POST.get("a"):
            formdata=stud()
            formdata.name=request.POST.get("n")
            formdata.adress= request.POST.get("a")
            formdata.save()
            tabledata = stud.objects.all()
            return render(request, "dbs.html", {'key': tabledata})
            # return render(request,'dbs.html')
    tabledata=stud.objects.all()
    return render(request,"dbs.html",{'key':tabledata})
