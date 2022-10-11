def comentario(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=204) vamos bien
        Regresa estado = 205 -> acepto lexema
    """
    if estado == 204:
        if caracter == "#": estado = 205
        else: return -1, False, None
    if estado == 205:
        return -1, False, "COMENTARIO"