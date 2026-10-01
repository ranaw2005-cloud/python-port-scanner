import socket
from datetime import datetime


def scan_port(host, port, timeout=0.5):
    """Return True if a TCP connection to host:port succeeds."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def get_service(port):
    """Look up the common service name for a port, if there is one."""
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def main():
    print("Only scan systems you own or have permission to scan.\n")
    target = input("Target host [127.0.0.1]: ").strip() or "127.0.0.1"
    start = int(input("Start port [1]: ") or 1)
    end = int(input("End port [1024]: ") or 1024)

    if not (1 <= start <= end <= 65535):
        print("Invalid port range.")
        return

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Could not resolve that host.")
        return

    print(f"\nScanning {target} ({ip}) ports {start}-{end}")
    print(f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    open_ports = []
    for port in range(start, end + 1):
        if scan_port(ip, port):
            service = get_service(port)
            open_ports.append((port, service))
            print(f"[OPEN] {port}/tcp  {service}")

    print(f"\nDone. {len(open_ports)} open port(s) found.")


if __name__ == "__main__":
    main()