def sum_csv(file_name):
    values=[]
    file_name=open('shampoo_sales.csv', 'r')
    for line in file_name:
        elements=line.split(',')
        if elements[0]!='Date':
            date=elements[0]
            value=elements[1]
            values.append(value)
            file_name.close()
    prezzo=0
    for item in values:
        prezzo=prezzo + item
    return prezzo
sum_csv('file_name')