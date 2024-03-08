from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['carnet', 'nombres', 'apellidos', 'correo_electronico', 'fecha_nacimiento']
        labels = {
            'carnet': 'Carnet',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'correo_electronico': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
