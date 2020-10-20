from os import name
from django.http import request
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from accounts.models import mycustomers
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def customers(request):
    mycusts=  mycustomers.objects.all()
    return render(request, 'viewcustomers.html', {'mycusts': mycusts})



def personal_account(request , customer_name):
    mycusts=  mycustomers.objects.all()
    parcusts=  mycustomers.objects.get(name = customer_name)
    return render(request , 'personal_account.html' , {'parcusts': parcusts  })

def transactionpage(request):
    mycusts=  mycustomers.objects.all()
    return render(request, 'transaction.html', {'mycusts': mycusts})



def transaction(request):
    mycusts=  mycustomers.objects.all()
    amount =int(request.POST.get('amount'))
    print(amount)

    from_customer =  get_object_or_404(mycusts, name=request.POST.get('from_customerid'))
    to_customer =get_object_or_404(mycusts, name=request.POST.get('to_customerid'))
    if from_customer == to_customer:
        messages.error(request ,"Sender and Receiver must be different !!!")
        return redirect('/accounts/transactionpage')

    else:
        if from_customer.CurrentBalance >= amount:
            from_customer.CurrentBalance = from_customer.CurrentBalance - amount
            from_customer.save()
            to_customer. CurrentBalance = to_customer.CurrentBalance + amount
      
            to_customer.save()
            messages.success(request ,"Transaction Successful")
            return redirect('/accounts/customers')
   
        else:
            messages.error(request ,"Balance Not Sufficient !!!")
            return redirect('/accounts/transactionpage')



  
   