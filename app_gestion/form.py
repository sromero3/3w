from django import forms
from django.forms import DateField, DateInput, FloatField, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app_gestion.models import Pago, Documento, Cliente


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
    

    # 
class agregar_documentoForm(ModelForm):
  
    def __init__(self, *args, **kwargs):
        super(agregar_documentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control alto'
       
        self.fields['monto'].widget.input_type = 'text' #Pasa el campo numerico a texto          
        self.fields['monto'].widget.attrs.update(
            {'required': True, 'maxlength': '10',
             'class': 'form-control input-numero alto'})
        
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['observacion'].widget.attrs['rows'] = 3

    class Meta:
        model = Documento
        fields = ('numero','cliente','fecha','vencimiento','monto','observacion','iva')
 
        widgets = {
            'fecha': DateInput(format=('%Y-%m-%d')),
            'vencimiento': DateInput(format=('%Y-%m-%d'))
        }

# agregar cliente 
class agregar_clienteForm(ModelForm):
  
    def __init__(self, *args, **kwargs):
        super(agregar_clienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control alto'

        
        self.fields['correo'].widget.input_type = 'email' #Pasa el campo numerico a email  
        
        self.fields['ced_rif'].widget.attrs.update(
            {'maxlength': '8', 'minlength': '7',
             'onkeypress': "return soloNumeros(event)"
             })
       
        self.fields['telefono'].widget.attrs.update(
            {'maxlength': '7', 'minlength': '7',
             'onkeypress': "return soloNumeros(event)"
             })
        
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['observacion'].widget.attrs['rows'] = 3

    class Meta:
        model = Cliente
        fields = ('ced_rif','nombre','telefono','correo','direccion','ciudad','vendedor','status','observacion')
 
        # widgets = {
        #     'fecha': DateInput(format=('%Y-%m-%d')),
        #     'vencimiento': DateInput(format=('%Y-%m-%d'))
        # }




