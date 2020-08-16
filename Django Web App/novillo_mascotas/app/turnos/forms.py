from django import forms
from app.modelo.models import Turno

class TurnoFormulario(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ["descripcion"]
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'})
        }