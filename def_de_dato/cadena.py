def cadena(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=27) vamos bien
        Regresa estado = 33 -> acepto lexema
    """
    if estado == 27:
        if caracter == "c": estado = 28
        else: return -1, False, None
    elif estado == 28:
        if caracter == "a": estado = 29
        else: return -1, False, None
    elif estado == 29:
        if caracter == "d": estado = 30
        else: return -1, False, None
    elif estado == 30:
        if caracter == "e": estado = 31
        else: return -1, False, None
    elif estado == 31:
        if caracter == "n": estado = 32
        else: return -1, False, None
    elif estado == 32:
        if caracter == "a": estado = 33
        else: return -1, False, None
    if estado == 33:
        return estado, True, "CADENA"
    return estado, False, None
    