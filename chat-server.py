import socket
import threading

HOST = "0.0.0.0"
PORT = 8000

def receive(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            print(f"\nClient : {data.decode('utf-8')}")
            print("Server (Anda) : ", end="", flush=True)

        except:
            break

def send(conn):
    while True:
        pesan = input("Server (Anda) : ")

        if pesan.lower() == "/exit":
            conn.close()
            break

        conn.sendall(pesan.encode("utf-8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server aktif di {HOST}:{PORT}")
print("Menunggu client...")

conn, addr = server.accept()

print(f"Client {addr} terhubung.\n")

threading.Thread(target=receive, args=(conn,), daemon=True).start()

send(conn)