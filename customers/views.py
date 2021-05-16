from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def list_customer(request):
    customers = Customer.objects.all().order_by('-id')
    queryset = request.GET.get('q')

    if queryset:
        customers = Customer.objects.filter(
            Q(name__icontains=queryset)|
            Q(email__icontains=queryset)| # LIKE % ana %
            Q(cpf__icontains=queryset)
        )
    paginator = Paginator(customers, 5) 
    page = request.GET.get('page')
    customers = paginator.get_page(page)

    return render(request,"customers/customer_list.html",{'customers':customers})

def add_customer(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = CustomerForm()
        messages.success(request,"Customer Added Successfully")
        return redirect('list_customer')
    return render(request,"customers/add_customer.html",{'form':form})

def edit_customer(request,id=None):
    customer = get_object_or_404(Customer,id=id)
    form = CustomerForm(request.POST or None,instance=customer)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Customer updated successfully")
        return redirect('list_customer')
    return render(request,"customers/edit_customer.html",{'form':form})

def remove_customer(request,id=None):
    customer = get_object_or_404(Customer,id=id)
    if request.method == "POST":
        customer.delete()
        messages.warning(request,"Customer deleted successfully")
        return redirect('list_customer')
    
    return render(request,"customers/remove_customer.html",{'customer':customer})