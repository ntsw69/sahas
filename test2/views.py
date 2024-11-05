from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm

def login_signup(request):
    login_form = LoginForm()
    signup_form = SignupForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')  # Redirect after successful login
        elif 'signup' in request.POST:
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                return redirect('login_signup')  # Redirect after successful signup

    return render(request, 'login_signup.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })
