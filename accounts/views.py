from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def portfolio_view(request):
    return render(request, 'accounts/index.html')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio')  # Adjust 'home' to your desired redirect URL after login
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
