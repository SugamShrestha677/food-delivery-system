from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RegisterView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Forget password views
@method_decorator(csrf_exempt, name='dispatch')
class PasswordResetRequestView(APIView):
    authentication_classes = []  
    permission_classes = []
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password reset link sent.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        reset_url = f"http://127.0.0.1:8000/api/auth/password-reset-confirm/{user.id}/{token}/"
        print("DEBUG reset URL:", reset_url)  # <--- Add this line



class PasswordResetConfirmView(APIView):
    def post(self, request, uid, token):
        data = {
            'uid': uid,
            'token': token,
            'new_password': request.data.get('new_password'),
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)  # Ends session
        return Response({"detail": "Logged out successfully."})
    



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
# def user_sign(request):
#     return render(request,"accounts/login.html")


# def restaurant_sign(request):
#     return render(request,"restaurant/signup-in.html")


# def dashboard(request):
#     return render(request,"accounts/dashboard.html")


from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout, authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RegisterView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Custom login view with role-based checks
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            # Get the user from the request
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            
            if user:
                print(f"DEBUG: API Login - User {user.username} has role: {user.role}")
                
                # Add role information to the response
                response.data['role'] = user.role
                response.data['username'] = user.username
                
                # Also log the user in via Django session for compatibility
                from django.contrib.auth import login
                login(request, user)
        
        return response
    


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permission import IsCustomer

class CustomerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def get(self, request):
        return Response({"message": f"Welcome {request.user.username}, to your dashboard"})

