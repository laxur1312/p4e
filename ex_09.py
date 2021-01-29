# In this exercise we count which is the most common word in a file and how many times it's in it

fname=input('Enter file name: ')

try:
    fhandle=open(fname)
except:
    print('File not found.')
    exit()

counts=dict()

for line in fhandle:
    #print(line)
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

# Now we want to find the most common word and how many times it occurs.

bigWord=None
bigCount=None

for key,value in counts.items():
    #print(key,value)
    if bigCount is None or bigCount < value:
        bigCount=value
        bigWord=key

print('In file', fname, 'the most common word is', bigWord, 'with', bigCount, 'occurences.')
