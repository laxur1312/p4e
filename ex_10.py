# En este ejercicio imprimimos las 5 palabras más comunes en un documento usando tuples

fname=input('Enter file name: ')
if len(fname)<1 : fname='clown.txt'

try:
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

counts=dict()
revlist=list()
lst=list()

for line in fhandle:
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

for k,v in counts.items():
    newtup=(v,k)
    revlist.append(newtup)

revlist=sorted(revlist, reverse=True)
for v,k in revlist:
    newnewtup=(k,v)
    lst.append(newnewtup)

print(lst[:5])
