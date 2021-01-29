print('python shout.py')
fname=input('Enter a file name: ')

try:
    fhandle=open(fname)
except:
    print('Archivo no encontrado')
    exit()

for line in fhandle:
    rline=line.rstrip()
    rline=rline.upper()
    print(rline)
