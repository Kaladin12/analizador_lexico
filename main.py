from config import diagramas

recupera = False

def fallo(inicio = 0):
    global estado
    global recupera
    if inicio == 0: return 7
    elif inicio == 7: return 16
    elif inicio == 16: return 22
    elif inicio == 22: return 27
    elif inicio == 27: return 209
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
cadena = 'entero flotante cadena siono nulo hugyefjne2?'
super_cadena_original = cadena
estado = 0
inicio = 0
final = 0
inicio_subcadena = 0

def buscar_lexema_en_diagrama(estado, caracter):
    global inicio_subcadena, encontro_lexema , final
    #print("estado:", estado, final)
    estado, regresa = diagramas[inicio][0](estado, caracter) # Revisar si en base al caracter se mueve a otro estado o fallo (-1)    
    final = final+1 if not regresa else final-1 #
    # id321=
    if estado == diagramas[inicio][1]: # Si el estado esta en el estado de aceptacion correspondiente al diagrama
        encontro_lexema = True 
        #print(super_cadena_original, inicio_subcadena, final)
        #print(super_cadena_original[inicio_subcadena:final])
        inicio_subcadena = final+1 # Funcion de "aceptar", mover el apuntador de inicio uno a la derecha del de busqueda 
        
    return estado, regresa # Este valor unicamente puede ser un estado dentro del diagrama [no de aceptacion] o -1

def cosa(cadena, estado):
    global encontro_lexema
    global inicio, final, inicio_subcadena, super_cadena_original
    caracter = ''
    cadena_original = cadena
    while True:
        if len(cadena) != 0 :
            caracter = cadena[0]
            cadena  = cadena [1:]   
        #print('dentro: ',caracter,'|', cadena, estado)
        #estado = diagramas[inicio](estado, caracter)
        
        estado, _ = (buscar_lexema_en_diagrama(estado, caracter)) # Esta funcion se mueve a traves de un diagrama (Ej: entero - aceptacion: 6)
    
        #print('despues: ', estado, encontro_lexema)
        if estado in (-1, diagramas[inicio][1]) or len(cadena)==0: break
        

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
        inicio = 0
        final = inicio_subcadena
        recupera = False
    #print('fuera',inicio_subcadena, final)
    encontro_lexema = False
    
    