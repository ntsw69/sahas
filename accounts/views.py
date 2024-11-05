from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random





def login_signup(request):
    return render(request, 'accounts/login_signup.html') 

def login_signup(request):
    return render(request, 'login_signup.html')



def admin_login(request):
    return render(request, 'accounts/adminlogin.html')

def userviewcase(request) : 
    return render(request, 'accounts/viewcase.html')

def emergency(request):
    return render(request, 'accounts/pcasecompleted.html') 

def pcasecompleted(request):
    return render(request, 'accounts/pcasecompleted.html') 

def overview(request):
    return render(request, 'accounts/overview.html') 

def pviewcase_view(request):
    return render(request, 'accounts/pviewcase.html') 
def police_view(request):
    # Your view logic here
    return render(request, 'accounts/police.html')
def userviewcase(request): 
    return render(request, 'accounts/viewcase.html')

def user_dashboard_view(request):
    return render(request, 'accounts/dashboard.html')  # Replace with actual template if different

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password."
            return render(request, 'accounts/adminlogin.html', {'error': error})

    return render(request, 'accounts/adminlogin.html')

def login_signup(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'signup':
            # Handle signup logic here
            pass
        elif form_type == 'login':
            # Handle login logic here
            pass

    return render(request, 'accounts/login_signup.html')

def verify_otp(request):
    # OTP verification logic here
    return render(request, 'accounts/verify_otp.html')

def verify_login_otp(request):
    # Login OTP verification logic here
    return render(request, 'accounts/verify_login_otp.html')

def logout_view(request):
    logout(request)
    return redirect('login_signup')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login_signup(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Handle signup form submission
        if form_type == 'signup':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            date_of_birth = request.POST.get('date_of_birth')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different one.')
                return render(request, 'accounts/login_signup.html')

            if password == password2:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )

                if not Profile.objects.filter(user=user).exists():
                    Profile.objects.create(
                        user=user,
                        phone_number=phone_number,
                        date_of_birth=date_of_birth
                    )

                otp = random.randint(100000, 999999)
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )

                request.session['otp'] = otp
                request.session['user_id'] = user.id

                return redirect('verify_otp')

            else:
                messages.error(request, 'Passwords do not match.')

        # Handle login form submission
        elif form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                otp = random.randint(100000, 999999)
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )

                request.session['login_otp'] = otp
                request.session['user_id'] = user.id

                return redirect('verify_login_otp')
            else:
                messages.error(request, 'Invalid login credentials.')

    return render(request, 'accounts/login_signup.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == str(request.session.get('otp')):
            user_id = request.session.get('user_id')
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()

            # Ensure the user is logged in if needed
            login(request, user)  # Log the user in

            return redirect('dashboard')  # Redirect to the user dashboard
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'accounts/verify_otp.html')


def verify_login_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == str(request.session.get('login_otp')):
            user_id = request.session.get('user_id')
            user = User.objects.get(id=user_id)
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'accounts/verify_login_otp.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Check if user is admin
            login(request, user)
            return redirect('dashboard')  # Adjust to your desired redirect
        else:
            error = "Invalid username or password."
            return render(request, 'accounts/adminlogin.html', {'error': error})

    return render(request, 'accounts/adminlogin.html')
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Check if user is admin
            # Generate OTP
            otp = random.randint(100000, 999999)
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            # Store OTP and user ID in session
            request.session['admin_login_otp'] = otp
            request.session['admin_user_id'] = user.id

            return redirect('verify_admin_login_otp')  # Redirect to OTP verification

        else:
            error = "Invalid username or password."
            return render(request, 'accounts/adminlogin.html', {'error': error})

    return render(request, 'accounts/adminlogin.html')
def verify_admin_login_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == str(request.session.get('admin_login_otp')):
            user_id = request.session.get('admin_user_id')
            user = User.objects.get(id=user_id)
            login(request, user)  # Log the admin in
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'accounts/verify_admin_login_otp.html')

