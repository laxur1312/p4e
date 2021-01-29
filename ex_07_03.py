# Este ejercicio es idéntico al anterior, pero imprime un mensaje chusco si se introduce el easter egg

count=0
sum=0
easter_egg='na na boo boo'

print('python shout.py')
fname=input('Enter a file name: ')

if fname==easter_egg:
    print("NA NA BOO BOO TO YOU! You've been punk'd!")
    exit()

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
