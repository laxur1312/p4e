#En este ejercicio definimos una función que borra el primer y último elementos de una lista y otra que borra todos menos el primero y el último

print('La lista original es:')

lista=['a','b','c','d','e','f']
print(lista)

#Definimos la función que borra el primer y último elementos
def chop(t):
    del t[0]
    del t[len(t)-1]
    return None

#Definimos la función que borra todo menos el primer y último elementos
def middle(t):
    del t[1:len(t)-1]

chop(lista)
print('La lista después de usar chop es:')
print(lista)

#Reintroducimos la lista original para poder apreciar la función middle mejor

lista=['a','b','c','d','e','f']
middle(lista)
print('La lista después de usar middle es:')
print(lista)
