count=0
sum=0

print('python shout.py')
fname=input('Enter a file name: ')

try:
    fhandle=open(fname)
except:
    print('Archivo no encontrado')
    exit()

for line in fhandle:
    rline=line.rstrip()
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    colpot=line.find(':')
    newline=line[colpot+1:].strip()
    fnewline=float(newline)
    count=count+1
    sum=sum+fnewline
    print (fnewline)

print(sum/count)
