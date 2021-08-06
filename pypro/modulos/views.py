from django.shortcuts import render

from pypro.modulos import facada


def indice(request):
    ctx = {'modulos': facada.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = facada.encontrar_modulo(slug)
    aulas = facada.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facada.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
