entrada = "id*id+id$"

# epsilon es  '', error es '-' E -> TQ -> FZ
GLC = {
    'E': {'id': [['T'],['Q']], '+':[['-']], '*':[['-']], '(':[['T'],['Q']],')':[['-']], '$':[['-']]},
    'Q': {'id': [['-']], '+': [['+'],['T'],['Q']], '*':[['-']],'(':[['-']],')':[['']], '$':[['']]}, #['', '+TQ']
    'T': {'id': [['F'],['Z']], '+': [['-']], '*':[['-']], '(':[['F'],['Z']], ')':[['-']], '$':[['-']]},#['FZ'],
    'Z': {'id': [['-']], '+':[['']], '*': [['*'],['F'],['Z']], '(': [['-']], ')':[['']], '$':[['']] },#['', '*FZ'],
    'F': {'id': [['id']], '+':[['-']], '*':[['-']], '(': [['('],['E'],[')']], ')':[['-']],'$':[['-']]}#['(E)', 'id']
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