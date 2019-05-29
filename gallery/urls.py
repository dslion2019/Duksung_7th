from django.urls import path

from .views import HomePageView, CreatePostView, DetailPostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('gallery/<pk>', DetailPostView.as_view(), name='detail_post')
   
]