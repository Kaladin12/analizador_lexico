def cada(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=125) vamos bien
        Regresa estado = 129 -> acepto lexema
    """
    if estado == 125:
        if caracter == "c": estado = 126
        else: return -1, False, None
    elif estado == 126:
        if caracter == "a": estado = 127
        else: return -1, False, None
    elif estado == 127:
        if caracter == "d": estado = 128
        else: return -1, False, None
    elif estado == 128:
        if caracter == "a": estado = 129
        else: return -1, False, None
    if estado == 129:
        return estado, True, "CADA"
    return estado, False, None
    