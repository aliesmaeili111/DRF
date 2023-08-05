# from django.shortcuts import render
from api.serializers import ArticleSerializer,UserSerializer
from blog.models import Article
from rest_framework.generics import (RetrieveAPIView,
                                    ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView,
                                    RetrieveDestroyAPIView)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from api.permissions import (IsSuperUser,IsAuthorOrReadOnly,
                            IsStaffOrReadOnly,
                            IsSuperUserOrStaffReadOnly)
from rest_framework.authentication import SessionAuthentication

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentucation_classes = (SessionAuthentication,)
    

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    permission_classes = (IsSuperUserOrStaffReadOnly,)
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)
    