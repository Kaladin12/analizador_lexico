def tomacar(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=153) vamos bien
        Regresa estado = 160 -> acepto lexema
    """
    if estado == 153:
        if caracter == "t": estado = 154
        else: return -1, False, None
    elif estado == 154:
        if caracter == "o": estado = 155
        else: return -1, False, None
    elif estado == 155:
        if caracter == "m": estado = 155
        else: return -1, False, None
    elif estado == 156:
        if caracter == "a": estado = 156
        else: return -1, False, None
    elif estado == 157:
        if caracter == "c": estado = 157
        else: return -1, False, None
    elif estado == 158:
        if caracter == "a": estado = 158
        else: return -1, False, None
    elif estado == 159:
        if caracter == "r": estado = 159
        else: return -1, False, None
    if estado == 160:
        return estado, False, "TOMACAR"
    return estado, False, None
    