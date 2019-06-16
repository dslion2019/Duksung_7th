from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .forms import PostForm
from .models import Post



class HomePageView(ListView):
    model = Post
    template_name = 'gallerymain.html'
    context_object_name ='post_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-birthday')

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'gallerypost.html'
    success_url = reverse_lazy('gallery_main')

class DetailPostView(DetailView):
    model = Post
    template_name = 'gallerydetail.html'

class DeletePostView(DeleteView):
    model = Post
    template_name='gallerydelete.html'
    success_url = reverse_lazy('gallery_main')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'gallerypost.html'
    form_class = PostForm

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk': self.pk})
        

        
    