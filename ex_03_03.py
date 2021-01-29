# Exercise 3.3

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
    if fscore>=0.9: grade='A'
    elif fscore>=0.8: grade ='B'
    elif fscore>=0.7: grade = 'C'
    elif fscore>=0.6: grade = 'D'
    else: grade='F'
    print('Your grade is', grade)
