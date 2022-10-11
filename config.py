from def_de_dato.entero import entero
from def_de_dato.flotante import flotante
from def_de_dato.siono import siono
from def_de_dato.nulo import nulo
from def_de_dato.cadena import cadena
from misc.identificador import identificador
from tipo_de_dato.val_entero import val_entero
from tipo_de_dato.val_flotante import val_flotante
from tipo_de_dato.val_siono import val_falso, val_verdadero
from tipo_de_dato.val_cadena import val_cadena
from operadores.oprel import oprel_
from operadores.agrupacion import agrupacion
from operadores.artimeticos import aritmeticos
from operadores.logicos import logicos
from misc.condicional import condicional
from misc.interruptor import interruptor
from misc.predeterminado import predeterminado
from misc.caso import caso
from misc.cada import cada
from misc.mientras import mientras
from misc.regresar import regresar
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
    61: (agrupacion, (62, 63,64,65)),
    72: (oprel_, (74,75,77,78,80,81,83)),
    58: (val_cadena, 60),
    66: (aritmeticos, (67,68,69,70,71)),
    84: (logicos,(85,86)),
    87: (condicional, (90,92)),
    93: (interruptor, 104),
    105: (predeterminado, 119),
    120: (caso, 124),
    125: (cada, 129),
    130: (mientras, (139,143)),
    144: (regresar, 152),
    209: (identificador, 211)
}