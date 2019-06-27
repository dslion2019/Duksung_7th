from django.urls import path
from schedule.views import EventListView, EventCreateView, EventDeleteView


urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('create/', EventCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='delete'),
]