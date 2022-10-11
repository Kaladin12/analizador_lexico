def val_flotante(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=22) vamos bien
        Regresa estado = 26 -> acepto lexema
    """
    if estado == 34:
        if caracter.isnumeric(): estado = 35
        else: return -1, False, None
    elif estado == 35:
        if caracter.isnumeric(): estado = 35
        elif caracter == ".": estado = 36
        else: return -1, False, None
    elif estado == 36:
        if caracter.isnumeric(): estado = 37
        else: return -1, False, None
    elif estado == 37:
        if caracter.isnumeric(): estado = 37
        else: estado = 38
    if estado == 38:
        return estado, True, "VAL_FLOT"
    return estado, False, None
    