from config import diagramas
from check_if_id_is_reserved import check_if_id_is_reserved_
from fallo import fallo

recupera = False
encontro_lexema = False
cadena = 'enterof 5.2 3 verdadero nulo flotantee cadena5 falso siono nulo hugyefjne2?'
super_cadena_original = cadena
estado = 209
inicio = 209
final = 0
inicio_subcadena = 0



def buscar_lexema_en_diagrama(estado, caracter):
    global inicio_subcadena, encontro_lexema , final
    #print("estado:", estado, final)
    estado, regresa, tok = diagramas[inicio][0](estado, caracter) # Revisar si en base al caracter se mueve a otro estado o fallo (-1)    
    if not regresa: final += 1
    else: final = final -1 if caracter != " " else final # no tiene sentido quitar siempre un caracter
    #print(final)
    if estado == diagramas[inicio][1]: # Si el estado esta en el estado de aceptacion correspondiente al diagrama
        s = super_cadena_original[inicio_subcadena:final]
        if inicio == 209:
            temp_tok = check_if_id_is_reserved_(s)
            if temp_tok!=None:  tok = temp_tok
        encontro_lexema = True 
        if regresa:
            print(tok, super_cadena_original[inicio_subcadena:final+1])
        else:
            print(tok, super_cadena_original[inicio_subcadena:final])
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

        estado, _ = (buscar_lexema_en_diagrama(estado, caracter)) # Esta funcion se mueve a traves de un diagrama (Ej: entero - aceptacion: 6)
    
        #print('despues: ', estado, encontro_lexema)
        if estado in (-1, diagramas[inicio][1]) or len(cadena)==0: break
        

    if not encontro_lexema:
        if len(cadena_original)> 0 and cadena_original[0]==" ":
            encontro_lexema = True #bandera para comenzar en primer diagrama
            return cadena_original[1:]
        return cadena_original
    return cadena[1:] if len(cadena)>0 and cadena[0] == " " else cadena

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
    
    