num=0
tot=0.0
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
    #fnum=convert(sval)
    num=num+1
    tot=tot+fval
    avg=tot/num

#print('ALL DONE')
print(num, tot, avg)
