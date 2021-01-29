# En este ejercicio, el usuario introduce un URL y se imprimen el npumero todal de caracteres y los primeros 3000 caracteres.

import socket

count=0
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url=input('Enter URL: ')
doc=''

try:
    domain=url.split('/')[2]
except:
    print('Invalid URL')
    exit()
#print(domain)
try:
    mysock.connect((domain, 80))
except:
    print('Invalid URL')
    exit()

cmd = ('GET '+url+ ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    data=data.decode()
    doc=doc+data
    count+= len(data)
mysock.close()

print(doc[:3000],'\n')
print('The page has', count, 'characters (only the first 3000 are displayed)')
