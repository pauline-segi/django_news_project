from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    #this part above takes you back to the login page after you've created an account, with most websites, this is automated in the background so once you create the account, you don't need to login again --- this could be something we change on our website if we wanted so you're not having to login again
    template_name = 'users/createAccount.html'
