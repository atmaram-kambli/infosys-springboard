"""
URL configuration for foodapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from restuarant import views as restua_views
# from customer import views as customer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('', include('home.urls')),
    # path('', home_views.index, name='index'),
    # path('dashboard/', home_views.dashboard, name='dashboard'),
    # path('<str:city>/', home_views.restaurant_list, name='restaurant_list'),
    # # path('restuarant_list/', home_views.restaurant_list, name='restua_list')
    # path('restaurant/<int:restaurant_id>/', restua_views.restaurant_detail, name='restaurant_detail'),

]