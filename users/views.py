from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required
def home(request):
    return render(request, 'home.html')

def login_page(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        # AC_Owner login
        if user.user_type == 1:
            login(request, user)
            return redirect('brands')

        # Brand Manager
        elif user.user_type == 2:
            login(request, user)
            return redirect('home')

        # staff user
        elif user.user_type == 3:
            login(request, user)
            return redirect('home')
        
        # superuser login
        elif user.is_superuser:
            login(request, user)
            return redirect('home')
        else:
            HttpResponse('Username or password is incorrect!')
    context = {}
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')