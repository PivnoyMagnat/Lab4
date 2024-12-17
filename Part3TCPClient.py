import socket
import os

def send_file(file_path, host='127.0.0.1', port=65432, buffer_size=4096):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    file_name = os.path.basename(file_path)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")
    client_socket.send(file_name.encode())

    with open(file_path, "rb") as file:
        while (data := file.read(buffer_size)):
            client_socket.sendall(data)

    print(f"File {file_name} successfully sent to the server")
    client_socket.close()

if __name__ == "__main__":
    file_to_send = input("Enter the path to the file you want to send: ").strip()
    send_file(file_to_send)