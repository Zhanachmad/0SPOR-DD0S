import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")
c = input(">>>: ")

if c == "0":
     os.system("pip install requests")
     os.system("pip install progressbar")
     os.system("pip install randomstring")
     os.system("apt-get install nodej-lts")
     os.system("apt-get install npm")
     os.system("npm install os")
elif c == "1":
     os.system("pip3 install requests")
     os.system("pip3 install progressbar")
     os.system("pip3 install randomstring")
     os.system("apt-get install nodej-lts")
     os.system("apt-get install npm")
     os.system("npm install os")
     print("Done.")



