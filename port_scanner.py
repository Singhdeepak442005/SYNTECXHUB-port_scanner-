import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print("Scanning ports...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

            s.close()

        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            return
        except socket.error:
            continue

    print("\n==============================")
    print(" Scan Completed Successfully ")
    print("==============================")

    if open_ports:
        print("Open Ports Found:", open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target, start_port, end_port)
