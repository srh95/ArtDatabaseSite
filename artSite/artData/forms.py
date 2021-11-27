from django import forms
from .models import CustomerModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ["customer_id", "first_name", "last_name", "street_num","street_name", "city", "state", "zip_code", "preferred_style", "preferred_medium", "phone_num", "artist_id"]
