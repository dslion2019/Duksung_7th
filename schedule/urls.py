from django.urls import path
from schedule.views import ScheduleListView, ScheduleCreateView, ScheduleDeleteView


urlpatterns = [
    path('', ScheduleListView.as_view(), name='list'),
    path('create/', ScheduleCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(), name='delete'),
]