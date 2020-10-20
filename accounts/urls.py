from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customers', views.customers , name = 'customers'),
    path('personal_account/<customer_name>', views.personal_account, name = 'personal_account' ),
    path('transactionpage',views.transactionpage, name = 'transactionpage' ),
    path('transaction' , views.transaction , name = 'transaction'),
    

   
 
 
    
    
    ]
