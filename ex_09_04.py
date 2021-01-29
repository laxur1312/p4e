# Este ejercicio es idéntico al anterior, pero al final nos dice cual es la dirección de correo mas común
# y con cuantas ocurrencias

print('python dow.py')
adress=dict()

fname=input('Enter file name: ')


try:
    #if len(fname)<1: fhandle='mbox-short.txt'
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

bigAdress=None
bigCount=None

for key,value in adress.items():
    if bigCount is None or bigCount<value:
        bigCount=value
        bigAdress=key

print(bigAdress, bigCount)
