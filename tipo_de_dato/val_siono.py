def val_verdadero(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=42) vamos bien
        Regresa estado = 51 -> acepto lexema
    """
    if estado == 42:
        if caracter == "v" : estado = 43
        else: return -1, False, None
    elif estado == 43:
        if caracter == "e": estado = 44
        else: return -1, False, None
    elif estado == 44:
        if caracter == "r": estado = 45
        else: return -1, False, None
    elif estado == 45:
        if caracter == "d": estado = 46
        else: return -1, False, None
    elif estado == 46:
        if caracter == "a": estado = 47
        else: return -1, False, None
    elif estado == 47:
        if caracter == "d": estado = 48
        else: return -1, False, None
    elif estado == 48:
        if caracter == "e": estado = 49
        else: return -1, False, None
    elif estado == 49:
        if caracter == "r": estado = 50
        else: return -1, False, None
    elif estado == 50:
        if caracter == "o": estado = 51
        else: return -1, False, None
    if estado == 51:
        return estado, False, "VAL_SIONO"
    return estado, False, None
    
def val_falso(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=52) vamos bien
        Regresa estado = 57 -> acepto lexema
    """
    if estado == 52:
        if caracter == "f" : estado = 53
        else: return -1, False, None
    elif estado == 53:
        if caracter == "a": estado = 54
        else: return -1, False, None
    elif estado == 54:
        if caracter == "l": estado = 55
        else: return -1, False, None
    elif estado == 55:
        if caracter == "s": estado = 56
        else: return -1, False, None
    elif estado == 56:
        if caracter == "o": estado = 57
        else: return -1, False, None
    if estado == 57:
        return estado, True, "VAL_SIONO"
    return estado, False, None