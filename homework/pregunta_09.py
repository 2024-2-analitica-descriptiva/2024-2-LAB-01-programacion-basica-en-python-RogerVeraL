"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    data = (lambda: __import__('homework.read_data', fromlist=['read_data']).read_data())()

    p9 = {}
    rows = [row[4].split(",") for row in data]
    for row in rows:
        for word in row:
            key, value = word.split(":")
            p9[key] = p9.get(key, 0) + 1
    #p9 =  {k:v for k,v in sorted(p9.items())}
    return dict(sorted(p9.items()))
print(pregunta_09())
