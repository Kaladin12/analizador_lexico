def dormir(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=161) vamos bien
        Regresa estado = 167 -> acepto lexema
    """
    if estado == 161:
        if caracter == "d": estado = 162
        else: return -1, False, None
    elif estado == 162:
        if caracter == "o": estado = 163
        else: return -1, False, None
    elif estado == 163:
        if caracter == "r": estado = 164
        else: return -1, False, None
    elif estado == 164:
        if caracter == "m": estado = 165
        else: return -1, False, None
    elif estado == 165:
        if caracter == "i": estado = 166
        else: return -1, False, None
    elif estado == 166:
        if caracter == "r": estado = 167
        else: return -1, False, None
    if estado == 167:
        return estado, False, "DORMIR"
    return estado, False, None
    