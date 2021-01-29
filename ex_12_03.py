# Similar a los ejercicios anteriores, pero usando urllib

import urllib.request, urllib.parse, urllib.error

doc=''

url=input('Enter URL: ')

try:
    fhand=urllib.request.urlopen(url)
except:
    print('Invalid URL')
    exit()

for line in fhand:
    doc=doc+line.decode()

print (doc[:3001],'\n')
print('The document has', len(doc), 'characters (only the first 3000 are displayed)')
