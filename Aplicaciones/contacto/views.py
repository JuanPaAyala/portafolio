
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contacto
from django.conf import settings
#from .utils import send_email_test

def contacto(request):
    if request.method == "POST":
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        send_mail(
            'Nombre',
            tname,
            'Mensaje',
            tmessage,
            'settings.EMAIL_HOST_USER',
            [temail],
            fail_silently=False)
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()        #return HttpResponse("EL registro fue ingresado")
        return render(request,"pages/gracias.html",)
    #mis_proyectos = Proyecto.objects.all()
    return render(request,"pages/contact.html",)

# def send_email(request):
#     print("Sending email")
#     send_email_test()
#     return render(request,"pages/gracias.html",)