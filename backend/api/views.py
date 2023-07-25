# from django.shortcuts import render
from api.serializers import ArticleSerializer,UserSerializer
from blog.models import Article
from rest_framework.generics import (RetrieveAPIView,
                                    ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView,
                                    RetrieveDestroyAPIView)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    