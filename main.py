import time
import socket
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR, 
                         1) # reuse address

server_socket.bind((SERVER_HOST, 
                    SERVER_PORT))

server_socket.listen(5) # backlog parameter establishes the queue

print(f"Listening on port {SERVER_PORT} ...")

print("Current working directory:", os.getcwd())

while True:
    
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    
    print(request)
    headers = request.split('\n')
    
    try:
        first_header_components = headers[0].split()
        http_method = first_header_components[0]
        path = first_header_components[1]
    except IndexError:
        print("Received malformed request")
        client_socket.close()
        continue

    if path == '/':
        try:
            with open('index.html', 'r') as fin:
                content = fin.read()
            response = 'HTTP/1.1 200 OK\n\n' + content
        except FileNotFoundError:
            print("Error: index.html not found")
            response = 'HTTP/1.1 404 Not Found\n\nFile not found'
        except Exception as e:
            print(f"Error reading file: {e}")
            response = 'HTTP/1.1 500 Internal Server Error\n\nServer error'
        finally:
            client_socket.sendall(response.encode())
            client_socket.close()
        
        