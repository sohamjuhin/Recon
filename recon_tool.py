import socket

def scan_port(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"Port {target_port} is open")
        sock.close()
    except socket.error:
        print(f"Could not connect to {target_host}")

def scan_target(target_host, start_port, end_port):
    print(f"Scanning target: {target_host}")
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)

if __name__ == "__main__":
    target_host = input("Enter the target host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    scan_target(target_host, start_port, end_port)
