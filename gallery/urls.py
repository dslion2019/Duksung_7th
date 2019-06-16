from django.urls import path

from .views import HomePageView, CreatePostView, DetailPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('gallery/', HomePageView.as_view(), name='gallery_main'),
    path('gallery/add/', CreatePostView.as_view(), name='gallery_add'),
    path('gallery/<int:pk>/', DetailPostView.as_view(), name='gallery_detail'),
    path('gallery/<int:pk>/delete/', DeletePostView.as_view(), name='gallery_delete'),
    path('gallery/<int:pk>/edit/', UpdatePostView.as_view(), name='gallery_edit'),
   
]