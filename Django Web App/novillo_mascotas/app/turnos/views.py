from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from app.helpers.helpers import permisos, debg
from app.modelo.models import Cliente, Mascota, Turno
from app.turnos.forms import TurnoFormulario


@login_required
def index(request):
    usuario = request.user
    group_permissions = permisos(request)
    cliente = None
    mascotas = None
    if usuario.groups.filter(name='Veterinario').exists():
        querySet = request.GET.get('cedula')
        if querySet:
            cliente = Cliente.objects.get(cedula=querySet)
            pprint(cliente.nombres)
            # debg(cliente)
            mascotas = Mascota.objects.filter(cliente=cliente.cliente_id)
    return render(request, 'turnos/index.html',
                  {'group_permissions': group_permissions, 'cliente': cliente, 'mascotas': mascotas})


def turnoSolicitud(request, cedula, nombre):
    usuario = request.user
    group_permissions = permisos(request)
    cliente = None
    mascotas = None
    if usuario.groups.filter(name='Veterinario').exists():
        formulario = TurnoFormulario(request.POST)
        cliente = Cliente.objects.all().filter(cedula=cedula)[0]
        mascotas = Mascota.objects.all().filter(nombre=nombre)[0]
        if request.method == 'POST':
            if formulario.is_valid():
                datos = formulario.cleaned_data
                turno = Turno()
                turno.descripcion = datos.get('descripcion')
                turno.responsable = usuario.id
                turno.mascota = mascotas
                turno.save()

        else:
            return render(request, 'turnos/solicitud.html', locals())
    return render(request, 'turnos/index.html')
