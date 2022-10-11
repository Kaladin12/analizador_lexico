def im(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=168) vamos bien
        Regresa estado = (176, 181) -> acepto lexema
    """
    if estado == 168:
        if caracter == "i": estado = 169
        else: return -1, False, None
    elif estado == 169:
        if caracter == "m": estado = 170
        else: return -1, False, None
    elif estado == 170:
        if caracter == "p": estado = 171
        else: return -1, False, None
    elif estado == 171:
        if caracter == "r": estado = 172
        elif caracter == "o": estado = 177
        else: return -1, False, None
        return estado, False, None
    elif estado == 172:
        if caracter == "i": estado = 173
        else: return -1, False, None
    elif estado == 173:
        if caracter == "m": estado = 174
        else: return -1, False, None
    elif estado == 174:
        if caracter == "i": estado = 175
        else: return -1, False, None
    elif estado == 175:
        if caracter == "r": estado = 176
        else: return -1, False, None
    if estado == 176:
        return estado, False, "IMPR"
    elif estado == 177:
        if caracter == "r": estado = 178
        else: return -1, False, None
    elif estado == 178:
        if caracter == "t": estado = 179
        else: return -1, False, None
    elif estado == 179:
        if caracter == "a": estado = 180
        else: return -1, False, None
    elif estado == 180:
        if caracter == "r": estado = 181
        else: return -1, False, None
    if estado == 181:
        return estado, False, "IMPO"
    return estado, False, None
    