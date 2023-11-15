from django.urls import path
from . import views

urlpatterns = [ 
    path("transaction/", views.transaccion, name="transaction"),
    path("transaction/<int:p_id>/delete", views.delete_transaccion, name="delete_cartera"),

]