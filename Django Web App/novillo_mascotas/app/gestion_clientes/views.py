from django.contrib.auth.models import Permission, User
from django.shortcuts import render, HttpResponse, redirect
from .forms import ClienteFormulario, MascotaFormulario
from app.modelo.models import Cliente, Mascota
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = 'Veterinario').exists():
        listaCliente = Cliente.objects.all().order_by('apellidos')
        return render(request,'clientes/principal.html', locals())
    else:
        return render(request,'login/aceso_prohibido.html', locals())

@login_required
def mascota(request):
    usuario = request.user
    if usuario.groups.filter(name = 'Cliente').exists() or usuario.groups.filter(name = 'Veterinario').exists():
        listaMascotas = Mascota.objects.all().order_by('nombre')
        return render(request,'clientes/mascotas.html', locals())
    else:
        return render(request,'login/aceso_prohibido.html', locals())

def crear(request): 
    formulario_cliente = ClienteFormulario(request.POST)
    formulario_mascota = MascotaFormulario(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid() and formulario_mascota.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.email = datos_cliente.get('email')
            cliente.celular = datos_cliente.get('celular')
            cliente.save()
            mascota = Mascota()
            datos_mascota = formulario_mascota.cleaned_data
            mascota.nombre = datos_mascota.get('nombre')
            mascota.raza = datos_mascota.get('raza')
            mascota.altura = datos_mascota.get('altura')
            mascota.tipo = datos_mascota.get('tipo')
            mascota.cliente = cliente
            mascota.save()
            return redirect(index)
    return render(request, 'clientes/formulario_crear.html', locals())


def modificar(request):
    return HttpResponse('modificar cliente')
