
from email import message
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from flask import request
from home.models import Product, Cart, OrderPlaced, Customer
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib import messages
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class ProductView(View):
    def get(self, request):
        all_pro = Product.objects.all()[:23:3]
        mobile = Product.objects.filter(category='MB')
        appliances = Product.objects.filter(category='AP')
        men_fs = Product.objects.filter(category='MF')
        wm_fs = Product.objects.filter(category='WF')
        m_ft = Product.objects.filter(category='MFW')
        wm_ft = Product.objects.filter(category='WFW')
        return render(request, 'home.html',
                      {
                          'mobile':mobile, 'appliances':appliances,
                          'men_fs':men_fs, 'wm_fs':wm_fs,
                          'm_ft':m_ft, 'wm_ft':wm_ft,
                          'all_pro':all_pro
                          })
        

# def home(request):
#  return render(request, 'home.html')

# def product_detail(request):
#  return render(request, 'productdetail.html')

class ProductDetailView(View):
    def get(self, request, url ):
       product =  Product.objects.get(url = url )
       return render (request, 'productdetail.html', {'product':product} )
        
def mobile(request, data =None):
    if data == None:
        mobile = Product.objects.filter(category='MB')  
    elif data == 'realme' or data ==  'POCO' or data ==  'Samsung':
        mobile = Product.objects.filter(category='MB').filter(brand=data)
    elif data == 'below':
        mobile = Product.objects.filter(category='MB').filter(discount_price__lt=10000)
    elif data == 'above':
        mobile = Product.objects.filter(category='MB').filter(discount_price__gt=10000)
    return render(request, 'mobile.html', {'mobile':mobile})
 
 
def appliances(request, data =None):
    if data == None:
        appliances = Product.objects.filter(category='AP')  
    elif data == 'Philips' or data ==  'LG' or data ==  'TCL' or data ==  'Samsung' or data ==  'Whilepool':
        appliances = Product.objects.filter(category='AP').filter(brand=data)
    elif data == 'below':
        appliances = Product.objects.filter(category='AP').filter(discount_price__lt=50000)
    elif data == 'above':
        appliances = Product.objects.filter(category='AP').filter(discount_price__gt=50000)
    return render(request, 'appliances.html', {'appliances':appliances})

def menfashion(request, data = None):
    if data == None:
        menfashion = Product.objects.filter(category='MF')  
    elif data == 'MontCarlo' or data == 'PeterEngland' or data == 'ARCreation' or data == 'LeeCooper':
        menfashion = Product.objects.filter(category='MF').filter(brand=data)
    elif data == 'below':
        menfashion = Product.objects.filter(category='MF').filter(discount_price__lt=1000)
    elif data == 'above':
        menfashion = Product.objects.filter(category='MF').filter(discount_price__gt=1000)
    return render(request, 'menfashion.html', {'menfashion':menfashion} )

def womenfashion(request, data = None):
    if data == None:
        womenfashion = Product.objects.filter(category='WF')  
    elif data == 'Zaara' or data == 'MRX' or data == 'TRX' :
        womenfashion = Product.objects.filter(category='WF').filter(brand=data)
    elif data == 'below':
        womenfashion = Product.objects.filter(category='WF').filter(discount_price__lt=5000)
    elif data == 'above':
        womenfashion = Product.objects.filter(category='WF').filter(discount_price__gt=5000)
    return render(request, 'womenfashion.html', {'womenfashion':womenfashion} )

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = ProfileForm() 
        return render(request, 'profile.html', {'form':form})
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            Address = form.cleaned_data['Address']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            profile = Customer(user=user, name=name, Address=Address, phone=phone, city=city, zipcode=zipcode, state=state, country=country)
            profile.save()
            messages.success(request, 'Your Profile Update Successfully')
        return render(request, 'profile.html', {'form':form})
        

def address(request):
    address = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'address':address})


def addtocart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    cart = Cart(user=user, product=product)
    cart.save()
    print(product_id)
    return redirect('/items-in-cart')


def items_in_cart(request):  
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)  
        # print(cart)
        amount = 0
        shipping_amount = 40
        total_amount = 0
        cart_product = [ p for p in Cart.objects.all() if p.user == user ]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = ( p.quantity * p.product.discount_price)
                amount += tempamount
                totalamount = amount + shipping_amount
                   
            return render(request, 'addtocart.html', {'cart':cart ,'shipping_amount':shipping_amount, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'empty.html')
        

def plus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        print(product_id)
        c = Cart.objects.get(Q(product=product_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        amount = 0
        shipping_amount = 40
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = ( p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount = amount + shipping_amount
            
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        print(product_id)
        c = Cart.objects.get(Q(product=product_id) & Q(user = request.user))
        c.quantity-=1
        c.save()
        amount = 0
        shipping_amount = 40
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = ( p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount = amount + shipping_amount
            
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        print(product_id)
        c = Cart.objects.get(Q(product=product_id) & Q(user = request.user))
        c.delete()
        amount = 0
        shipping_amount = 40
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = ( p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount = amount + shipping_amount
            
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
    
@login_required
def checkout(request):
    user = request.user
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0
    shipping_amount = 40
    cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = ( p.quantity * p.product.discount_price)
            amount += tempamount
        totalamount = amount + shipping_amount
   

    return render(request, 'checkout.html', {'address':address, 'totalamount':totalamount, 'cart_items':cart_items})


def payment(request):
    user = request.user
    addid = request.GET.get('addid')
    customer = Customer.objects.get(id=addid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'orders.html', {'order_place':op})



def search(request):
    query = request.GET['query']
    if len(query) > 80:
        search = Product.objects.none()
    else:
        searchtitle = Product.objects.filter(title__icontains = query)
        searchbrand = Product.objects.filter(brand__icontains = query)
        searchall = searchtitle.union(searchbrand)
        
    return render( request, 'search.html', {'search' : searchall, 'query' : query })



def buy_now(request):
    return render(request, 'buynow.html')


