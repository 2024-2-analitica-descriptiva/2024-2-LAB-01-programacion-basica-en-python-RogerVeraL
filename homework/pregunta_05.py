"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = (lambda: __import__('homework.read_data', fromlist=['read_data']).read_data())()

    p5 = {}
    for row in data:
        key,value = row[0],int(row[1])
        if key in p5:
            p5[key].append(value)
        else:
            p5[key] = [value]
    return sorted([(k, max(v), min(v)) for k, v in p5.items()])
print(pregunta_05())
