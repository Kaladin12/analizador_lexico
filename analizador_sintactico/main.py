from GLC import GLC
from terminales import terminales
#entrada = "COND_IF AGR_OP VAL_ENT OP_MAY VAL_ENT AGR_CP AGR_OB ENTERO ID OP_ASIG VAL_ENT EOL AGR_CB $"
#entrada = "HAZ_MNTRS AGR_OB ENTERO ID OP_ASIG VAL_ENT ARI_PLUS VAL_ENT EOL AGR_CB AGR_OP AGR_OP VAL_ENT OP_MAY VAL_ENT AGR_CP AND AGR_OP VAL_SIONO AGR_CP AGR_CP EOL $"
#entrada = ' ENTERO OP_ASIG ENTERO $'
entrada = 'ENTERO ID OP_ASIG VAL_ENT EOL COND_IF AGR_OP VAL_ENT OP_MAY VAL_ENT AGR_CP AGR_OB ENTERO ID OP_ASIG VAL_ENT EOL AGR_CB $'
def pila(entrada):
    # Split de entrada
    entrada = entrada.split()
    # Definicion de parametros
    pila = [['$'], ['MAIN']]
    #simbolo_inicio = "$E"
    while (len(pila)>0):
        print(pila, entrada,pila[-1],pila[-1][0] in GLC)
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
            if (entrada[0] in terminales and pila[-1][0] == entrada[0]) or entrada[0] == pila[-1][0]:
                entrada = entrada[1:]
                pila.pop()
            elif pila[-1] == ['']:
                pila.pop()
            else:
                print('ERROR')
                return False
    return True

if (pila(entrada)):
    print('ACEPTADA')
else:
    print('RECHAZADA')
