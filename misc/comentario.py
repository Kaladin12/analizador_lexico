def comentario(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=204) vamos bien
        Regresa estado = 205 -> acepto lexema
    """
    if estado == 204:
        if caracter == "#": estado = 205
        else: return -1, False, None
    elif estado == 205:
        if caracter == '\\': estado = 205.1
        else: estado = 205
    elif estado == 205.1:
        if caracter == 'n': estado = 205.2
        else: return -1, False, None
    if estado == 205.2:
        return estado, False, "COMENTARIO"
    return estado, False, None