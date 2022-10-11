def identificador(estado, caracter):
    if estado == 209:
        if caracter!=" " and caracter.isalpha() or caracter == "_": estado = 210
        else: return -1, False, None
    elif estado == 210:
        if caracter.isalpha() or caracter.isnumeric() or  caracter == "-" or caracter == "_": estado = 210
        else: 
            estado = 211
            #print("Identificador", '-'+caracter+'-') 
            return estado, True, "ID" # tambien quiero que se regrese #holamundo= holamundo? regresa() y acepta() 
    return estado, False, None
    