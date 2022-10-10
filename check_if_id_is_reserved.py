from config import diagramas
from fallo import fallo

def check_if_id_is_reserved_(cadena):
    temp = 0
    init_ = 0
    tok = None
    s_ = cadena
    while (temp<=33 or temp >=42 and temp<=57) and len(s_)>0:
        caracter = s_[0]
        s_ = s_[1:]
        temp, _, tok = diagramas[init_][0](temp, caracter)
        if temp == -1:
            if init_ == 52: break
            init_ = fallo(init_)
            temp = init_
            s_ = cadena
        elif temp == diagramas[init_][1]: 
            if len(s_)>0: return None
            break
    return tok