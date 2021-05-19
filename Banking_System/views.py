from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def customer(request):
    customer=Cutomers.objects.all
    dict={"customer":customer}
    return render(request,'viewcustomers.html',dict)

def money(request,id):
    money=Cutomers.objects.get(id=id)
    customer=Cutomers.objects.exclude(name=money.name)
    tdict={
        "money":money,
        "customer":customer
    }
    return render(request,'transfermoney.html',tdict)

def money_processing(request,id):
    if request.method =="POST":
        transfered_to=request.POST["transfered_to"]
        amount=request.POST["amount"]
        cus=Cutomers.objects.get(id=id)
        his=History(transfered_by=cus.name,transfered_to=transfered_to,amount=amount)
        if float(cus.balance)>float(his.amount):
            cus.balance=cus.balance-float(his.amount)
            cus.save()
            his.save()
            return redirect("/customer")
        else:
            return redirect("/customer")

    



def history(request):
    hist=History.objects.all()
    dic={"hist":hist}
    return render(request,'history.html',dic)

    