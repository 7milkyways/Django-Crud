from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post

class PostCreateView(ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(ListView):
    model = Post

class PostUpdateView(ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

