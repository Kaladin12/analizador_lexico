def val_flotante(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=22) vamos bien
        Regresa estado = 26 -> acepto lexema
    """
    if estado == 34:
        if caracter.isNumeric(): estado = 35
        else: return -1
    elif estado == 35:
        if caracter == "u": estado = 36
        else: return -1
    elif estado == 36:
        if caracter == "l": estado = 25
        else: return -1
    elif estado == 37:
        if caracter == "o": estado = 26
        else: return -1
    if estado == 38:
        print("TipoDato_Flotante")
    return estado
    