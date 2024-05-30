from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.username = user.email  # Use email as username
            user.save()
            messages.success(request, 'User created successfully.')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'user/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')
