from pypro.modulos import facada


def listar_modulos(requests):
    return {'MODULOS': facada.listar_modulos_ordenados()}
