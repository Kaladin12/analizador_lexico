def oprel_(estado, caracter):
    """
        En cada return, hay tres parametros:
            estado:
                -1 significa error
                cualquier otro: vamos bien
            regresa
                quitamos o no el ultimo caracter leido de la cadena
            tipo    
                None: significa que aun no encontramos lexema (y en algun punto error)
                "": tipo del lexema

    """
    if estado == 72: # case 0 
        if caracter == "=": estado = 73
        elif caracter == ">": estado = 76
        elif caracter == "<": estado = 79
        elif caracter == "!": estado = 82
        else: return -1, False, None
        return estado, False, None
    elif estado == 73:
        if caracter == "=": estado = 74
        else: estado = 75
    if estado == 74:
        return estado, False, "OP_IGIG"
    if estado == 75: 
        return estado, True, "OP_ASIG"
    
    elif estado == 76:
        if caracter == "=": estado = 78
        else: estado = 77
    if estado == 77:
        return estado, True, "OP_MAY"
    if estado == 78: 
        return estado, False, "OP_MAI"

    elif estado == 79:
        if caracter == "=": estado = 81
        else: estado = 80
    if estado == 80:
        return estado, True, "OP_MEN"
    if estado == 81: 
        return estado, False, "OP_MEI"    

    elif estado == 82:
        if caracter == "=": estado = 83
        else: return -1, False, None
    if estado == 83:
        return estado, False, "OP_DIF"
    return estado, False, None
