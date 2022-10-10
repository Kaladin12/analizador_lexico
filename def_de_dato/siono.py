def siono(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=16) vamos bien
        Regresa estado = 21 -> acepto lexema
    """
    if estado == 16:
        if caracter == "s": estado = 17
        else: return -1, False, None
    elif estado == 17:
        if caracter == "i": estado = 18
        else: return -1, False, None
    elif estado == 18:
        if caracter == "o": estado = 19
        else: return -1, False, None
    elif estado == 19:
        if caracter == "n": estado = 20
        else: return -1, False, None
    elif estado == 20:
        if caracter == "o": estado = 21
        else: return -1, False, None
    if estado == 21:
        return estado, False, "SIONO"
    return estado, False, None
    