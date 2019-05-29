from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name ='post_list'
    def get_queryset(self):
        return Post.objects.order_by('-now_date')[:6]

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.html'
    