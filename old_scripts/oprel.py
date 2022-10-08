recupera = False
def fallo(inicio = 0):
    global estado
    global recupera
    if inicio == 0: return 9
    elif inicio == 9: return 12
    elif inicio == 12: return 20
    elif inicio == 20: return 25
    elif inicio == 25 and not recupera: 
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
cadena = '5.5E+6 <> 5 >veinte =45.2E-1 25 e0 <2.0'
estado = 0
inicio = 0
def cosa(cadena, estado):
    global encontro_lexema
    global inicio
    caracter = ''
    cadena_original = cadena
    while True:
        if len(cadena) != 0 :
            caracter = cadena[0]
            cadena  = cadena [1:]
        #print('dentro: ',caracter, cadena, estado)
        if estado == 0: # case 0 
            if caracter == " ": estado = 0
            elif caracter == "<": estado = 1
            elif caracter == "=": estado = 5
            elif caracter == ">": estado = 6
            else: 
                break
        if estado == 1:
            if len(cadena) != 0 :
                caracter = cadena[0]
            if caracter == "=": estado = 2
            elif caracter == ">": estado = 3
            else: estado = 4
        if estado == 6:
            if len(cadena) != 0 :
                caracter = cadena[0]
            if caracter == "=": estado = 7
            else: estado = 8
        if estado == 2:
            cadena  = cadena [1:]
            print("devuelve(oprel, MEI)")
            encontro_lexema = True
            break
        if estado == 3:
            cadena  = cadena [1:]
            print("devuelve(oprel, DIV)")
            encontro_lexema = True
            break
        if estado == 4:
            print("devuelve(oprel, MEN)")
            encontro_lexema = True
            break
        if estado == 5:
            print("devuelve(oprel, IGU)")
            encontro_lexema = True
            break
        if estado == 7:
            cadena  = cadena [1:]
            print("devuelve(oprel, MAI)")
            encontro_lexema = True
            break
        if estado == 8:
            print("devuelve(oprel, MAY)")
            encontro_lexema = True
            break
        if estado == 9:
            if esLetra(caracter): estado  = 10
            else: break
        if estado == 10:
            if len(cadena) != 0 :
                caracter = cadena[0]
                if esLetra(caracter) or esNumero(caracter): estado = 10
                else: estado = 11
            else: estado = 11
        if estado == 11:
            print("devuelve(obten_complex, ID)")
            encontro_lexema = True
            break
        if estado == 12:
            if esNumero(caracter): estado = 13
            else: break
        elif estado == 13:
            if esNumero(caracter): estado = 13
            elif caracter == 'E': estado = 16
            elif caracter == '.': estado = 14
            else: break
        elif estado == 14:
            if esNumero(caracter): estado = 15
            else: break
        elif estado == 15:
            if esNumero(caracter): 
                if len(cadena) == 0 :break
                else: estado = 15
            elif caracter == 'E': estado = 16
            else: break
        elif estado == 16:
            if caracter in ['+', '-']: estado = 17
            elif esNumero(caracter): estado = 18
            else: break
        elif estado == 17:
            if esNumero(caracter): estado = 18
            else: break
        if estado == 18:
            if len(cadena) != 0 :
                caracter = cadena[0]
                if esNumero(caracter): estado = 18
                else: estado = 19
            else: estado = 19
        if estado == 19:
            if len(cadena)>0 and esLetra(cadena[0]):
                inicio = fallo(-1)
                break
            print("devuelve(oprel, exponcencial)")
            encontro_lexema = True
            break
        if estado == 20:
            if esNumero(caracter): estado = 21
            else: break
        elif estado == 21:
            if esNumero(caracter): estado = 21
            elif caracter == '.': estado = 22
            else: break
        elif estado == 22:
            if esNumero(caracter): estado = 23
            else: break
        if estado == 23:
            if len(cadena) != 0 :
                caracter = cadena[0]
                if esNumero(caracter): estado = 23
                else: estado = 24
            else: estado = 24
        if estado == 24:
            if len(cadena)>0 and esLetra(cadena[0]):
                inicio = fallo(-1)
                break
            print("devuelve(oprel, flotante)")
            encontro_lexema = True
            break
        if estado == 25:
            if esNumero(caracter): estado = 26
            else: break
        if estado == 26:
            if len(cadena) != 0 :
                caracter = cadena[0]
                if esNumero(caracter): estado = 26
                else: estado = 27
            else: estado = 27
        if estado == 27:
            if len(cadena)>0 and esLetra(cadena[0]):
                inicio = fallo(-1)
                break
            print("devuelve(oprel, entero)")
            encontro_lexema = True
            break

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
        recupera = False
    encontro_lexema = False
    
    