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
pay= frate*fhours
if fhours<=40:
    print('You get paid', pay)
else:
    ovt=(fhours-40)*1.5
    pay=(40*frate)+(ovt*frate)
    print('Since you worked over 40 hours, you get paid', pay)
print ('Bye bye!')
