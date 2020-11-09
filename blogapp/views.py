from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm

# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class = PostForm
    template_name='update_post.html'
    fields=['title','content']

class DeletePostView(DeleteView):
    model=Post
    #form_class = PostForm
    template_name='delete_post.html'
    success_url = reverse_lazy('index')