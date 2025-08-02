from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.restaurants.models import Restaurant
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from functools import wraps

# Enhanced role-based access decorator
def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                print(f"DEBUG: User not authenticated, redirecting to signin")
                # Redirect to generic signin that can detect role
                user_role = getattr(request.user, 'role', None)
                print(f"[DEBUG] role_required: user={request.user}, role={user_role}, allowed={allowed_roles}")
                return redirect('signin')

            
            print(f"DEBUG: User {request.user.username} has role: {request.user.role}")
            print(f"DEBUG: Allowed roles: {allowed_roles}")
            
            if request.user.role not in allowed_roles:
                print(f"DEBUG: Access denied - user role '{request.user.role}' not in allowed roles {allowed_roles}")
                return HttpResponseForbidden("You do not have permission to access this page.")
            
            print(f"DEBUG: Access granted for user {request.user.username}")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator




def signin(request):
    # Generic signin that redirects to role-specific signins
    return render(request, 'accounts/generic_signin.html')









def home(request):
    return render(request,"accounts/home.html")

def test_page(request):
    return render(request, 'restaurant/dashboard.html')


def restaurant_signin(request):
    if request.method == "POST":
        logout(request)  # <== force logout first
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(f"[DEBUG] Authenticated user: {user} with role: {getattr(user, 'role', 'N/A')}")

        if user is not None and user.role == 'owner':
            login(request, user)
            return redirect('restaurant_dashboard')
        else:
            messages.error(request, "Invalid credentials or incorrect role access")
    return render(request, 'restaurant/signup-in.html')

def customer_signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == 'customer':
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid credentials or incorrect role access")
            
    return render(request, 'accounts/login.html')


def deliveryperson_signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == 'driver':
            login(request, user)
            return redirect('deliveryperson_dashboard')
        else:
            messages.error(request, "Invalid credentials or incorrect role access")
            
    return render(request, 'driver/driversignin.html')
@login_required
@role_required(['restaurant_owner'])
def restaurant_dashboard(request):
    print(f"[DEBUG] Accessing restaurant_dashboard | user: {request.user.username} | role: {request.user.role}")
    return render(request, 'restaurant/dashboard.html')

@login_required
@role_required(['customer'])
def customer_dashboard(request):
    return render(request, 'accounts/customer.html')

@login_required
@role_required(['driver'])
def deliveryperson_dashboard(request):
    print(f"[DEBUG] Accessing deliveryperson_dashboard | user: {request.user.username} | role: {request.user.role}")
    return render(request, 'driver/dashboard.html')




def restaurant(request):
    return render(request, 'restaurant/restaurantlanding.html')

def signout(request):
    logout(request)
    return redirect('home')


# from django.http import Http404

# @login_required(login_url='/restaurant/signin/')
# def restaurant_dashboard(request):
#     print("DEBUG: request.user =", request.user)
#     print("DEBUG: request.user.id =", request.user.id)
#     print("DEBUG: request.user.username =", request.user.username)

#     try:
#         restaurant = Restaurant.objects.get(user=request.user)
#     except Restaurant.DoesNotExist:
#         print("ERROR: No Restaurant found for user:", request.user.username)
#         raise Http404("Restaurant not found")

#     return render(request, 'restaurant/dashboard.html', {'restaurant': restaurant})



def restaurant_session_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == 'restaurant_owner':
            login(request, user)  # sets request.user
            return redirect('/restaurant/dashboard/')
        else:
            messages.error(request, "Invalid credentials or not a restaurant owner.")

    return render(request, 'restaurant/signin.html')


# @login_required(login_url='/restaurant/signin/')
# def restaurant_dashboard(request):
#     return render(request, 'restaurant/dashboard.html', {'restaurant': restaurant})
    # try:
    #     print(f"DEBUG: request.user.id = {request.user.id}")
    #     restaurant = Restaurant.objects.get(user=request.user)
    #     return render(request, 'restaurant/dashboard.html', {'restaurant': restaurant})
    # except Restaurant.DoesNotExist:
    #     print(f"ERROR: No Restaurant found for user: {request.user}")
    #     return render(request, 'restaurant/not_found.html', status=404)

def order(request):
    return render(request, 'restaurant/order.html')
def menu(request):
    return render(request, 'restaurant/menu.html')
def profile(request):
    return render(request, 'restaurant/profile.html')
def restaurant_template_view(request):
    return render(request, "restaurant/restaurant.html")
def customer(request):
    return render(request, "accounts/customer.html")
