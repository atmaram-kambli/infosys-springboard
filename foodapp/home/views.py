from django.shortcuts import render, HttpResponse
from restuarant.models import Restaurant

# Create your views here.
def index(request):
    return render(request,'index.html')


def dashboard(request):
    return render(request,'dashboard.html')

# def restuarant_list(request):
#     from django.shortcuts import render


def restaurant_list(request, city):
    restaurants = Restaurant.objects.filter(city__iexact=city)
    
    context = {
        'restaurants': restaurants,
        'city_name': city.capitalize()
    }
    
    return render(request, 'restaurant_list.html', context)
