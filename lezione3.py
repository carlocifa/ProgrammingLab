def sum_csv(my_file):
    somma=0
    for item in my_file:
        somma=somma+item
    return somma
    
values=[]
my_lista=open('shampoo_sales.csv','rw')
for line in my_lista:
    elements= line.split(",")
    if elements[0]!="Date":
        value=float(elements[1])
        values.append(value)

risultato=sum_csv(values)
print("risultato è:{}".format(risultato))
    