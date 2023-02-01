class ExamException(Exception):
        pass

class CSVTimeSeriesFile():
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

def compute_daily_max_difference(self):
    lista_epoch=[]
    lista_temp=[]
    lista_diff=[]
    for lista in self:
        epoch=lista[0]
        lista_epoch.append(epoch)
        temp=lista[1]
        lista_temp.append(temp)
    x=0
    lista_giorni_epoch=[]
    for i in range(0, len(lista_epoch)):
        if i==0:
            inizio_giorno=lista_epoch[i]-(lista_epoch[i]%86400)
        if lista_epoch[i]- inizio_giorno >=86400:
            x=x+1
            lista_giorni_epoch.append(i)
            inizio_giorno=lista_epoch[i]-(lista_epoch[i]%86400)
    lista_giorni_epoch.append(len(lista_epoch))
    s=0
    for i in range(0, x+1):
        lista_giorni_temp=[]
        while s < lista_giorni_epoch[i]:
           lista_giorni_temp.append(lista_temp[s])
           s+=1
        differenza=max(lista_giorni_temp)-min(lista_giorni_temp)
        differenza=round(differenza, 3)
        lista_diff.append((differenza))
    return lista_diff     
            

       


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print('lista epoch e temperatura:\n{}'.format(time_series))
compute_daily_max_difference(time_series)
print('lista differenze massime:\n{}'.format(compute_daily_max_difference(time_series)))
