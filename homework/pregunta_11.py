"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    

    """
    data = (lambda: __import__('homework.read_data', fromlist=['read_data']).read_data())()
    p11 = {}
    for row in data:
        for letra in row[3].split(","):
            p11[letra] = p11.get(letra, 0) + int(row[1])
    return dict(sorted(p11.items()))
print(pregunta_11())