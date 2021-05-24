from django.forms import ModelForm,Textarea
from .models import USP, Business



class USPForm(ModelForm):
    class Meta:
        model = USP
        fields = ['description',]
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 3, 'class': 'uspfield', 'placeholder': 'Add new Usp', 'autocomplete':'off'}),
        }

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['user']
