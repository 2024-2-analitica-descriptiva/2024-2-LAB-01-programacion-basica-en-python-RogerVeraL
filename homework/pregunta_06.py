"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    data = (lambda: __import__('homework.read_data', fromlist=['read_data']).read_data())()

    p6 = {}
    rows = [row[4].split(",") for row in data]
    for row in rows:
        for word in row:
            key, value = word.split(":")
            if key in p6:
                p6[key].append(int(value))
            else:
                p6[key] = [int(value)]
    return sorted([(k, min(v), max(v)) for k, v in p6.items()])

print(pregunta_06())
