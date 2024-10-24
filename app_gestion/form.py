from django import forms
from django.forms import DateField, DateInput, FloatField, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app_gestion.models import Pago


class DateInput(forms.DateInput):
    input_type = 'Date'


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.label

# asentar_pago - Asentar un pago -
class asentar_pagoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(asentar_pagoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control alto'

        # self.fields['monto'].widget.input_type = 'text' #Pasa el campo numerico a texto          
        # self.fields['monto'].widget.attrs.update(
        #     {'required': True, 
        #      'class': 'form-control input-numero', 'onchange': "Calcular()"})
              
        # self.fields['monto_procesar'].widget.input_type = 'text' #Pasa el campo numerico a texto          
        # self.fields['monto_procesar'].widget.attrs.update(
        #     {'readonly': True,
        #      'class': 'form-control input-numero'})
       
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['observacion'].widget.attrs['rows'] = 3
       
    class Meta:
        model = Pago
        fields = ('fecha', 'referencia', 'forma', 'monto','tasa',
                  'monto_procesar', 'banco_destino', 'observacion')

    fecha = forms.DateField(widget=DateInput)
    

