from django import forms
from .models import Usuario

class Formulario(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu email'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu contraseña'})
    )


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }