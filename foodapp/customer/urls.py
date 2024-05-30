from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('add_to_cart/<int:item_id>/',views. add_to_cart, name='add_to_cart'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
