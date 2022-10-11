def en(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=206) vamos bien
        Regresa estado = 208 -> acepto lexema
    """
    if estado == 206:
        if caracter == "e": estado = 207
        else: return -1, False, None
    elif estado == 207:
        if caracter == "e": estado = 208
        else: return -1, False, None
    if estado == 208:
        return -1, False, "EN"