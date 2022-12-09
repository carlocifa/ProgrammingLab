class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    #def __init__(self, prediction ):
        #self.prediction = prediction
    def predict(self, data):
        #Sdata = "".join(data)
        
        #dataf=float(data)
        prev_value = None
        increment = 0
        mid_increment = 0
        for item in data:
            for i,element in enumerate(data):
                if prev_value is not None:
                    increment = increment + item - prev_value
                prev_value = item
                if i != 0:
                    mid_increment = increment/i
        prediction =prev_value + mid_increment
        return prediction

#dat=["50","52","60"]
#num=IncrementModel()
#print(num.prediction)
#print(num.predict(dat))