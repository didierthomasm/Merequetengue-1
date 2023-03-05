from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from Fandango.models import Pegoste


class HomePage(TemplateView):
    template_name = 'Fandango/home.html'


class PegostesList(ListView):
    template_name = 'Fandango/pegostes_list.html'
    model = Pegoste


class PegosteView(DetailView):
    template_name = 'Fandango/pegoste.html'
    model = Pegoste


class CreatePegoste(CreateView):
    model = Pegoste
    template_name = 'Fandango/create_pegoste.html'
    fields = '__all__'
    success_url = reverse_lazy('pegostes_list')
