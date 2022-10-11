def mientras(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=130) vamos bien
        Regresa estado = (139,143) -> acepto lexema
    """
    if estado == 130:
        if caracter == "m": estado = 131
        else: return -1, False, None
    elif estado == 131:
        if caracter == "i": estado = 132
        else: return -1, False, None
    elif estado == 132:
        if caracter == "e": estado = 133
        else: return -1, False, None
    elif estado == 133:
        if caracter == "n": estado = 134
        else: return -1, False, None
    elif estado == 134:
        if caracter == "t": estado = 135
        else: return -1, False, None
    elif estado == 135:
        if caracter == "r": estado = 136
        else: return -1, False, None
    elif estado == 136:
        if caracter == "a": estado = 137
        else: return -1, False, None
    elif estado == 137:
        if caracter == "s": estado = 138
        else: return -1, False, None
    elif estado == 138:
        if caracter == "-": estado = 140
        else: estado = 139
    elif estado == 140:
        if caracter == "h": estado = 141
        else: return -1, False, None
    elif estado == 141:
        if caracter == "a": estado = 142
        else: return -1, False, None
    elif estado == 142:
        if caracter == "z": estado = 143
        else: return -1, False, None
    if estado == 139:
        return estado, True, "MNTRS"
    if estado == 143:
        return estado, True, "HAZ_MNTRS"
    return estado, False, None
    