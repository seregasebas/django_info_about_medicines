from django.contrib.auth.forms import UserCreationForm
from .models import MedUser

class RegistrationForm(UserCreationForm):

    class Meta:
        model = MedUser
        fields = ('username', 'password1', 'password2', 'email')
