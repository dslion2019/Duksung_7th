from django.urls import path
from . import views
from .views import HomePageView, CreatePostView, DetailPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', HomePageView.as_view(), name='gallery_main'),
    path('add/', CreatePostView.as_view(), name='gallery_add'),
    path('<int:pk>/', DetailPostView.as_view(), name='gallery_detail'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='gallery_delete'),
    path('<int:pk>/edit/', UpdatePostView.as_view(), name='gallery_edit'),
    path('<int:pk>/addcomment/',views.gallerycomment, name='gallery_add_comment'),
    ]