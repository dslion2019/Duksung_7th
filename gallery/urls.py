from django.urls import path

from .views import HomePageView, CreatePostView, DetailPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gallery/add/', CreatePostView.as_view(), name='add_post'),
    path('gallery/<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('gallery/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
   
]