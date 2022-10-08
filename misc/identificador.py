def identificador(estado, caracter):
    if estado == 209:
        if caracter.isalpha() or caracter == "_": estado = 210
        else: return -1, False
    elif estado == 210:
        if caracter.isalpha() or caracter.isnumeric() or caracter == "_": estado = 210
        else: 
            estado = 211
            print("Identificador") 
            return estado, True # tambien quiero que se regrese #holamundo= holamundo? regresa() y acepta() 
    return estado, False
    