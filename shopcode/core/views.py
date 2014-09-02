from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from core.models import Client

from .forms import RegisterForm


class RegisterClientView(CreateView):
    form_class = RegisterForm
    template_name = 'register_client.html'
    success_url = '/'

    def form_valid(self, form):
        domain_url = form.cleaned_data['domain_url']
        description = form.cleaned_data['description']
        first_name = form.cleaned_data['first_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # Create client
        user = User.objects.create_user(
            username, email, password
        )
        user.first_name = first_name
        user.save()
        client = Client(
            domain_url=domain_url,
            schema_name=username,
            description=description,
        )
        client.user = user
        client.save()
        return super(RegisterClientView, self).form_valid(form)
