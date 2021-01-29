str='X-DSPAM-Confidence: 0.8475 '

colpot=str.find(':')
num=str[colpot+1:].strip()
fnum=float(num)

print(fnum)
