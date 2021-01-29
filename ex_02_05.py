print('Converitdor de Celsius a Farenheit\n')

while True:
    Ctemp=input('Introduce una temperatura en grados Celsius\npara convertirla a grados Farenheit.\nEscribe "fin" para terminar: ')
    if Ctemp == 'fin':
        exit()
    try:
        fCtemp=float(Ctemp)
        Ftemp=(fCtemp*1.8)+32
        print(fCtemp, 'grados Celsius son', Ftemp, 'grados Farenheit')
        break
    except:
        print('Argumento inválido. Trata de nuevo.')
        continue
