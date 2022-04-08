from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("user", "book", "end_at", "plated_end_at")
        labels = {"user": "user",
                  "book": "book",
                  "end_at": "Return date (%Y-%m-d %H:%M:S)",
                  "plated_end_at": "Planned return (%Y-%m-d %H:%M:S)"
                  }
