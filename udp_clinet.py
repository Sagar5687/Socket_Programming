import socket
server_ip='localhost'
server_port=12345

client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    message=input("Enter the message (bye to quit ): ")
    client_socket.sendto(message.encode(),(server_ip,server_port))

    if message.lower() == "bye":
        break

    data, _=client_socket.recvfrom(1024)
    response=data.decode()
    print("[Respones received from server]: ",response)
    

client_socket.close()
