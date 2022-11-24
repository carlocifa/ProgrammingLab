def sum_csv(nome_file):
    values=[] 
    file=open(nome_file,'r') 
    for line in file:
        elements=line.split(',')
        if elements[0]!='Date':
            value=elements[1]
            values.append(float(value))
    file.close()
    if(len(values)==0):
        return None
    else:
        return sum(values)

