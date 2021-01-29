# En este ejercicio se cuenta cuantas veces aparce cada letra en un documento de texto (pero solo las letras a-z)
# y al final imprime las frecuencias en orden descendiente

#print('python dow.py')
letters=dict()
srtlst=list()
abc=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
count=0

fname=input('Enter file name: ')
if len(fname)<1: fname='clown.txt'

try:
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

for line in fhandle:
    #print(line)
    line=line.rstrip()
    line=line.lower()
    #print(line)
    words=line.split()
    #print(words)
    for word in words:
        for char in word:
            if char not in abc:
                continue
            count=count+1
            #print(char, count)
            letters[char]=letters.get(char,0)+1

for k,v in letters.items():
    v=(v/count)*100
    v=round(v,3)
    newtup=(v,k)
    srtlst.append(newtup)

srtlst=sorted(srtlst, reverse=True)

for v,k in srtlst:
    v=str(v)+'%'
    print(k,v)
#print(count)
