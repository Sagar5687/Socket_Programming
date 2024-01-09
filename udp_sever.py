import socket
import threading

def start_chatbot():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    sock.bind(server_address)
    print("Chatbot started.")
    while True:
        data, address = sock.recvfrom(1024)
        message = data.decode()
        print(f"Received message: {message} from {address}")
        client_thread = threading.Thread(target=process_client_message, args=(sock, message, address))
        client_thread.start()

def process_client_message(sock, message, address):
    response = input("Enter response : ")
    sock.sendto(response.encode(), address)

start_chatbot()

 
