large=None
small=None
#def convert(inp):
    #try:
        #finp=float(inp)
    #except:
        #print('Invalid input')
        #continue
    #return finp

while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input')
        continue

    if large is None:
        large=fval
    elif fval> large:
        large=fval

    if small is None:
        small=fval
    elif fval< small:
        small=fval


#print('ALL DONE')
print('The largest number is', large, 'and the smallest is', small)
