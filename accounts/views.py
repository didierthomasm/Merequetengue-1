from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.urls import reverse
from django.views.generic import FormView

from accounts.forms import RegisterPegosteadorForm


# ToDo:
#  1. Implement creation of Profile/About Me for a newly registered pegosteador. The idea is to create a Pegoste
#    so new model has to be created only for the profile, if anything, extend Pegoste for this porpoise.
#  2. Once the Profile is implemented, add as part of registration as an optional step.
class RegisterPegosteadorView(FormView):
    """
    Taking advantage of generic view class FormView to implement the form RegisterPegosteadorForm,
    which extends UserCreationForm, therefore continuing the use of standard functionality.
    """
    
    form_class = RegisterPegosteadorForm
    template_name = 'accounts/register_pegosteador.html'

    # ToDo: Implement permissions to pegosteador (User) level, to restrict the addition of pegostes
    #  only to the authenticated pegosteador, and that can only update pegostes belonging to that pegosteador.
    def form_valid(self, form):
        """
        This override will add the default Group "Pegosteadores" to set the permissions to add and
        update pegostes in Fandago application.

        :param form: An instance of the form class implemented by this view.
        :return: The validated form produced by the parent method.
        """
        pegosteadores = Group.objects.get(name='Pegosteadores')
        new_pegosteador = form.save()
        new_pegosteador.refresh_from_db()
        new_pegosteador.groups.add(pegosteadores)
        new_pegosteador.save()
        form.save_m2m()

        return super().form_valid(form)

    def get_success_url(self):
        """
        Override to authenticate and login the newly registered pegosteador, and then redirect it to the "home" of
        that pegosteador.

        :return: The URL to the home of the newly created pegosteador.
        """
        form_kwargs = self.get_form_kwargs()
        data = form_kwargs.get('data')
        pegosteador_auth = authenticate(username=data.get('username'), password=data.get('password1'))
        login(self.request, pegosteador_auth)

        return reverse('Fandango:pegosteador_home', kwargs={'username': data.get('username')})
