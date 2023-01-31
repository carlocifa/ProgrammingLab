class ExamException(Exception):
        pass

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
            if elements[0]!='epoch':
                date=int(elements[0])
                value=float(elements[1].replace('\n',''))
                values.append([date,value])
        my_file.close()
        return values
    def compute_daily_max_difference(self, time_series):
        lista_epoch=[]
        lista_temp=[]
        lista_diff=[]
        for lista in time_series:
            epoch=lista[0]
            lista_epoch.append(epoch)
            temp=lista[1]
            lista_temp.append(temp)
        for i in range(0, len(lista_epoch)-1):
            if i==0:
                inizio_giorno=lista_epoch[i]
            if lista_epoch[i]%86400==0:
                inizio_giorno=lista_epoch[i]
            lista_giorni=[] 
            while lista_epoch[i] - inizio_giorno < 86400 and i < len(lista_epoch):
                lista_giorni.append(lista_temp[i])
                i=i+1
            minimo=min(lista_giorni)
            massimo=max(lista_giorni)
            differenza=massimo-minimo
            lista_diff.append(differenza)
                
                

            
class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        string_data = super().get_data()
        return string_data
       


time_series_file = CSVFile(name='data.csv')
time_series = time_series_file.get_data()
#print('{}'.format(time_series))
time_series_file.compute_daily_max_difference(time_series)


