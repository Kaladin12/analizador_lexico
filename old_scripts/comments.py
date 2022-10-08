recupera = False

def fallo(inicio = 0):
    global estado
    global recupera
    if inicio == 0: return 3
    elif inicio == 3: return 8
    elif inicio == 8 and not recupera: 
        recupera = True
        return 0
    else: 
        print('Error de compilador')
        return None

def esLetra(caracter:str):
    if caracter.isalpha(): 
        return True
    return False

def esNumero(caracter):
    #print('numerico', caracter.isnumeric(), len(caracter), caracter)
    if caracter.isnumeric(): 
        return True
    return False

encontro_lexema = False
cadena = '(* //\\n *) { cor } // lin \\n //\\n'
super_cadena_original = cadena
estado = 0
inicio = 0
final = 0
inicio_subcadena = 0
def cosa(cadena, estado):
    global encontro_lexema
    global inicio
    global final
    global inicio_subcadena
    global super_cadena_original
    caracter = ''
    cadena_original = cadena
    while True:
        if len(cadena) != 0 :
            caracter = cadena[0]
            cadena  = cadena [1:]
            
        print('dentro: ',caracter, cadena, estado)
        if estado == 0: # case 0 
            if caracter == "{": estado = 1
            else: break
        elif estado == 1:
            """if len(cadena) != 0 :
                caracter = cadena[0]"""
            if caracter == "}": estado = 2
            else: estado = 1
        elif estado == 2:
            #cadena  = cadena [1:]
            print(inicio_subcadena, final)
            print(f"devuelve(Multiline brackets, {super_cadena_original[inicio_subcadena:final]})") # AGREGAR EL COMENTARIO RECUPERADO {  }
            inicio_subcadena = final+1
            encontro_lexema = True
            break
        elif estado == 3:
            if caracter == "(": estado = 4
            else: break
        elif estado == 4:
            if caracter == "*": estado = 5
            else: break
        elif estado == 5:
            if caracter == "*": estado = 6
            else: estado = 5
        elif estado == 6:
            """if len(cadena) != 0 :
                caracter = cadena[0]"""
            if caracter == ")": estado = 7
            else: break
        elif estado == 7:
            print(inicio_subcadena, final)
            print(f"devuelve(Multilinea parentesis, {super_cadena_original[inicio_subcadena:final]}") # AGREGAR EL COMENTARIO RECUPERADO MULTILINE (* *)
            inicio_subcadena = final+1
            encontro_lexema = True
            break
        elif estado == 8:
            if caracter == "/": estado = 9
            else: break
        elif estado == 9:
            if caracter == "/": estado = 10
            else: break
        elif estado == 10:
           if caracter == "\\": estado = 11
           else: estado = 10
        elif estado == 11:
            """if len(cadena) != 0 :
                caracter = cadena[0]"""
            if caracter == "n": estado = 12
            else: break
        elif estado == 12:
            print(inicio_subcadena, final)
            print(f"devuelve(single line, {super_cadena_original[inicio_subcadena:final]})") # AGREGAR EL COMENTARIO RECUPERADO SINGLELINE //
            inicio_subcadena = final+1
            encontro_lexema = True
            break

        final += 1

    if not encontro_lexema:
        return cadena_original[1:] if len(cadena_original)> 0 and cadena_original[0]==" " else cadena_original

    return cadena[1:] if len(cadena)>0 and cadena[0] == " " else cadena

while len(cadena)!=0:
    cadena = cosa(cadena, estado)
    if inicio == None:
        break
    inicio = fallo(inicio)
    if inicio == None:
        break
    estado = inicio
    
    #print('cadena: [', cadena, estado, encontro_lexema, recupera)
    if encontro_lexema:
        final = inicio_subcadena
        recupera = False
    print('fuera',inicio_subcadena, final)
    encontro_lexema = False
    
    