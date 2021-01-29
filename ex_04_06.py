hours = input('How many hours do you work? ')
try:
    fhours = float(hours)
except:
    fhours =-1
while fhours==-1:
    print('Error, please enter a numeric input ')
    hours = input()
    try:
        fhours = float(hours)
    except:
        fhours =-1
rate = input('How much do you get paid by hour? ')
try:
    frate = float(rate)
except:
    frate =-1
while frate==-1:
    print('Error, please enter a numeric input ')
    rate = input()
    try:
        frate = float(rate)
    except:
        frate =-1
def computepay(t,m):
    if t<=40:
        normal=t*m
        return normal
    else:
        ovt=(t-40)*1.5
        overtime=(40*m)+(ovt*m)
        return overtime
pay=computepay(fhours,frate)
print('You get paid', pay)
print ('Bye bye!')
