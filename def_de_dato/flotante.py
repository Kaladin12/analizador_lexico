def flotante(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=7) vamos bien
        Regresa estado = 15 -> acepto lexema
    """
    estado_inicial = estado
    if estado == 7:
        if caracter == "f": estado = 8
        else: return -1, False, None
    elif estado == 8:
        if caracter == "l": estado = 9
        else: return -1, False, None
    elif estado == 9:
        if caracter == "o": estado = 10
        else: return -1, False, None
    elif estado == 10:
        if caracter == "t": estado = 11
        else: return -1, False, None
    elif estado == 11:
        if caracter == "a": estado = 12
        else: return -1, False, None
    elif estado == 12:
        if caracter == "n": estado = 13
        else: return -1, False, None
    elif estado == 13:
        if caracter == "t": estado = 14
        else: return -1, False, None
    elif estado == 14:
        if caracter == "e": estado = 15
        else: return -1, False, None
    if estado == 15:
        return estado, False, "FLOTANTE"
    
    return estado, False, None