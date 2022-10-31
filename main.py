def get_column(data):
    column_name = []
    for i in data:
        column_name.append(i.split(",")[-1])

    return column_name
data = open('data.csv').read() 
data=data.split("\n")
print(get_column(data))
