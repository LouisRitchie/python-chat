# UDP Server in Python
# This python server uses socket like the TCP server. However, we instead
# utilize User Datagram Protocol. This protocol tolerates low latency and
# tolerates loss of connection.
import socket
import time

host = '127.0.0.1'
port = 5000

# overriding the default with params Socket family and socket type
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
# making it asynchronous
s.setblocking(0)

quitting = False
print "Server started."

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)

        # time.ctime() prints a timestamp. Investigate further.
        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            s.sendto(data, client)

    except:
        pass

s.close()
