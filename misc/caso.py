def caso(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=120) vamos bien
        Regresa estado = 124 -> acepto lexema
    """
    if estado == 120:
        if caracter == "c": estado = 121
        else: return -1, False, None
    elif estado == 121:
        if caracter == "a": estado = 122
        else: return -1, False, None
    elif estado == 122:
        if caracter == "s": estado = 123
        else: return -1, False, None
    elif estado == 123:
        if caracter == "o": estado = 124
        else: return -1, False, None
    if estado == 124:
        return estado, False, "CASO"
    return estado, False, None
    