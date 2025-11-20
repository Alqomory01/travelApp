# from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from .permissions import IsAdmin

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
# class UserListView(generics.ListAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAdmin]

#     def get_queryset(self):
#         # Optionally filter users by role
#         role = self.request.query_params.get('role')
#         if role in ['admin', 'agent', 'customer']:
#             return User.objects.filter(role=role)
#         return User.objects.all()

# Create your views here.
