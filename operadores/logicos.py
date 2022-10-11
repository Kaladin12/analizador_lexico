def logicos(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=84) vamos bien
        Regresa estado = (85,86) -> acepto lexema
    """
    if estado == 84:
        if caracter == "&" : estado = 85
        elif caracter == "|": estado = 86
        else: return -1, False, None
    if estado == 85:
        return estado, False, "AND"
    if estado == 86:
        return estado, False, "OR"