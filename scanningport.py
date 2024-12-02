import socket

# Fungsi untuk memeriksa port yang terbuka
def scan_ports(target_ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout 1 detik
        result = sock.connect_ex((target_ip, port))  # Coba terhubung ke IP dan port
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Contoh Penggunaan
target_ip = "192.168.11.190"  # Ganti dengan IP target yang akan dipindai
ports = [22, 80, 443, 8080, 3306]  # Daftar port yang ingin dipindai
open_ports = scan_ports(target_ip, ports)

if open_ports:
    print(f"Port terbuka di {target_ip}: {open_ports}")
else:
    print(f"Tidak ada port yang terbuka di {target_ip}")
