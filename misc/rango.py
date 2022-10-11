def rango(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=182) vamos bien
        Regresa estado = 187 -> acepto lexema
    """
    if estado == 182:
        if caracter == "r": estado = 183
        else: return -1, False, None
    elif estado == 183:
        if caracter == "a": estado = 184
        else: return -1, False, None
    elif estado == 184:
        if caracter == "n": estado = 185
        else: return -1, False, None
    elif estado == 185:
        if caracter == "g": estado = 186
        else: return -1, False, None
        return estado, False, None
    elif estado == 186:
        if caracter == "o": estado = 187
        else: return -1, False, None
    if estado == 187:
        return estado, False, "RANG"
    return estado, False, None
    