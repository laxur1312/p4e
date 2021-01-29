# En este ejercicio, el usuario introduce un URL y el browser la abre

import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url=input('Enter URL: ')

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
    print(data.decode())
mysock.close()
