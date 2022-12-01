class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
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
#csvfile=CSVFile('./shampoo_sales.csv')
#print(csvfile.get_data())