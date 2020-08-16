from pprint import pprint

from django.core import serializers


def permisos(request):
    usuario = request.user
    perm = usuario.groups.all()
    urls = {'Administrativo': ''}
    return perm


def debg(data):
    d = serializers.serialize("json", data)
    pprint(d)
