from django.template.defaulttags import register
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms
from .models import product, testimonial, order, confirmed_orders

# Create your views here.
def index(request):
    
    featured_products = product.objects.filter(featured_product=True)
    all_products = product.objects.all()
    offer = product.objects.filter(offer=True).last()
    testimonials = testimonial.objects.all()

    data = {
        'featured_products': featured_products,
        'all_products': all_products,
        'offer': offer,
        'testimonials': testimonials
    }
    return render(request, 'index.html', data)

def products(request):
    all_products = product.objects.all()

    data = {
        'all_products': all_products,
    }
    return render(request, 'products.html', data)

def product_details(request, id):
    target_product = product.objects.get(id= id)
    all_products = product.objects.all()

    data = {
        'product': target_product,
        'product_gallery': [
            target_product.gallery_1,
            target_product.gallery_2,
            target_product.gallery_3,
            target_product.gallery_4,
        ],
        'all_products': all_products
    }
    
    return render(request, 'product-details.html', data)

def signup(request):
    if request.method == 'POST':
        username = request.POST['useeeername']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This is used username')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This is used email')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'thanks for register, plz login ')
        else:
            messages.info(request, 'the password is not the same')
        return redirect('account')
    else:
        return render(request, 'account.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong username or password')
            return redirect('login')
    else: 
        return render(request, 'account.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def addtocart(request, product_id, username):
    count = request.POST['count']
    size = request.POST['size']
    target_product = product.objects.get(id=product_id)
    temp = order.objects.filter(product = target_product, username=username, size=size)
    
    if temp.exists():
        my_order = order.objects.get(product=target_product, username=username, size=size)
        my_order.count += int(count)
    else:
        my_order = order.objects.create(product=target_product, username=username, count=count, size=size)
    my_order.save()
    return redirect('/cart/'+username)

def removeorder(request, product_id, username):
    order.objects.get(id=product_id).delete()


    return redirect('/cart/'+username)

def cart(request, username):
    all_orders = order.objects.filter(username=username, is_confirmed=False)
    
    data = {
        'orders': all_orders,
        'orders_not_exist': not all_orders.exists()
    }
    return render(request, 'cart.html', data)

def account(request):
    return render(request, 'account.html')

def confirm(request, total_price):
    return render(request, 'confirm.html', {'total_price': total_price})

def send(request, username, total_price):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
    else:
        return redirect('/confirm')
    if confirmed_orders.objects.filter(user=user).exists():
        confirmed_orders.objects.get(user=user).delete()
    confirmed_orders.objects.create(user=user,total_price=int(total_price),address=address,phone=phone)
    return redirect('/')




# filters
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)