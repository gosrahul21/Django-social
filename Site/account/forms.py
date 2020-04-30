from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django  import forms
from account import models

class UserCreateForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=(
            "username","email","password1","password2"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

