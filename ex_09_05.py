# En este ejercicio contamos cuantos mensajes llegan de cada dominio de correo electónico

print('python dow.py')
domain=dict()

fname=input('Enter file name: ')


try:
    if len(fname)<1: fhandle='mbox-short.txt'
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

for ln in fhandle:
    ln=ln.rstrip()
    if not ln.startswith('From '):
        continue
    wds=ln.split('@')
    #print(wds)
    nwds=wds[1]
    nwds=nwds.split()
    #print(nwds)
    dmn=nwds[0]
    #print(dmn)
    domain[dmn]=domain.get(dmn,0)+1

print(domain)
