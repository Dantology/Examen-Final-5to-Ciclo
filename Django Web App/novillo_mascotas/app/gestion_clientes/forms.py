from django import forms
from app.modelo.models import Cliente, Mascota


class ClienteFormulario (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos","celular", "email"]
        widgets = {
            'cedula': forms.TextInput(attrs={'placeholder': 'Ingrese Cédula', 'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese Apellidos', 'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese Nombres', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese Correo Electrónico', 'class': 'form-control col-md-8', 'type': 'email'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ingrese Celular', 'class': 'form-control col-md-8'}),
        }


class MascotaFormulario (forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "raza", "altura","tipo"]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre de la mascota', 'class': "form-control"}),
            'raza': forms.TextInput(attrs={'placeholder': 'Ingrese la raza', 'class': "form-control"}),
            'altura': forms.TextInput(attrs={'placeholder': 'Ingrese la altura en metros', 'class': "form-control"}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Ingrese el tipo de mascota', 'class': "form-control"}),
        }
