import time
from datetime import datetime as dt
import colorama 
from colorama import Fore, Back, Style
import socket 
import os 
import sys 


def CS(X):
    time.sleep(X)
    os.system("clear")

def socknames():
    myHostName = socket.gethostname()
    myIP = socket.gethostbyname(myHostName)
    print("\033[35m[\033[36m*\033[35m] With Loopback Addr -> {}".format(myIP))

def block2():
    hosts_path = "/etc/hosts"
    redirect = '127.0.0.1'
    print("--------------------- UP TO 6 WEBSITES ------------- ")
    op1 = str(input(" Website @> "))
    op2 = str(input(" Website @> "))
    op3 = str(input(" Website @> "))
    op4 = str(input(" Website @> "))
    op5 = str(input(" Website @> "))
    op6 = str(input(" Website @> "))
    website_list = [f"{op1}",f"{op2}",f"{op3}",f"{op4}",f"{op5}",f"{op6}" ]  
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        time.sleep(4)
                        print(f"\033[35m[\033[36m*\033[35m] Blocking Host      -> ", website_list)
                        socknames()
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)    
        try:
            hosts_path = "/etc/hosts"
            with open('/etc/hosts', 'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open('months.txt', 'w') as fw:
                    for line in lines:
                        if ptr != 6:
                            fw.write(line)
                        ptr += 1
            print("\033[35m[\033[36m*\033[35m] File Write Deleted......")
        except:
            print("[!] [DATA]->[ERROR]->[SYS]->[WRITE] ")
            print(f"[!] HOSTS COULD NOT BE DELETED FROM {hosts_path}")
            print("[!] THIS CAN RESULT IN A PERMANANT LOCK FROM THE ")
            print("[!] TARGETED WEBSITES CATTING THE HOST FOR VIEW ")
            print("--=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=--=-=-=-=--=-=-")
            os.system("cat /etc/hosts")



def block1():
    us = str(input(" Website @> "))
    website_list = [f"{us}"]  
    while True:
        hosts_path = "/etc/hosts"
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        time.sleep(4)
                        print(f"\033[35m[\033[36m*\033[35m] Blocking Host      -> ", website_list)
                        socknames()
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)    
        try:
            hosts_path = "/etc/hosts"
            with open('/etc/hosts', 'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open('months.txt', 'w') as fw:
                    for line in lines:
                        if ptr != 6:
                            fw.write(line)
                        ptr += 1
            print("\033[35m[\033[36m*\033[35m] File Write Deleted......")
        except:
            print("[!] [DATA]->[ERROR]->[SYS]->[WRITE] ")
            print(f"[!] HOSTS COULD NOT BE DELETED FROM {hosts_path}")
            print("[!] THIS CAN RESULT IN A PERMANANT LOCK FROM THE ")
            print("[!] TARGETED WEBSITES CATTING THE HOST FOR VIEW ")
            print("--=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=--=-=-=-=--=-=-")
            os.system("cat /etc/hosts")

def menu():
    print("""
 __     __               __              ___              
|  |--.|  |.-----..----.|  |--. ______ .'  _|.-----..----.
|  _  ||  ||  _  ||  __||    < |______||   _||  -__||   _|
|_____||__||_____||____||__|__|        |__|  |_____||__|
Block websites and host names          ArkAngeL43  
--------------------------------------------------------                                                         
    [1] -> Block A Website 
    [2] -> Block Multiple 
    """)
    option = str(input(" Options @> "))

    if option == '1':
        block1()
    elif option == '2':
        block2()


if __name__ == "__main__":
    try:
        CS(1)
        menu()
    except KeyboardInterrupt:
        print("\n")
        hosts_path = "/etc/hosts"
        print("""\033[31mIF THIS MESSAGE APPEARED PLEASE DELETE IT MANUALLY OR 
        IF A WEBSITE IS STILL BEING BLOCKED
        """)
        print("\033[31m----------------------------------------------------")
        print("\033[31m[!] [DATA]->[ERROR]->[SYS]->[WRITE] ")
        print(f"\033[31m[!] HOSTS COULD NOT BE DELETED FROM {hosts_path}")
        print("\033[31m[!] THIS CAN RESULT IN A PERMANANT LOCK FROM THE ")
        print("\033[31m[!] TARGETED WEBSITES CATTING THE HOST FOR VIEW ")
        print("\033[31m--=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=--=-=-=-=--=-=-")
        print(Fore.GREEN+"Printing File of hosts......")
        time.sleep(2)
        os.system(f"cat {hosts_path}")
