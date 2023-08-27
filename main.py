import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("14:5a:fc:3e:c3:9e", 4))
server.listen()

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message:")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass