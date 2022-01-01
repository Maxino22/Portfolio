from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import DefaultPagination
from .models import Blog, Profile, Tag, Contact, Comments
from .serializers import BlogSerializer, ProfileSerializer, TagSerializer, ContactSerializer, CommentSerializer
# Create your views here.


def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'posts.html', context)

def post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)

    context = {
        'post': post
    }

    return render(request, 'post.html', context)


class Profile(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class BlogsView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_fields = ['tags']
    search_fields = ['title', 'sub_title']
    ordering_fields = ['blog_date']


class BlogDetails(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewset(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class ContactView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
