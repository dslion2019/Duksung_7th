from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView

from schedule.models import Schedule


class ScheduleListView(ListView):
    template_name = 'schedule_list.html'
    model = Schedule


class ScheduleCreateView(RedirectView):
    url = reverse_lazy('list')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if title and start_date and end_date:
            Schedule.objects.create(title=title, start_date=start_date, end_date=end_date)
            return super(ScheduleCreateView, self).post(request, *args, **kwargs) 
        else:
            raise Http404


class ScheduleDeleteView(RedirectView):
    url = reverse_lazy('list')

    def get(self, request, *args, **kwargs):
        schedule = get_object_or_404(Event, pk=kwargs.get('pk'))
        schedule.delete()
        return super(ScheduleDeleteView, self).get(request, *args, **kwargs)