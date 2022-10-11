def agrupacion(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=61) vamos bien
        Regresa estado = (62, 63, 64,65) -> acepto lexema
    """
    if estado == 61:
        if caracter == "(" : estado = 62
        elif caracter == ")": estado = 63
        elif caracter == "{": estado = 64
        elif caracter == "}": estado = 65
        else: return -1, False, None
    if estado == 62:
        return estado, False, "AGR_OP"
    if estado == 63:
        return estado, False, "AGR_CP"
    if estado == 64:
        return estado, False, "AGR_OB"
    if estado == 65:
        return estado, False, "AGR_CB"
    