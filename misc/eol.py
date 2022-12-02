def eol(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=125) vamos bien
        Regresa estado = 129 -> acepto lexema
    """
    #print(estado,'dentro')
    if estado == 212:
        if caracter == ";": estado = 213
        
        return estado, True, "EOL"
    return estado, False, None