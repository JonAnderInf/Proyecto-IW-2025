from django import forms
from .models import Ticket, Empleado, Equipo

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'  
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
