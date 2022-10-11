def val_cadena(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=58) vamos bien
        Regresa estado = 60 -> acepto lexema
    """
    if estado == 58:
        if caracter=='"' : estado = 59
        else: return -1, False, None
    elif estado == 59:
        if caracter == '"': estado = 60
        elif isinstance(caracter, str): estado = 59
        else: return -1, False, None
    
    if estado == 60:
        return estado, False, "VAL_CAD"
    return estado, False, None