from def_de_dato.entero import entero
from def_de_dato.flotante import flotante
from def_de_dato.siono import siono
from def_de_dato.nulo import nulo
from def_de_dato.cadena import cadena
from misc.identificador import identificador
from tipo_de_dato.val_entero import val_entero
from tipo_de_dato.val_flotante import val_flotante
from tipo_de_dato.val_siono import val_falso, val_verdadero
from operadores.oprel import oprel_
from func_auxiliar.regresar import regresar 
from func_auxiliar.tomacar import tomacar
from func_auxiliar.dormir import dormir


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
    72: (oprel_, (74,75,77,78,80,81,83)),
    144: (regresar, 152),
    153: (tomacar, 160),
    161: (dormir, 167),
    209: (identificador, 211)
}