handle=open('mbox-short.txt')
count=0

for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    parts=line.split()

    # Guardian
    if len(parts)<2:
        continue

    else:
        count=count+1
        print(parts[1])

print('There are', count, 'lines in the file with From as the first word.')
