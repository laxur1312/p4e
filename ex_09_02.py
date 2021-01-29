# En este ejercicio contamos cuantos mensajes llegan en cada día de la semana

print('python dow.py')
days=dict()

fname=input('Enter file name: ')


try:
    if len(fname)<1: fhandle='mbox-short.txt'
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

for ln in fhandle:
    ln=ln.rstrip()
    if not ln.startswith('From'):
        continue
    wds=ln.split()
    if len(wds)<3:
        continue
    dotw=wds[2]
    #print(dotw)
    days[dotw]=days.get(dotw,0)+1

print(days)
