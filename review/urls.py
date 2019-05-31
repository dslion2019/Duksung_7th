from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('rpost/', views.rpost, name='rpost'), # 글쓰기
    path('rshow/', views.rshow, name='rshow'), # 전체 글 보기
    path('<int:pk>/redit/', views.redit, name='redit'), # 폼 수정
    path('<int:pk>/delete/', views.delete, name='delete'), #폼 삭제
]