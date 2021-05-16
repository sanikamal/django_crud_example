from django.urls import path
from .views import list_customer,add_customer,edit_customer,remove_customer
urlpatterns = [
    path('',list_customer,name='list_customer'),
    path('add_customer/',add_customer,name='add_customer'),
    path('edit_customer/<int:id>',edit_customer),
    path('remove_customer/<int:id>',remove_customer)

]
