# En este ejercicio contamos cuantos mensajes llegan de cada dirección de correo

print('python dow.py')
adress=dict()

fname=input('Enter file name: ')
if len(fname)<1: fname='mbox-short.txt'

try:
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

for ln in fhandle:
    ln=ln.rstrip()
    if not ln.startswith('From '):
        continue
    #print(ln)
    wds=ln.split()
    if len(wds)<2:
        continue
    mail=wds[1]
    adress[mail]=adress.get(mail,0)+1

print(adress)
