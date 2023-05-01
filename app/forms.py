from django import forms
from app.models import *
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'email': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Unesite Vaš email'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'email': _(''),
            'question_text': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Unesite Vaš email'
        self.fields['question_text'].widget.attrs['placeholder'] = 'Unesite Vaše pitanje'

        
class ReservationForm(forms.ModelForm):
    projection = forms.ModelChoiceField(queryset=Projection.objects.order_by('movie__title'))
    
    class Meta:
        model = Reservation
        fields = '__all__'
        labels = {
            'first_name': _(''),
            'last_name': _(''),
            'email': _(''),
            'number_of_tickets': _(''),
            'projection': _(''),
        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Unesite Vaše ime'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Unesite Vaše prezime'
        self.fields['email'].widget.attrs['placeholder'] = 'Unesite Vaš email'
        self.fields['number_of_tickets'].widget.attrs['placeholder'] = 'Unesite broj karata'
        self.fields['projection'].label = ''
        