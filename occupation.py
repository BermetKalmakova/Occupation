filename = 'occupations.csv'
f = open(filename,'rU')
text = f.read()

dict = {}
L = text.split("\n")
i = 1
while i < len(L):
    if L[i][0] == '"':
        index = L[i].find('"', beg = 1, end = len(L[i]))
        dict[float(L[i][index+1:])] = L[i][1:index]
    
