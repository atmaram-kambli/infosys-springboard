from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if(user and password != user.password):
            return render(request, 'user/login.html')
        
        userAuth = authenticate(request, email=user.email, password=password)
        auth_login(request, userAuth)
        
        return render(request,'index.html')
    return render(request,'user/login.html')

def register(request):
    if request.method == 'POST':       
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        
        user = User(firstname=firstname, lastname=lastname, email=email,password=password, address=address)
        user.save()

        print("User created successfully.")
        return redirect('login')
    return render(request,'user/register.html')
