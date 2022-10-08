def val_entero(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=39) vamos bien
        Regresa estado = 41 -> acepto lexema
    """
    if estado == 39:
        if caracter.isnumeric() : estado = 40
        else: return -1
    elif estado == 40:
        if caracter.isnumeric(): estado = 40
        else: estado = 41
    if estado == 41:
        print("Entero")
    return estado
    