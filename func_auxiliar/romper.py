def romper(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=188) vamos bien
        Regresa estado = 194 -> acepto lexema
    """
    if estado == 188:
        if caracter == "r": estado = 189
        else: return -1, False, None
    elif estado == 189:
        if caracter == "o": estado = 190
        else: return -1, False, None
    elif estado == 190:
        if caracter == "m": estado = 191
        else: return -1, False, None
    elif estado == 191:
        if caracter == "p": estado = 192
        else: return -1, False, None
    elif estado == 192:
        if caracter == "e": estado = 193
        else: return -1, False, None
    elif estado == 193:
        if caracter == "r": estado = 194
        else: return -1, False, None
    if estado == 194:
        return estado, False, "ROMPER"
    return estado, False, None
    