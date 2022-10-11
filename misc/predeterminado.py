def predeterminado(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=105) vamos bien
        Regresa estado = 119 -> acepto lexema
    """
    if estado == 105:
        if caracter == "p": estado = 106
        else: return -1, False, None
    elif estado == 106:
        if caracter == "r": estado = 107
        else: return -1, False, None
    elif estado == 107:
        if caracter == "e": estado = 108
        else: return -1, False, None
    elif estado == 108:
        if caracter == "d": estado = 109
        else: return -1, False, None
    elif estado == 109:
        if caracter == "e": estado = 110
        else: return -1, False, None
    elif estado == 110:
        if caracter == "t": estado = 111
        else: return -1, False, None
    elif estado == 111:
        if caracter == "e": estado = 112
        else: return -1, False, None
    elif estado == 112:
        if caracter == "r": estado = 113
        else: return -1, False, None
    elif estado == 113:
        if caracter == "m": estado = 114
        else: return -1, False, None
    elif estado == 114:
        if caracter == "i": estado = 115
        else: return -1, False, None
    elif estado == 115:
        if caracter == "n": estado = 116
        else: return -1, False, None
    elif estado == 116:
        if caracter == "a": estado = 117
        else: return -1, False, None
    elif estado == 117:
        if caracter == "d": estado = 118
        else: return -1, False, None
    elif estado == 118:
        if caracter == "o": estado = 119
        else: return -1, False, None
    if estado == 119:
        return estado, False, "PRED"
    return estado, False, None
    