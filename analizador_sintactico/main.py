entrada = "id*id+id$"

# epsilon es  '', error es '-' E -> TQ -> FZ
Ee = [ 'ID', 'OP_ASIG', 'CADENA', 'ENTERO', 'FLOTANTE', 'SIONO', 'VAL_CAD', 'VAL_SIONO', 'VAL_ENT', 'VAL_FLOT', 'ARI_PLUS', 'ARI_SUBS', 'ARI_MULT', 'ARI_DIV', 'ARI_POW', 'AGR_OP', 'AGR_CP' ]  
GLC = {
    'S': {'$':[['']], 'ID': [['ASIGN']], 'OP_ASIG':[['-']], 'EOL':[['']], 'CADENA': [['ASIGN']], 'ENTERO': [['ASIGN']], 'FLOTANTE':[['ASIGN']], 'SIONO':[['ASIGN']], 'VAL_CAD':[['-']], 'VAL_SIONO':[['-']], 'VAL_FLOT':[['-']]},
    'ASIGN': {''},
    'TIPO': {},
    'VALOR': {},
    'ARI_PS': {},
    'ARI_MD': {},
    'EXPR': {'$':[['']], 'ID':[['VALOR'],['V']], 'OP_ASIG':[['-']], 'EOL':[[]],'CADENA':[[]],'ENTERO':[[]],'FLOTANTE':[[]], 'SIONO':[[]], 'VAL_CAD':[['-']], 'VAL_SIONO':[[]]},
    'V': {'ID':[['-']], "OP_ASIG":[['-']], "EOL":[['']], "CADENA":[['-']], "ENTERO":[['-']], "FLOTANTE":[['-']]},
    'X': {'ID':[['-']], "OP_ASIG":[['-']], "EOL":[['']], "CADENA":[['-']], "ENTERO":[['-']], "FLOTANTE":[['-']]},   
    'T': {'ID':[['VALOR'], ['U']], "OP_ASIG":[['-']], "EOL":[['-']], "CADENA":[['-']], "ENTERO":[['-']]},
    'U': {'ID':[['-']], "OP_ASIG":[['-']], "EOL":[['']], "CADENA":[['-']], "ENTERO":[['-']]},
}


def pila(entrada):
    # Definicion de parametros
    pila = [['$'], ['E']]
    #simbolo_inicio = "$E"
    while (len(pila)>0):
        print(pila, entrada,pila[-1],pila[-1][0] in GLC)
        if(pila[-1][0] in GLC): # no terminal
            
            posibles_prods = GLC[pila[-1][0]]
            pila = pila[:-1]
            if entrada[:2] == 'id':
                for i in posibles_prods['id'][::-1]:
                    pila.append(i)
            else:
                for i in posibles_prods[entrada[:1]][::-1]:
                    pila.append(i)
        else: # terminal
            print('TERMINAL', pila[-1], entrada)
            if entrada[:2] == 'id' and pila[-1][0] == 'id':
                entrada = entrada[2:]
                pila.pop()
            elif entrada[:1] == pila[-1][0]:
                entrada = entrada[1:]
                pila.pop()
            elif pila[-1] == ['']:
                pila.pop()
            else:
                print('ERROR')
                break

pila(entrada)