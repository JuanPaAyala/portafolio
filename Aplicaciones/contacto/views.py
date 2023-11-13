
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
            # 'Nombre', tname,
            'Mensaje', tmessage,
            'settings.EMAIL_HOST_USER',
            [temail],
            fail_silently=False)
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()        #return HttpResponse("EL registro fue ingresado")
        return render(request,"pages/gracias.html",)
    #mis_proyectos = Proyecto.objects.all()
    return render(request,"pages/contact.html",)


# def contacto(request):
#     if request.method == "POST":
#         tname = request.POST["name"]
#         temail = request.POST["email"]
#         tphone = request.POST["phone"]
#         tmessage = request.POST["message"]
#         ctx = {
#             'Nombre', tname,
#             'Mensaje', tmessage,
#             #'email', temail
#         }
#         message = render_to_string('mail.html', ctx)
#         send_mail('Gracias Por Contactarnos',
#             message,
#             settings.EMAIL_HOST_USER,
#             ['projecthouse2120@gmail.com'], 
#             fail_silently=False, html_message=message)
#         obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
#         obj_contact.save()    
#         #return HttpResponse("EL registro fue ingresado")
#         return render(request,"pages/gracias.html",)
#     #mis_proyectos = Proyecto.objects.all()
#     return render(request,"pages/contact.html",)

# from django.shortcuts import render, HttpResponse
# from django.core.mail import send_mail
# from django.conf import settings

# from .models import Contacto

# # Create your views here.
# def contacto(request):
#     if request.method == "POST":
#         tname = request.POST["name"]
#         temail = request.POST["email"]
#         tphone = request.POST["phone"]
#         tmessage = request.POST["message"]
#         obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
#         obj_contact.save()
#         #return HttpResponse("EL registro fue ingresado")
#         email(obj_contact)
#         return render(request,"pages/gracias.html",)
#     #mis_proyectos = Proyecto.objects.all()
#     return render(request,"pages/contact.html",)

# def email(email):
#     subject = 'Thank you for contact me'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['projecthouse2120@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return True
    