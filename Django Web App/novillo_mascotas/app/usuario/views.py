from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from app.usuario.forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = 'Veterinario').exists() or usuario.groups.filter(name = 'Administrador').exists():
        listaUsuarios = User.objects.all().order_by('last_name')
        return render(request,'usuario/principal.html', locals())
    else:
        return render(request,'login/aceso_prohibido.html', locals())

class RegistroUsuario(CreateView):
    model = User
    template_name="usuario/registrar.html"
    form_class= RegistroUsuarioForm
    success_url=reverse_lazy('index')
