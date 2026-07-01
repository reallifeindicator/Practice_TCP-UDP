import socket
import threading

HOST = "10.25.18.19"  #sesuaikan ip address server
PORT = 7000

def receive(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break

            print(f"\nServer : {data.decode('utf-8')}")
            print("Client (Anda) : ", end="", flush=True)

        except:
            break

def send(client):
    while True:
        pesan = input("Client (Anda) : ")

        if pesan.lower() == "/exit":
            client.close()
            break

        client.sendall(pesan.encode("utf-8"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Berhasil terhubung ke server.\n")

threading.Thread(target=receive, args=(client,), daemon=True).start()

send(client)