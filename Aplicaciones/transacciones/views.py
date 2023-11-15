from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from django.db.models import Sum, Case, When, F
from django.urls import reverse
from .models import Transaction

# Create your views here.

def transaccion(request):
    if request.method == "POST":
        tname = request.POST["name"]
        tdate = request.POST["date"]
        tdescription = request.POST["description"]
        obj_contact = Transaction(name=tname,date=tdate,description=tdescription)
        obj_contact.save()
        mis_ingreso = Transaction.objects.all()
        return render(request, "pages/transaction.html", {"transaction":mis_ingreso})
    else:
        mis_ingreso = Transaction.objects.all()
        return render(request, "pages/transaction.html", {"transaction":mis_ingreso})

def consultar_cartera(request):
    mis_ingreso = Transaction.objects.all()
    return render(request, "pages/transaction.html", {"transaction":mis_ingreso})

def delete_transaccion(request, p_id):
    obj_contact = get_object_or_404(Transaction,pk=p_id)
    obj_contact.delete()
    mis_ingreso = Transaction.objects.all()
    return render(request, "pages/transaction.html", {"transaction":mis_ingreso})
