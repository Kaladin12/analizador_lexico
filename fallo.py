def fallo(inicio = 0):
    diagram_switch = {
        209: 0,
        0: 7,
        7:16,
        16:22,
        22:27,
        27:42,
        42:52,
        52:34,
        34:39,
        39:72,
        72:144,
        144:153,
        153:161
    }

    if inicio in diagram_switch:
        return diagram_switch[inicio]
    else: 
        print(inicio)
        print('Error de compilador')
        return None