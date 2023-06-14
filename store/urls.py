from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_details/<str:id>', views.product_details, name='product_details'),
    path('cart/<str:username>', views.cart, name='cart'),
    path('addtocart/<str:product_id>/<str:username>', views.addtocart, name='addtocart'),
    path('removeorder/<str:product_id>/<str:username>', views.removeorder, name='removeorder'),
    path('products', views.products, name='products'),
    path('account', views.account, name='account'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('confirm/<str:total_price>', views.confirm, name='confirm'),
    path('send/<str:username>/<str:total_price>', views.send, name='send'),
]