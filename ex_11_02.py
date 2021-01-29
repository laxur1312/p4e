# Este programa busca ciertos elementos en un archivo, extrae los números y
# promedia todos los números que cumplen con el criterio.

import re

lista=list()
fname=input('Enter file: ')

if len(fname)<1: fname='mbox.txt'

try:
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

for line in fhandle:
    line=line.rstrip()
    x=re.findall('New Revision:\s([0-9.]+)', line)
    if len(x)>0:
        for number in x:
            number=float(number)
            lista.append(number)

total=sum(lista)
avg=total/len(lista)
avg=round(avg,3)

print(avg)
