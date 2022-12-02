import sys
sys.path.insert(0,'/analizador_sintactico')

from .GLC import GLC
from .terminales import terminales
# IF ( 2 > 5 ) { ENTERO COSA = 5 ; }
#entrada = "COND_IF AGR_OP VAL_ENT OP_MAY VAL_ENT AGR_CP AGR_OB ENTERO ID OP_ASIG VAL_ENT EOL AGR_CB $"
#entrada = "HAZ_MNTRS AGR_OB ENTERO ID OP_ASIG VAL_ENT ARI_PLUS VAL_ENT EOL AGR_CB AGR_OP AGR_OP VAL_ENT OP_MAY VAL_ENT AGR_CP AND AGR_OP VAL_SIONO AGR_CP AGR_CP EOL $"
# ENTERO = ENTERO
#entrada = ' ENTERO OP_ASIG ENTERO $'
#entrada = 'ENTERO ID OP_ASIG VAL_ENT EOL COND_IF AGR_OP VAL_ENT OP_MAY VAL_ENT AGR_CP AGR_OB ENTERO ID OP_ASIG VAL_ENT EOL AGR_CB $'

def pila(entrada):
    # Split de entrada
    entrada = entrada.split()
    # Definicion de parametros
    pila = [['$'], ['MAIN']]
    #simbolo_inicio = "$E"
    while (len(pila)>0):
        print('PILA',pila,'entrada', entrada,'head',pila[-1],'es variable? ',pila[-1][0] in GLC, '\n')
        if(pila[-1][0] in GLC): # no terminal
            
            posibles_prods = GLC[pila[-1][0]]
            pila = pila[:-1]
            if entrada[0] in terminales:
                for i in posibles_prods[entrada[0]][::-1]:
                    pila.append(i)
            else:
                for i in posibles_prods[entrada[0]][::-1]:
                    pila.append(i)
        else: # terminal
            print('TERMINAL', pila[-1], entrada)
            print("\n")
            if (entrada[0] in terminales and pila[-1][0] == entrada[0]) or entrada[0] == pila[-1][0]:
                entrada = entrada[1:]
                pila.pop()
            elif pila[-1] == ['']:
                pila.pop()
            else:
                print('ERROR')
                return False
    return True

def llamada(entrada):
    if (pila(entrada)):
        print('ACEPTADA')
    else:
        print('RECHAZADA')
