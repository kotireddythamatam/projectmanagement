######################## django #########################
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings

######################## django #########################
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

######################## Company #########################
from .serializers import (
	CompanySerializer,
)
from .models import (
    Company,
)

######################## common #########################


class CompanyAPI(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        


