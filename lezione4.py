class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
        elements=[]
        my_file=open(self.name, 'r')
        for line in my_file:
            if line!='Date,Sales\n':
                elements.append(line)
        my_file.close()
        return elements
            
                
csv_file = CSVFile("shampoo_sales.csv")            # in questo modo istanzi l'oggetto csv_file, passandogli come argomento il nome del file
data = csv_file.get_data()                                    # chiami il metodo get_data dell'oggetto e salvi l'output nella variabile data
print(data)