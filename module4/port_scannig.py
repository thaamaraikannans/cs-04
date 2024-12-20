import socket

def port_scanning( port):
    target = "65.0.4.157"
    tcp = socket.socket()
    tcp.settimeout(3)
    response = tcp.connect_ex((target, port))
    if response == 0:
        print(f"port {port} is open")
    else:
        print(f"port {port} is closed")
    return


for po in range(1, 100):
    port_scanning(po)