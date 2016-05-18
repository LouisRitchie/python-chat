# client.py -- Client for the chat app
# Press enter to refresh and see new messages - no "hot reloading"
#
import socket
import threading # used for asynchronous purposes.
import time

tLock = threading.Lock()
shutdown = False

def receiving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0 # will pick any open port on the PC

server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

# Passing a target and args that are the name and socket
rT = threading.Thread(target = receiving, args=('RecvThread', s))
rT.start()

alias = raw_input("Name: ")
message = raw_input(alias + "-> ")
while message != "q":
    if message != "":
        s.sendto(alias + ": " + message, server)
    tLock.acquire()
    message = raw_input(alias + "-> ")
    tLock.release()
    time.sleep(0.2)

shutdown = True
rT.join()
s.close()
