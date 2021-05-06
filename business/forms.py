from django.forms import ModelForm,Textarea
from .models import USP, Business



class USPForm(ModelForm):
    class Meta:
        model = USP
        fields = ['description', 'business']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 3}),
        }

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['user']
