def entero(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=0) vamos bien
        Regresa estado = 6 -> acepto lexema
    """
    if estado == 0:
        if caracter == "e": estado = 1
        else: return -1, False, None
    elif estado == 1:
        if caracter == "n": estado = 2
        else: return -1, False, None
    elif estado == 2:
        if caracter == "t": estado = 3
        else: return -1, False, None
    elif estado == 3:
        if caracter == "e": estado = 4
        else: return -1, False, None
    elif estado == 4:
        if caracter == "r": estado = 5
        else: return -1, False, None
    elif estado == 5:
        if caracter == "o": estado = 6
        else: return -1, False, None
    if estado == 6:
        return estado, False, "ENTERO"
    return estado, False, None
    