# En este ejercicio vemos cual es la dirección de correo que aparece más veces en un documnento
# y la imprimimos usando tuples.

print('python dow.py')
adress=dict()
srtlst=list()

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

for k,v in adress.items():
    newtup=(v,k)
    srtlst.append(newtup)

srtlst=sorted(srtlst, reverse=True)

del srtlst[1:len(srtlst)+1]

for v,k in srtlst:
    print(k,v)
