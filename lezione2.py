def sum_list(lista):
    risultato=0
    if lista == []:
        return None
    for item in lista:
        risultato=risultato+item
    return risultato
my_list=[]

print("sommatoria vale:{}".format(sum(my_list)))