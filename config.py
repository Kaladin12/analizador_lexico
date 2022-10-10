from def_de_dato.entero import entero
from def_de_dato.flotante import flotante
from def_de_dato.siono import siono
from def_de_dato.nulo import nulo
from def_de_dato.cadena import cadena
from misc.identificador import identificador
from tipo_de_dato.val_entero import val_entero
from tipo_de_dato.val_flotante import val_flotante
from tipo_de_dato.val_siono import val_falso, val_verdadero

# inicio: (diagrama, aceptacion)
diagramas = {
    0: (entero, 6),
    7: (flotante, 15),
    16: (siono, 21),
    22: (nulo, 26),
    27: (cadena, 33),
    34: (val_flotante, 38),
    39: (val_entero, 41),
    42: (val_verdadero, 51),
    52: (val_falso, 57),
    209: (identificador, 211)
}