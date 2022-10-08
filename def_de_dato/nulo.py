def nulo(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=22) vamos bien
        Regresa estado = 26 -> acepto lexema
    """
    if estado == 22:
        if caracter == "n": estado = 23
        else: return -1, False
    elif estado == 23:
        if caracter == "u": estado = 24
        else: return -1, False
    elif estado == 24:
        if caracter == "l": estado = 25
        else: return -1, False
    elif estado == 25:
        if caracter == "o": estado = 26
        else: return -1, False
    if estado == 26:
        print("Nulo")
    return estado, False
    