# En este ejercicio abrimos y leemos un archivo, y guardamos las palabras en él en un diccionario.

diccionario=dict()
fhandle=open('words.txt')

for ln in fhandle:
    ln=ln.rstrip()
    #print(ln)
    wds=ln.split()
    #print(wd)
    for wd in wds:
        wd=wd.lower()
        diccionario[wd]=diccionario.get(wd,0)

#print(diccionario)

# Ahora preguntamos si alguna palabra está en el diccionario

pregunta=input("Input a word to see if it's in the dictionary:"  )
pregunta=pregunta.lower()

if pregunta in diccionario:
    print(pregunta, 'is in the dictionary')
    exit()
else:
    print(pregunta, 'is not in the dictionary')
    exit()
