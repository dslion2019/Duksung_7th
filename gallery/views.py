from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .forms import PostForm
from .models import Post



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name ='post_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-birthday')

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.html'

class DeletePostView(DeleteView):
    model = Post
    template_name='delete.html'
    success_url = reverse_lazy('home')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post.html'
    form_class = PostForm

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk': self.pk})
        

        
    