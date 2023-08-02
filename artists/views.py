# This file is part of ArtistAPI.
#
# ArtistAPI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ArtistAPI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ArtistAPI.  If not, see <https://www.gnu.org/licenses/>.


# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, SAFE_METHODS
# from rest_framework.filters import SearchFilter
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer, UserSerializer
from .filters import ArtistFilter

import markdown

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly,]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = ArtistFilter
    
    def create(self, request, *args, **kwargs):
        response = {"message": "You can't create new artist."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    authentication_classes = [TokenAuthentication,]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['work_type',]

class RegisterView(APIView):
    def post(self, request):
        name = request.data.get('name')
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password or not name:
            return Response({'error': 'Name, Username and Password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User(username=username, password=make_password(password))
        user.save()
        
        artist = Artist.objects.get(user=user)  # get the artist associated with this user
        artist.name = name  # set the artist name
        artist.save()  # save the artist object
        
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

def readme(request):
    with open('README.md', 'r') as f:
        readme_content = f.read()
        html_content = markdown.markdown(readme_content)

    return HttpResponse(html_content, content_type='text/html')