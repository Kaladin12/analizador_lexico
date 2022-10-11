def fallo(inicio = 0):
    diagram_switch = {
        209: 0,
        0: 7,
        7:87,
        87:16,
        16:22,
        22:27,
        27:42,
        42:52,
        52:93,
        93:105,
        105:120,
        120:125,
        125:130,
        130:144,
        144:34,
        34:39,
        39:72,
        72:61,
        61:58,
        58:66, 
        66:84  
    }

    if inicio in diagram_switch:
        return diagram_switch[inicio]
    else: 
        print(inicio)
        print('Error de compilador')
        return None