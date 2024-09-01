from socket import *
import time
import subprocess
import platform

serverPort = 9955
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print ('The server is ready to receive')
allowedIDS = ["1210279", "1212145"]
while True:
     clientSocket, addr = serverSocket.accept()
     id = clientSocket.recv(1024).decode()
     print("recieved id: ", id)
     if id in allowedIDS:
         print('The OS will lock the screen after 10 seconds')
         clientSocket.send("Locking screen in 10 seconds...".encode())
         time.sleep(10)
         system_platform = platform.system()
         if system_platform == "Windows":
            subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
         elif system_platform == "Linux":
             subprocess.run(["gnome-screensaver-command", "--lock"])
         elif system_platform == "Darwin":
             subprocess.run(["open", "-a", "ScreenSaverEngine"])
     else:
         print('ERROR: Invalid ID')
         clientSocket.send("ERROR: Invalid ID".encode())