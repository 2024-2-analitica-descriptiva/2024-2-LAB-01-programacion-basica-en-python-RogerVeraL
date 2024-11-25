def read_data():
    with open("files/input/data.csv", 'r') as file:
        data = file.readlines()
        data = [row.replace('\n', '') for row in data]
        data = [row.split('\t') for row in data]
    return data
