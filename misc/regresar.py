def regresar(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=144) vamos bien
        Regresa estado = 152 -> acepto lexema
    """
    if estado == 144:
        if caracter == "r": estado = 145
        else: return -1, False, None
    elif estado == 145:
        if caracter == "e": estado = 146
        else: return -1, False, None
    elif estado == 146:
        if caracter == "g": estado = 147
        else: return -1, False, None
    elif estado == 147:
        if caracter == "r": estado = 148
        else: return -1, False, None
    elif estado == 148:
        if caracter == "e": estado = 149
        else: return -1, False, None
    elif estado == 149:
        if caracter == "s": estado = 150
        else: return -1, False, None
    elif estado == 150:
        if caracter == "a": estado = 151
        else: return -1, False, None
    elif estado == 151:
        if caracter == "r": estado = 152
        else: return -1, False, None
    if estado == 152:
        return estado, True, "REGRS"
    return estado, False, None
    