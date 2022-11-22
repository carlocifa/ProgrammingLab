def sum_csv(file_name):
    values=[]
    prezzo=0
    for item in file_name:
        prezzo= prezzo + item
    return prezzo
    my_file=open('shampoo_sales.csv', 'r')
    for line in my_file:
        elements=line.split(',')
        if elements[0]!='Date':
            date=elements[0]
            value=elements[1]
    values.append(float(value))
    my_file.close()
sum_csv('file_name')

