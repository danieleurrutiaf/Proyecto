from django import forms
from .models import Usuario, Genero

from django.forms import ModelForm


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_genero'].queryset = Genero.objects.all()