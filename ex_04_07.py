# Exercise 4.7

def computegrade(x):
    if x>=0.9: y='A'
    elif x>=0.8: y ='B'
    elif x>=0.7: y = 'C'
    elif x>=0.6: y = 'D'
    else: y='F'
    return y


while True:
    score=input('Enter a score between 0.0 and 1.0 to obtain your grade.\nType "done" to exit: ')
    if score=='done':
        exit()
    try:
        fscore=float(score)
    except:
        print('Bad score')
        continue
    if fscore>1.0 or fscore<0.0:
        print('Bad score')
        continue
    grade=computegrade(fscore)

    print('Your grade is', grade)
