from config import diagramas
from check_if_id_is_reserved import check_if_id_is_reserved_
from fallo import fallo

recupera = False
encontro_lexema = False

def buscar_lexema_en_diagrama(estado, caracter):
    global inicio_subcadena, encontro_lexema , final
    #print("estado:", estado, final)
    estado, regresa, tok = diagramas[inicio][0](estado, caracter) # Revisar si en base al caracter se mueve a otro estado o fallo (-1)    
    if not regresa: final += 1
    else: final = final -1 if caracter != " " else final # no tiene sentido quitar siempre un caracter
    #print(final)
    aceptacion = diagramas[inicio][1]
    if ((isinstance(aceptacion, tuple) and estado in aceptacion) 
            or 
            estado == diagramas[inicio][1]): # Si el estado esta en el estado de aceptacion correspondiente al diagrama
        #s = super_cadena_original[inicio_subcadena:final]
        s = super_cadena_original[inicio_subcadena:final]
    
        if inicio == 209:
            temp_tok = check_if_id_is_reserved_(s)
            if temp_tok!=None:  tok = temp_tok
        encontro_lexema = True 
        #if regresa:
        #    print(tok, super_cadena_original[inicio_subcadena:final+1], inicio_subcadena, final+1)
        #else:
        #    print(tok, super_cadena_original[inicio_subcadena:final], inicio_subcadena, final)
        print(tok,s)
        inicio_subcadena = final+1 if regresa else final # Funcion de "aceptar", mover el apuntador de inicio uno a la derecha del de busqueda 
        
    return estado, regresa # Este valor unicamente puede ser un estado dentro del diagrama [no de aceptacion] o -1

def cosa(cadena, estado):
    global encontro_lexema
    global inicio, final, inicio_subcadena, super_cadena_original
    caracter = ''
    cadena_original = cadena+' '
    while True:
        if len(cadena) != 0 :
            caracter = cadena[0]
            cadena  = cadena [1:]   
        #print('dentro: ',caracter,'|', cadena, estado)

        estado, reg = (buscar_lexema_en_diagrama(estado, caracter)) # Esta funcion se mueve a traves de un diagrama (Ej: entero - aceptacion: 6)
    
        #print('despues: ', estado, encontro_lexema)
        aceptacion = diagramas[inicio][1]
        
        if ((isinstance(aceptacion, tuple) and estado in aceptacion) or
            estado in (-1, diagramas[inicio][1]) or len(cadena)==0): 
            #if caracter == " "  and not encontro_lexema: 
            #    inicio_subcadena -=1
            break
        
    if not encontro_lexema:
        while len(cadena_original)>0:
            if not cadena_original[0]==" ":
                break
            encontro_lexema = True #bandera para comenzar en primer diagrama
            cadena_original = cadena_original[1:]
            inicio_subcadena +=1
        return cadena_original
    while len(cadena)>0:
        if not cadena[0]==" ":
            break
        cadena = cadena[1:]
        inicio_subcadena +=1
    if reg:
        if len(cadena)==0: 
            inicio_subcadena -= 1
            return caracter
        elif caracter!=' ':  
            return caracter + cadena
    return cadena

cadenas = []
with open(r"C:\Users\Yo\prueba.txt", encoding='utf-8') as f:
    cadenas = f.read().splitlines()
for cadena in cadenas:
    #cadena = 'en caso  en imprimir longitud longitudes &50.2569 < predeterminado interruptor siw si sin sino sinowe -5  "tt4b"interruptor  &| "" cada cadaw cadena cadena542 (1245 e == 4565.2 _ } mientras-haz mientras regresar2 tomacar dormire < 5 importar rango romper romper2 < rango2'#  != verdadero    nulo    <= ==    cas    flotante e  < cadena5  falso siono nulo hugyefjne2?'
    # '  cadena cadena542   != verdadero    nulo    <= ==    cas    flotante e  < cadena5  falso siono nulo hugyefjne2' 
    super_cadena_original = cadena
    estado = 209
    inicio = 209
    final = 0
    inicio_subcadena = 0
    cadena = cadena + ' '
    while len(cadena)!=0:
        cadena = cosa(cadena, estado)
        #print(encontro_lexema)
        if inicio == None:
            break
        if not encontro_lexema:
            inicio = fallo(inicio)
            if inicio == None:
                break
            estado = inicio
            final = inicio_subcadena
        #print('cadena: [', cadena, estado, encontro_lexema, recupera)
        else:
            inicio = 209
            estado =  inicio
            final = inicio_subcadena
            recupera = False
        #print('fuera',inicio_subcadena, final)
        encontro_lexema = False
        
        