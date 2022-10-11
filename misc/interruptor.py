def interruptor(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=93) vamos bien
        Regresa estado = 104 -> acepto lexema
    """
    if estado == 93:
        if caracter == "i": estado = 94
        else: return -1, False, None
    elif estado == 94:
        if caracter == "n": estado = 95
        else: return -1, False, None
    elif estado == 95:
        if caracter == "t": estado = 96
        else: return -1, False, None
    elif estado == 96:
        if caracter == "e": estado = 97
        else: return -1, False, None
    elif estado == 97:
        if caracter == "r": estado = 98
        else: return -1, False, None
    elif estado == 98:
        if caracter == "r": estado = 99
        else: return -1, False, None
    elif estado == 99:
        if caracter == "u": estado = 100
        else: return -1, False, None
    elif estado == 100:
        if caracter == "p": estado = 101
        else: return -1, False, None
    elif estado == 101:
        if caracter == "t": estado = 102
        else: return -1, False, None
    elif estado == 102:
        if caracter == "o": estado = 103
        else: return -1, False, None
    elif estado == 103:
        if caracter == "r": estado = 104
        else: return -1, False, None
    if estado == 104:
        return estado, False, "INTER"
    return estado, False, None
    