# UDP Server in Python
# This python server uses socket like the TCP server. However, we instead
# utilize User Datagram Protocol. This protocol tolerates low latency and
# tolerates loss of connection.
import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    # overriding the default with params Socket family and socket type
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print "Server started."
    while True:
        data, address = s.recvfrom(1024)
        print "Message from: " + str(address)
        print "From connected user: "  + str(data)
        data = str(data).upper()
        print "Sending: " + str(data)
        # UDP does not always know where to send data, so we keep the address
        s.sendto(data, address)
    s.close()

if __name__ == '__main__':
    Main()
