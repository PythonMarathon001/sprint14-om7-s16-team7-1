from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name",
                  "email", "password", "role", "is_active")
        labels = {"first_name": "Name",
                  "middle_name": "Middle name",
                  "last_name": "Surname",
                  "email": "Email",
                  "password": "password",
                  "role": "Role",
                  "is_active": "As active"
                  }



