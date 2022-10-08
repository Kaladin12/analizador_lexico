recupera = False

def fallo(inicio = 0):
    global estado
    global recupera
    if inicio == 0: return 7
    elif inicio == 7: return 16
    elif inicio == 7: return 16
    elif inicio == 7: return 16
    elif inicio == 7: return 16
    elif inicio == 16 and not recupera: 
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
        
        if estado == 0:
            if caracter == "e": estado = 1
            else: break
        elif estado == 1:
            if caracter == "n": estado = 2
            else: break
        elif estado == 2:
            if caracter == "t": estado = 3
            else: break
        elif estado == 3:
            if caracter == "e": estado = 4
            else: break
        elif estado == 4:
            if caracter == "r": estado = 5
            else: break
        elif estado == 5:
            if caracter == "o": estado = 6
            else: break
        elif estado == 6:
            print("Entero")
        elif estado == 7:
           if caracter == "f": estado = 8
           else: break
        elif estado == 8:
            if caracter == "l": estado = 9
            else: break
        elif estado == 9:
            #print(inicio_subcadena, final)
            #print(f"devuelve(single line, {super_cadena_original[inicio_subcadena:final]})") # AGREGAR EL COMENTARIO RECUPERADO SINGLELINE //
            #inicio_subcadena = final+1
            #encontro_lexema = True
            if caracter == "o": estado = 10
            else: break
        elif estado == 10:
            if caracter == "t": estado = 11
            else: break
        elif estado == 11:
            if caracter == "a": estado = 12
            else: break
        elif estado == 12:
            if caracter == "n": estado = 13
            else: break
        elif estado == 13:
            if caracter == "t": estado = 14
            else: break
        elif estado == 14:
            if caracter == "e": estado = 15
            else: break
        elif estado == 15:
            print("flotante")
        elif estado == 16:
            if caracter == "s": estado = 17
            else: break
        elif estado == 17:
            if caracter == "i": estado = 18
            else: break
        elif estado == 18:
            if caracter == "o": estado = 19
            else: break
        elif estado == 19:
            if caracter == "n": estado = 20
            else: break
        elif estado == 20:
            if caracter == "o": estado = 21
            else: break
        elif estado == 21:
            print("siono")
        elif estado == 24:
            if caracter == "l": estado = 25
            else: break
        elif estado == 25:
            if caracter == "o": estado = 26
            else: break
        elif estado == 26:
            print("(SIONO)")
        elif estado == 16:
            if caracter == "e": estado = 18
            else: break
        elif estado == 16:
            if caracter == "e": estado = 18
            else: break
        elif estado == 16:
            if caracter == "e": estado = 18
            else: break
        
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
    
    