from def_de_dato.entero import entero
from def_de_dato.flotante import flotante
from def_de_dato.siono import siono
from def_de_dato.nulo import nulo
from def_de_dato.cadena import cadena
from misc.identificador import identificador

# inicio: (diagrama, aceptacion)
diagramas = {
    0: (entero, 6),
    7: (flotante, 15),
    16: (siono, 21),
    22: (nulo, 26),
    27: (cadena, 33),
    209: (identificador, 211)
}