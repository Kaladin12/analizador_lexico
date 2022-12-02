import os

PRODUCTIONS = {}
TERMINALES = set()

def generate_json_for_productions():
    import json, re
    
    TEMP = None
    with open(os.path.join(os.getcwd(),  'GLC_FINAL.txt')) as f:
        TEMP = f.readlines()
        f.close()
    for production in TEMP:
        #print(production)
        splitted = [V.strip().replace('\n','').split() for V in production.split('::=')]
        #print(splitted)
        if splitted[0][0] not in PRODUCTIONS:
            PRODUCTIONS[splitted[0][0]] = []
        PRODUCTIONS[splitted[0][0]].append(splitted[1])
    for i in PRODUCTIONS:
        for prod in PRODUCTIONS[i]:
            for ind in prod:
                #print(prod, ind)
                if ind not in PRODUCTIONS :
                    TERMINALES.add(ind)
    json_obj = json.dumps(PRODUCTIONS)
    with open('temp_.json', 'w') as f:
        f.write(json_obj)
    """for i in PRODUCTIONS:
        print(i, PRODUCTIONS[i])"""
def PRIMERO(A):
    print('A: ', A, isinstance(A, list))
    if not isinstance(A, list) and A in TERMINALES:
        return {A}
    elif not isinstance(A, list) and A in PRODUCTIONS:
        PRODS = PRODUCTIONS[A]
        to_return = set()
        for prod in PRODS:
            #print('PROD ', prod)
            temp = PRIMERO(prod)
            to_return = temp | to_return
        return to_return
    elif len(A)==0 or A == ['EPSILON']:
        return {'EPSILON'}
    else:
        to_return = PRIMERO(A[0])
        
        print(to_return, A[0], A)
        temp = set()
        if 'EPSILON' in to_return:
            i = 1
            while 'EPSILON' in to_return:
                temp = to_return | (to_return - {'EPSILON'})
                print(A[i:], len(A[i:])==0)
                if  len(A[i:])==0 :
                    temp = temp | {'EPSILON'}
                    break
                if A[i:] in TERMINALES:
                    temp = temp | {A[i:]}
                    break
            to_return = PRIMERO(A[i:])
            temp = temp | to_return - {'EPSILON'}
            i += 1
        else:
            temp = temp | to_return
    return temp

def SIGUIENTE(A):
    to_return = set()
    if A == 'MAIN':
        to_return = to_return | {'$'}
    for VAR, PRODS_ALT in PRODUCTIONS.items():
        for PROD in PRODS_ALT:
            for PROD_VAR in PROD:
                if PROD_VAR == A:
                    NEXT = PROD[PROD.index(PROD_VAR)+1:]
                    if len(NEXT)==0:
                        if VAR == A:
                            continue
                        else: 
                            to_return = to_return | SIGUIENTE(VAR)
                    else:
                        TEMP = PRIMERO(NEXT)
                        print('NEXT: ',NEXT, PROD_VAR, TEMP)
                        if 'EPSILON' in TEMP:
                            to_return = to_return | TEMP - {'EPSILON'}
                            to_return = to_return | SIGUIENTE(VAR)
                        else:
                            to_return = to_return | TEMP
    return to_return 
def build_table():
    TABLE = {}
    TERMINALES_ = TERMINALES | {'$'}
    for i in PRODUCTIONS:
        TABLE[i] = {}
        for term in TERMINALES_ - {'EPSILON'}:
            TABLE[i][term] = [['-']]
    for VAR, PRODS_ALT in PRODUCTIONS.items():
        print(VAR)
        for prod in PRODS_ALT:
            # para las terminales en Primero(A), se agrega la produccion en [VAR, terminal]
            terminales_primero = PRIMERO(prod)
            if 'EPSILON' not in terminales_primero:
                for term in terminales_primero - {'EPSILON'}:
                    TABLE[VAR][term] = [prod]
            else:
                terminales_siguiente = SIGUIENTE(VAR)
                print(VAR, prod, terminales_siguiente)
                for term in terminales_siguiente:
                    TABLE[VAR][term] = [prod]
                    
                
    #print(TABLE['MAIN'])        
    import json
    json_obj = json.dumps(TABLE)
    with open('temp_.json', 'w') as f:
        f.write(json_obj)

generate_json_for_productions()
#print(PRIMERO('NEW_OPER'))
#print(SIGUIENTE('ESTRUCT'))
build_table()

