lista=list()

while True:
    num=input("Input numbers and you'll get the largest and smallest at the end.\nWrite done when finished: ")
    if num=='done':
        print()
        break
    try:
        fnum=float(num)
    except:
        print('Invalid input')
        continue
    lista.append(fnum)



print('Los números que introdujiste son:',lista,'\n')
print('El número más grande es:', max(lista),'\n')
print('El número más pequeño es:', min(lista),'\n')
