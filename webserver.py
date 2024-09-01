from socket import *
serverPort = 9966                            # port number
serverSocket = socket(AF_INET, SOCK_STREAM)  
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('The server is ready to receive\n')   # message to start receiving requests
 
while True: 
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode('latin-1', 'replace') 
    request_line = sentence.split('\r\n')[0]
    print(sentence)
    if len(request_line.split(' ')) >= 2: 
        method, requestPath = request_line.split(' ')[:2]
    else:
        method, requestPath = '', ''       
    print(method)
    print(requestPath) 
    # checking the request
    if method == 'GET': 
        if requestPath in ['/', '/index.html', '/main_en.html', '/en']: #request to send main_en.html & main_en.css
             with open(r"C:\Users\hp\Desktop\network_project\main_en.html", "r") as f1, open(r"C:\Users\hp\Desktop\network_project\main_en.css", "r") as f2:
                  f1Content = f1.read()
                  f2Content = f2.read() 
                      
             combined_content = f"{f1Content}\n<style>{f2Content}</style>"
             response = f"HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{combined_content}" #response 
             connectionSocket.sendall(response.encode()) #send response to connectionSocket
        elif requestPath == "/ar":   #request to send main_ar.html & ar.css
             with open(r"C:\Users\hp\Desktop\network_project\main_ar.html", "r", encoding='utf-8') as f1, open(r"C:\Users\hp\Desktop\network_project\ar.css", "r") as f2:
                  f1Content = f1.read()
                  f2Content = f2.read() 
             combined_content = f"{f1Content}\n<style>{f2Content}</style>"
             response = f"HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n{combined_content}"#response
             connectionSocket.sendall(response.encode()) #send response to connectionSocket
        elif requestPath == "/cr":  #(request) 307 temporary redirect to cornell website
             connectionSocket.send("HTTP/1.1 307 temporary redirect\r\n".encode())
             connectionSocket.send("content-type:test/html\r\n".encode()) 
             connectionSocket.send("location:https://www.cornell.edu\r\n".encode())
             connectionSocket.send("\r\n".encode()) #send response to connectionSocket
        elif requestPath == "/so":   #(request) 307 temporary redirect to stackoverflow website
             connectionSocket.send("HTTP/1.1 307 temporary redirect\r\n".encode())
             connectionSocket.send("content-type:test/html\r\n".encode())
             connectionSocket.send("location:https://stackoverflow.com\r\n".encode())
             connectionSocket.send("\r\n".encode()) #send response to connectionSocket
        elif requestPath == "/rt":    #(request) 307 temporary redirect to ritaj website
             connectionSocket.send("HTTP/1.1 307 temporary redirect\r\n".encode())
             connectionSocket.send("content-type:test/html\r\n".encode())
             connectionSocket.send("location:https://ritaj.birzeit.edu\r\n".encode())
             connectionSocket.send("\r\n".encode()) #send response to connectionSocket
        elif requestPath == "/image2.png":   # request image.png
             connectionSocket.send("HTTP/1.1 200 ok \r\n".encode())
             connectionSocket.send("content-Type:image/png\r\n".encode())
             connectionSocket.send("\r\n".encode())
             image =open (r"C:\Users\hp\Desktop\network_project\image2.png","rb")
             connectionSocket.send(image.read())
             connectionSocket.send("\r\n".encode()) #send response to connectionSocket
        elif requestPath == "/image1.jpg":    # request image.jpg
             connectionSocket.send("HTTP/1.1 200 ok \r\n".encode())
             connectionSocket.send("content-Type:image/jpeg\r\n".encode())
             connectionSocket.send("\r\n".encode())
             image = open(r"C:\Users\hp\Desktop\network_project\image1.jpg", "rb")
             connectionSocket.send(image.read()) #send response to connectionSocket
        elif requestPath == "/.png":
             connectionSocket.send("HTTP/1.1 200 ok \r\n".encode())
             connectionSocket.send("content-Type:image/png\r\n".encode())
             connectionSocket.send("\r\n".encode())
             image =open (r"C:\Users\hp\Desktop\network_project\image2.png","rb")
             connectionSocket.send(image.read())
             connectionSocket.send("\r\n".encode()) #send response to connectionSocket
        elif requestPath == "/.jpg":
             connectionSocket.send("HTTP/1.1 200 ok \r\n".encode())
             connectionSocket.send("content-Type:image/jpeg\r\n".encode())
             connectionSocket.send("\r\n".encode())
             image = open(r"C:\Users\hp\Desktop\network_project\image1.jpg", "rb")
             connectionSocket.send(image.read()) #send response to connectionSocket
        elif requestPath == "/.css":    #request a css file
             f1 = open(r"C:\Users\hp\Desktop\network_project\CSS.css", "r")
             response = f"HTTP/1.1 200 OK\r\nContent-type: text/css\r\n\r\n{f1.read()}"
             connectionSocket.sendall(response.encode()) #send response to connectionSocket
        elif requestPath == "/.html":    #request a html file
             with open(r"C:\Users\hp\Desktop\network_project\file.html", "r") as f1:
                  file = f1.read()
             response = f"HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{file}"
             connectionSocket.sendall(response.encode()) #send response to connectionSocket
        elif requestPath == "/local_file.html":    #request a local html file
             with open(r"C:\Users\hp\Desktop\network_project\local_file.html", "r") as f1:
                  file = f1.read()
             response = f"HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{file}"
             connectionSocket.sendall(response.encode()) #send response to connectionSocket
        else:            # when anything other than any of the previous requests is requested then request the Error page
             with open(r"C:\Users\hp\Desktop\network_project\ERROR.html", "r") as f1, open(r"C:\Users\hp\Desktop\network_project\ERROR.css", "r") as f2:
                 f2Content = f2.read()
                 f1Content = (f1.read()).replace('{ip}', addr[0]).replace('{port}', str(addr[1])) #take the values of the port and the IP of the client to be shown
             combine = f"{f1Content}\n<style>{f2Content}</style>"
             response = f"HTTP/1.1 404 Not Found\r\nContent-type: text/html\r\n\r\n{combine}"
             connectionSocket.sendall(response.encode()) #send response to connectionSocket
        connectionSocket.close() 
        