from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User
from django import forms

class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = PerfilForm(instance=request.user)
    if request.htmx:
        return render(request, 'perfil_formulario.html', {'form': form})
    return render(request, 'perfil_detalle.html', {'form': form})
