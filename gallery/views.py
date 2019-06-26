from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

#forms
from gallery.forms import PostForm, CommentForm
from gallery.models import Post, Comment

#pagination
from django.core.paginator import Paginator

#login
from django.contrib.auth.models import User


class HomePageView(ListView):
    model = Post
    template_name = 'gallerymain.html'
    context_object_name ='post_list'
    paginate_by= 8

    def get_queryset(self):
        return Post.objects.all().order_by('-birthday')

#posts filter: public or private

#login required
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'gallerypost.html'
    success_url = reverse_lazy('gallery_main')
    
# login required
class DetailPostView(DetailView):
    model = Post
    template_name = 'gallerydetail.html'

#login + permission required
class DeletePostView(DeleteView):
    model = Post
    template_name='gallerydelete.html'
    success_url = reverse_lazy('gallery_main')

#login + permission required
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'gallerypost.html'
    form_class = PostForm

    def get_absolute_url(self):
        return reverse('gallery_detail', kwargs={'pk': self.pk})

#login required
def gallerycomment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('gallery_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'galleryaddcomment.html', {'form': form})


