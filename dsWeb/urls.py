from django.contrib import admin
from django.urls import path
import loginapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logoutok/', loginapp.views.logoutok, name='logoutok'),
    path('', loginapp.views.mainpage, name='mainpage'),
    path('login/', loginapp.views.loginpage, name='login'),
    path('logout/', loginapp.views.logout, name='logout'),
    path('signup/', loginapp.views.signuppage, name='signup'),
    path('signupok/', loginapp.views.singupok, name='signupok'),
    path('userlist/', loginapp.views.userlist, name='userlist'),
]
