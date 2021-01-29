# En este ejercicio contamos las horas a las que se reciven los correos
# usando tuples.

print('python dow.py')
hours=dict()
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
    time=wds[5]
    #print(time)
    parts=time.split(':')
    hour=parts[0]
    #print(hour)
    hours[hour]=hours.get(hour,0)+1

for k,v in hours.items():
    newtup=(k,v)
    srtlst.append(newtup)

srtlst=sorted(srtlst)

for k,v in srtlst:
    print(k,v)
