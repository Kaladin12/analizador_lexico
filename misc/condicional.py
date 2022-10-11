def condicional(estado, caracter):
    """
        Regresa -1 -> fallo (va a siguiente diagrama)
        Regresa estado (>=87) vamos bien
        Regresa estado = (90,92) -> acepto lexema
    """
    if estado == 87:
        if caracter=="s": estado = 88
        else: return -1, False, None
    elif estado == 88:
        if caracter=="i": estado = 89
        else: return -1, False, None
    elif estado == 89:
        if caracter=="n": estado = 91
        elif not caracter.isalpha(): estado = 90
        else: return -1, False, None
    elif estado == 91:
        if caracter=="o": estado = 92
        else: return -1, False, None
    if estado == 90:
        
        return estado, False, "COND_IF"
    
    if estado == 92: return estado, False, "COND_ELSE" 
    return estado, False, None
    