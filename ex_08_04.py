# En este ejercicio se abre un archivo, se añaden palabras a una lista y se ordenan alfabeticamente

lista_original=list()

fh=open('romeo.txt')


# Primero imprimimos el archivo para ver que todo funcione correctamente
#for line in fh:
    #line=line.rstrip()
    #print(line)

#Luego separamos palabra por palabra el documento

#for linea in fh:
    #linea=linea.rstrip()
    #partes=linea.split()
    #print(partes)

#Luego añadimos las palabras a la lista original si es que no están en ella

#for linea in fh:
    #linea=linea.rstrip()
    #partes=linea.split()
    #print(partes)
    #for i in partes:
        #if not i in lista_original:
            #lista_original.append(i)
#print(lista_original)

# Por último, hacemos una copia de la lsita original por si acaso, y ordenamos los elementos de la lista que fueron añadidios desde el documento

copia=lista_original[:]

for linea in fh:
    linea=linea.rstrip()
    partes=linea.split()
    for i in partes:
        if not i in lista_original:
            lista_original.append(i)
    lista_original.sort()

print(lista_original)
