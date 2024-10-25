from django import forms
from .models import CapOrder

class CapOrderForm(forms.ModelForm):
    class Meta:
        model = CapOrder
        fields = '__all__'  # You can specify specific fields if needed
