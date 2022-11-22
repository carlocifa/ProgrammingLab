class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self, name):
        values=[]
        lista=open(lista_liste.name, 'r')
        for line in lista:
            elements=line.split(',')
            if elements[0] != 'Date':
                value=elements[1]
                values.append(float(value))
                file.close()
        if(len(values)==0):
            return None
        else:
            print(values)
                
lista_liste=CSVFile('shampoo_sales.csv')
print(name.name)
print(name)
name.get_data(name)

        