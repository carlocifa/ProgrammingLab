class ExamException(Exception):
        pass

class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
        self.can_read=True
        try:
            myfile=open(self.name, 'r')
            myfile.readline()
        except:
            self.can_read=False
            
    def get_data(self):
        if not self.can_read:
            raise ExamException('Errore file non aperto o illeggibile')
        else:
            values=[]
            l_epoch=[] #lista di tutte le epoch
            my_file=open(self.name, 'r')
            for line in my_file:
                elements=line.split(',')
                if elements[0]!='epoch':
                    s=True
                    try:
                        epoch=int(elements[0])
                        temp=float(elements[1].replace('\n',''))
                    except:
                        s=False
                    if s==True:
                        values.append([epoch,temp]) 
                        l_epoch.append(epoch)
            for i in range(1, len(l_epoch)):
                if l_epoch[i-1] >= l_epoch[i]:
                    raise ExamException('Errore epoch non ordinate o duplicate') 
                
                
            my_file.close()
            return values

def compute_daily_max_difference(self):
    lista_epoch=[] #lista di tutte le epoch
    lista_temp=[] #lista di tutte le temperature
    lista_diff=[] # lista finale di tutte le differenze
    for lista in self:
        epoch=lista[0]
        lista_epoch.append(epoch)
        temp=lista[1]
        lista_temp.append(temp)
    x=0 #numero di giorni diversi in data
    lista_giorni_epoch=[] # lista delle posizioni i di data dove inizia un nuovo giorno 
    for i in range(0, len(lista_epoch)):
        if i==0:
            inizio_giorno=lista_epoch[i]-(lista_epoch[i]%86400)
        if lista_epoch[i]- inizio_giorno >=86400:
            x+=1
            lista_giorni_epoch.append(i)
            inizio_giorno=lista_epoch[i]-(lista_epoch[i]%86400)
    lista_giorni_epoch.append(len(lista_epoch)) #append ultimo elemento i di data
    s=0 #elementi di data
    for i in range(0, x+1):
        lista_giorni_temp=[] #lista di tutte le temperature in un solo giorno
        while s < lista_giorni_epoch[i]:
           lista_giorni_temp.append(lista_temp[s])
           s+=1
        if len(lista_giorni_temp)==1:
            differenza = None
        else:
            differenza=max(lista_giorni_temp)-min(lista_giorni_temp)
            differenza=round(differenza, 3)
        lista_diff.append((differenza))
    return lista_diff     
            

       


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
#print('lista epoch e temperatura:\n{}'.format(time_series))
compute_daily_max_difference(time_series)
#print('lista differenze massime:\n{}'.format(compute_daily_max_difference(time_series)))
