from django import forms
from .models import Rapiest

class RapistForm(forms.ModelForm):
    class Meta:
        model = Rapiest
        fields = '__all__'

