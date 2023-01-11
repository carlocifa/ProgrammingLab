class MovingAverage():
    def __init__(self, f):
        if f<=0:
            raise ExamException('Errore, finestra vuota')
        self.f=f
    def compute(self, lista):
        if lista==[]:
            raise ExamException('Errore lista vuota')
        elif len(lista)<self.f:
            raise ExamException('Errore, lunghezza della lista è minore della finestra')
        for i in range(0, len(lista)-1):
            if isinstance(lista[i],(int, float))==False:
                raise ExamException('Errore, lista non con numeri')
        lista1=[]
        for i in range(0,len(lista)+1-self.f):
            num=0
            sum=0
            media=0
            while num<self.f:
                sum=sum+lista[i]
                i=i+1
                num=num+1
                media=sum/self.f
            lista1.append(media)

        return lista1
            
            
            
            
            
      






moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)