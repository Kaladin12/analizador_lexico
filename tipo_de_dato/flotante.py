def flotante(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=34) vamos bien
        Regresa estado = 26 -> acepto lexema
    """
    if estado == 34:
        if caracter.isnumeric(): estado = 35
        else: return -1
    elif estado == 35:
        if caracter.isnumeric(): estado = 36
        else: return -1
    elif estado == 36:
        if caracter == "l": estado = 37
        else: return -1
    elif estado == 37:
        if caracter == "o": estado = 38
        else: return -1
    if estado == 38:
        print("TipoDato_Flotante")
    return estado
    