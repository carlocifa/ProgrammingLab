class CSVFile():
    def __init__(self,name):
        self.name=name
        self.can_read=True
        try:
            myfile=open(self.name, 'r')
            myfile.readline()
        except Exception as e:
            self.can_read=False
            print('Errore in apertura: "{}"'.format(e))
    def get_data(self):
        if not self.can_read:
            print('Errore file non aperto o illeggibile')
            return None
        else:
            values=[]
        my_file=open(self.name, 'r')
        for line in my_file:
            elements=line.split(',')
            if elements[0]!='Date':
                date=elements[0]
                value=elements[1].replace('\n','')
                values.append([date,value])
        my_file.close()
        return values
mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))
