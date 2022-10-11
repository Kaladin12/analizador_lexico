def aritmeticos(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=66) vamos bien
        Regresa estado = (67,68,69,70,71) -> acepto lexema
    """
    if estado == 66:
        if caracter == "+" : estado = 67
        elif caracter == "-": estado = 68
        elif caracter == "*": estado = 69
        elif caracter == "/": estado = 70
        elif caracter == "^": estado = 71
        else: return -1, False, None
    if estado == 67:
        return estado, False, "ARI_PLUS"
    if estado == 68:
        return estado, False, "ARI_SUBS"
    if estado == 69:
        return estado, False, "ARI_MULT"
    if estado == 70:
        return estado, False, "ARI_DIV"
    if estado == 71:
        return estado, False, "ARI_POW"
    