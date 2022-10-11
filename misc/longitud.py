def longitud(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=195) vamos bien
        Regresa estado = 203 -> acepto lexema
    """
    if estado == 195:
        if caracter == "l": estado = 196
        else: return -1, False, None
    elif estado == 196:
        if caracter == "o": estado = 197
        else: return -1, False, None
    elif estado == 197:
        if caracter == "n": estado = 198
        else: return -1, False, None
    elif estado == 198:
        if caracter == "g": estado = 199
        else: return -1, False, None
    elif estado == 199:
        if caracter == "i": estado = 200
        else: return -1, False, None
    elif estado == 200:
        if caracter == "t": estado = 201
        else: return -1, False, None
    elif estado == 201:
        if caracter == "u": estado = 202
        else: return -1, False, None
    elif estado == 202:
        if caracter == "d": estado = 203
        else: return -1, False, None
    if estado == 203:
        return estado, False, "LONGITUD"
    return estado, False, None