import os, time, sys,random
os.system("clear")
def parat():
	os.system("pkg update")
	os.system("pkg upgrade")
	print("\033[1;36;40m[+] Termux Is Updated and Upgraded")
	os.system("pkg install python")
	print("\033[1;36;40m[+] Python is Installed")
	os.system("pkg install python2")
	print("\033[1;36;40m[+] Python2 Is Installed")
	os.system("pkg install git")
	print("\033[1;36;40m[+] Git Is Installed")
	os.system("pkg install wget")
	print("\033[1;36;40m[+] wget Is Installed")
	os.system("pkg install curl")
	print("\033[1;36;40m[+] curl Is Installed")
	os.system("pkg install openssh")
	print("\033[1;36;40m[+] openssh Is Installed")
	os.system("pkg install figlet")
	print("\033[1;36;40m[+] figlet Is Installed")
	os.system("pkg install unstable-repo")
	print("\033[1;36;40m[+] unstable-repo Is Installed")
	os.system("git clone https://github.com/fadinglr/Parat.git")
	print("[+] Parat is successfully installed")
	b=str(input("\033[1;31;40mDo you want to exit? (y/n)"))
	if b =="y":
		os.system("exit")
	elif b == "n":
		os.system("python new.py")
parat()