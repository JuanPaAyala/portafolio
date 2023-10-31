from django.urls import path
from . import views

urlpatterns = [ 
    path("contact/", views.contacto, name="contacto"),
    #path("contact/", views.send_email, name="send_email"),
]