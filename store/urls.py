from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.toindex, name='index'),
    path('index', views.toindex, name='index'),
    path('product_details/<str:id>', views.product_details, name='product_details'),
    path('product_admin_details/<str:id>', views.product_admin_details, name='product_admin_details'),
    path('product_admin_details/view/<str:id>', views.product_admin_details_view, name='product_admin_details_view'),
    path('edit_product/<str:id>', views.edit_product, name='edit_product'),
    path('products', views.products, name='products'),
    path('products_admin', views.products_admin, name='products_admin'),
    path('cart', views.cart, name='cart'),
    path('addtocart/<str:product_id>', views.addtocart, name='addtocart'),
    path('removeorder/<str:product_id>', views.removeorder, name='removeorder'),
    path('account/signup', views.account_signup, name='account_signup'),
    path('account/login', views.account_login, name='account_login'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('confirm', views.confirm, name='confirm'),
    path('send', views.send, name='send'),
    path('confirmed', views.confirmed, name='confirmed'),
    path('confirmed_admin', views.confirmed_admin, name='confirmed_admin'),
    path('edit_confirmed_order/<str:id>/<str:stat>', views.edit_confirmed_order, name='edit_confirmed_order'),
    path('control_panel', views.control_panel, name='control_panel'),
    path('message/<str:message>/<str:directlink>', views.message_template, name='message_template'),
]