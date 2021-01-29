handle=open('mbox-short.txt')
for line in handle:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    parts=line.split()
    
    # Guardian
    if len(parts)<3:
        continue

    else:
        print(parts[2])
