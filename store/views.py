from django.template.defaulttags import register
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms, template
from .models import product, testimonial, order, confirmed_orders
from .forms import product_form 

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

def toindex(request):
    return redirect('/')

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
    
    return render(request, 'product_details.html', data)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This is used username')
                return redirect('/account/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This is used email')
                return redirect('/account/signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'thanks for register, plz login')
                return redirect('/account/login')
        else:
            messages.info(request, 'the password is not the same')
            return redirect('/account/signup')
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
            return redirect('/account/login')
    else: 
        return render(request, 'account.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def addtocart(request, product_id):
    count = request.POST['count']
    size = request.POST['size']
    target_product = product.objects.get(id=product_id)
    user = request.user
    temp = order.objects.filter(product = target_product, user=user, size=size, is_confirmed=False)
    
    if temp.exists():
        my_order = order.objects.get(product=target_product, user=user, size=size, is_confirmed=False)
        my_order.count += int(count)
    else:
        my_order = order.objects.create(product=target_product, user=user, count=count, size=size)
    my_order.save()
    return redirect('/cart')

def removeorder(request, product_id):
    order.objects.get(id=product_id).delete()

    return redirect('/cart')

def cart(request):
    all_orders = order.objects.filter(user=request.user, is_confirmed=False)
    
    data = {
        'orders': all_orders,
        'orders_not_exist': not all_orders.exists()
    }
    return render(request, 'cart.html', data)

def account_signup(request):
    return render(request, 'account.html',{'tp': 'signup'})

def account_login(request):
    return render(request, 'accountlogin.html', {'tp': 'signup'})

def confirm(request):
    all_orders = order.objects.filter(user=request.user, is_confirmed=False)
    total_price = 0
    for o in all_orders:
        total_price += o.count * o.product.price

    return render(request, 'confirm.html', {'total_price': total_price})

def send(request):
    user = request.user
    all_orders = order.objects.filter(user=request.user, is_confirmed=False)
    total_price = 0
    for o in all_orders:
        x = o
        o.is_confirmed = True
        o.save()
        total_price += o.count * o.product.price
    
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        if phone == '':
            messages.info(request, 'please fill the phone and address fields')
    else:
        return redirect('/confirm')
    # if confirmed_orders.objects.filter(user=user).exists():
    #     confirmed_orders.objects.get(user=user).delete()
    conf_order = confirmed_orders.objects.create(user=user,total_price=total_price,address=address,phone=phone)
    for o in all_orders:
        conf_order.orders.add(o)
        
    
    return redirect('/')

def confirmed(request):
    all_conf_orders = confirmed_orders.objects.filter(user=request.user)
    
    return render(request, 'confirmed.html', {'all_conf_orders': all_conf_orders, 'conf_orders_not_exist': not all_conf_orders.exists() })

def control_panel(request):
    if request.user.is_superuser:
        return render(request, 'control_panel.html')
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')

def confirmed_admin(request):
    if request.user.is_superuser:
        # all_users_conf_orders = confirmed_orders.objects.order_by('user').all
        all_users_conf_orders = dict()
        total_price_for_all_orders = 0
        for user_orders in confirmed_orders.objects.order_by('user').all():
            total_price_for_all_orders += user_orders.total_price
            username = user_orders.user.username
            if username not in list(all_users_conf_orders.keys()):
                all_users_conf_orders[f'{user_orders.user.username}'] = []
            all_users_conf_orders[f'{user_orders.user.username}'].append(user_orders)
            
            # all_users_conf_orders[f'{user_orders.user.username}'].append(user_orders)
        return render(request, 'confirmed_admin.html', {"all_users_conf_orders": all_users_conf_orders, 'total_price_for_all_orders': total_price_for_all_orders})
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')

def edit_confirmed_order(request, id, stat):
    if request.user.is_superuser:
        order = confirmed_orders.objects.get(id=id)
        order.status = stat
        order.save()
        return redirect('confirmed_admin')
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')

def products_admin(request):
    if request.user.is_superuser:
        all_products = product.objects.all()

        data = {
            'all_products': all_products,
        }
        return render(request, 'products_admin.html', data)
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')

def product_admin_details(request, id):
    if request.user.is_superuser:
        if(id == 'new'):
            prod = product.objects.create(rate=5, rate_text='FFFFF')
            prod.save()
            id = prod.id
        else:
            prod = product.objects.get(id=id)
        
        form = product_form(instance=prod)
        data = { 'form': form, 'id' : id }
        return render(request, 'product_admin_details.html', data)
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')

def edit_product(request, id):
    if request.user.is_superuser:
        prod = product.objects.get(id=id)
        if request.method == 'POST':
            if request.POST.get('offer_image'):
                prod.offer_image =  'static/images/' + request.POST.get('offer_image')
            elif not prod.offer_image :
                prod.offer_image =  'static/images/product-null.jpg'
            if request.POST.get('gallery_1'):
                prod.gallery_1 =  'static/images/' + request.POST.get('gallery_1')
            elif not prod.gallery_1 :
                prod.gallery_1 =  'static/images/product-null.jpg'
            if request.POST.get('gallery_2'):
                prod.gallery_2 =  'static/images/' + request.POST.get('gallery_2')
            elif not prod.gallery_2 :
                prod.gallery_2 =  'static/images/product-null.jpg'
            if request.POST.get('gallery_3'):
                prod.gallery_3 =  'static/images/' + request.POST.get('gallery_3')
            elif not prod.gallery_3 :
                prod.gallery_3 =  'static/images/product-null.jpg'
            if request.POST.get('gallery_4'):
                prod.gallery_4 =  'static/images/' + request.POST.get('gallery_4')
            elif not prod.gallery_4 :
                prod.gallery_4 =  'static/images/product-null.jpg'
            if request.POST.get('image'):
                prod.image =  'static/images/' + request.POST.get('image')
            elif not prod.image :
                prod.image =  'static/images/product-null.jpg'
            prod.description = request.POST.get('description')
            prod.sizes = request.POST.get('sizes')
            prod.name = request.POST.get('name')
            prod.featured_product = (request.POST.get('featured_product') == 'on')
            prod.offer = (request.POST.get('offer') == 'on')

            prod.save()
        return redirect(f'/product_admin_details/view/{id}')
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')

def product_admin_details_view(request, id):
    if request.user.is_superuser:
        target_product = product.objects.get(id= id)
        data = {
            'product': target_product,
            'product_gallery': [
                target_product.gallery_1,
                target_product.gallery_2,
                target_product.gallery_3,
                target_product.gallery_4,
            ],
            'id': id
        }
        
        return render(request, 'product_admin_details_view.html', data)
    else: return redirect('/message/FORBIDDEN FIELD ┌(ಠ_ಠ)┘ /home')


def message_template(request, message, directlink):
    return render(request, 'message.html', {'message':message, 'direct_link': directlink})























# filters
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='typeof')
def typeof(value):
    """
        returns the type of the value. 
    """
    return type(value)

@register.filter(name='is_succ')
def is_succ(val1):
    """
        check if start with 'thanks'.
    """
    return str(val1).split()[0] == 'thanks'

@register.filter(name='is_eq')
def is_succ(x, y):
    """
        check if the 2 strings are congurent.
    """

    return str(str(x)==str(y))