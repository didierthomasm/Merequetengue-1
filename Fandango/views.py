from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from Fandango.models import Pegoste


class HomePage(TemplateView):
    template_name = 'Fandango/home.html'


class Pegostes(ListView):
    model = Pegoste
    template_name = 'Fandango/pegostes.html'

    def get_queryset(self):
        return self.model.objects.filter(author__username=self.kwargs['username'])


class PegosteView(DetailView):
    model = Pegoste
    template_name = 'Fandango/pegoste_view.html'
    slug_field = 'slug'

    def get_queryset(self):
        return self.model.objects.filter(author__username=self.kwargs['username'])


class RedirectSlugPegoste(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pegoste = get_object_or_404(Pegoste, pk=kwargs['pk'])
        return pegoste.get_absolute_url()


# The mixin view LoginRequiredMixin implements the authentication mechanisms, so there is no
# need to implement additional functionality or validations.
#
# The default behavior of the mixin is to redirect to the login URL. The default value of "login_url" attribute
# of LoginRequiredMixin is the value in settings.LOGIN_URL, that its default value is 'accounts/login'.
# In this case, LoginRequiredMixin will use defaults.
#
#   Reference:
#     https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-loginrequiredmixin-mixin
#     https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-LOGIN_URL
class AddPegoste(LoginRequiredMixin, CreateView):
    model = Pegoste
    fields = '__all__'
    template_name = 'Fandango/add_update_pegoste.html'


class UpdatePegoste(LoginRequiredMixin, UpdateView):
    model = Pegoste
    fields = '__all__'
    template_name = 'Fandango/add_update_pegoste.html'
