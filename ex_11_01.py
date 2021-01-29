# Introducimos una regex y el programa cuenta cuantos matches hay en el archivo

import re
count=0


fname='mbox.txt'
fhandle=open(fname)

print('python grep.py')
regex=input('Enter a regular expression: ')

for line in fhandle:
    line=line.rstrip()
    x=re.findall(regex,line)
    if len(x)>0:
        count=count+1

print(fname, 'had', count, 'lines that matched', regex)
