hours = input('How many hours do you work? ')
fhours = float(hours)
rate = input('How much do you get paid by hour? ')
frate = float(rate)
pay= frate*fhours
if fhours<=40:
    print('You get paid', pay)
else:
    ovt=(fhours-40)*1.5
    pay=(40*frate)+(ovt*frate)
    print('Since you worked over 40 hours, you get paid', pay)
print ('Bye bye!')
