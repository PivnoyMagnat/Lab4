import threading
import socket

def test_client(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Response: {data.decode('utf-8')}")

if __name__ == "__main__":
    host, port = '127.0.0.1', 65432
    threads = []
    for i in range(5):
        t = threading.Thread(target=test_client, args=(host, port, f"Epye, it works, response client {i+1}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()