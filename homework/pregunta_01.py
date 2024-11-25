"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    from homework.read_data import read_data
    data = read_data() # data = (lambda: __import__('read_data').read_data())()
    return sum([int(row[1]) for row in data]) 
print(pregunta_01())
