from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views import View
from .models import Product, Customer, OrderPlaced, Cart
from .forms import CustomerRegistrationForm, MyPassChangeForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate

class ProductView(View):
    def get(self, request):
        totalcart = 0
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        shoes = Product.objects.filter(category='S')
        if request.user.is_authenticated :
            totalcart = len(Cart.objects.filter(user=request.user))
        return render (request, 'app/home.html', {'topwear': topwear, 
        'bottomwear': bottomwear, 'mobile':mobile, 'shoes':shoes, 'totalcart':totalcart})

class ProductdetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated :
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)
            ).exists()
        return render(request, 'app/productdetail.html',
        {'product':product, "item_already_in_cart":item_already_in_cart})
@login_required
def add_to_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    prod_id  = request.GET.get('product_id')  
    product = Product.objects.get(id=prod_id)
    Cart(user=user, product=product).save()
    return redirect('/showcart')

def show_cart(request):
    if request.user.is_authenticated :
        user =request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product :
            for p in cart_product :
                tempamount = (p.quantity * p.product.discount_price)
                amount += tempamount 
                total_amount = amount + shipping_charges    
        return render(request, 'app/addtocart.html',{'carts':cart,
        'total_amount':total_amount, 'amount':amount})

def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.quantity += 1
        cart.save()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.filter() if p.user == request.user]
        for p in cart_product :
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount  

        data = {
            'quantity' : cart.quantity,
            'amount'   : amount,
            'total_amount': amount + shipping_charges
        }

        return JsonResponse(data)    

def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.quantity -= 1
        cart.save()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.filter() if p.user == request.user]
        for p in cart_product :
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount 

        data = {
            'quantity' : cart.quantity,
            'amount'   : amount,
            'total_amount': amount + shipping_charges
        }

        return JsonResponse(data)    
@login_required
def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.delete()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.filter() if p.user == request.user]
        for p in cart_product :
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount  

        data = {
            'quantity' : cart.quantity,
            'amount'   : amount,
            'total_amount': amount + shipping_charges 
        }

        return JsonResponse(data) 

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-success'})

def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed': op})


def mobile(request):
    mobile = Product.objects.filter(category='M')
    return render(request, 'app/mobile.html', {'mobile':mobile})

def topwear(request):
    tw = Product.objects.filter(category='TW')
    return render(request, 'app/topwear.html', {'tw':tw})


def shoes(request):
    S = Product.objects.filter(category='S')
    return render(request, 'app/shoes.html', {'S':S})


def bottomwear(request):
    bw = Product.objects.filter(category='BW')
    return render(request, 'app/bottomwear.html', {'bw':bw})


class CustomerRegistrationView(View):
    def get(self, request):
         form = CustomerRegistrationForm()
         return render (request, 'app/customerregistration.html', {'form':form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid() :
            messages.success(request, 'Congratulations!! registered Successfully')
            form.save()
        return render (request, 'app/customerregistration.html', {'form':form})

@login_required       
def checkout(request):
    user =request.user
    cart_items = Cart.objects.filter(user=user)
    add = Customer.objects.filter(user=user)
    amount = 0.0
    shipping_charges = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.filter() if p.user == request.user]
    if cart_product :
        for p in cart_product :
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount      
            total_amount = amount + shipping_charges
    return render(request, 'app/checkout.html', {'add':add, 'total_amount':total_amount, 'cart_items':cart_items})


def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart :
        order_date = timezone.now().date()
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, order_date=order_date).save()
        c.delete()
    return redirect('orders')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('accounts/login')

@method_decorator(login_required, name='dispatch')
class profileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, "active":'btn-success'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid() :
            usr = request.user  
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfylly')
            form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, "active":'btn-success'})

