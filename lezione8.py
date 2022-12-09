class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')
class IncrementModel(Model):
    def predict(self, data):
        if not isinstance(data,list):
            raise Exception("Errore")
        prev_value = None
        diff=None
        tot=None
        for item in data:
            if prev_value != None:
                diff=diff+(item-prev_value)
                prev_value=item
                tot=diff/2
                
        prediction=tot+prev_value
        return prediction