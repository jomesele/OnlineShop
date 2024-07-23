from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ስም' , 'ስልክ', 'email', 'ከተማ',
                  'የአካባቢዎ_ልዩ_ስም']
    

