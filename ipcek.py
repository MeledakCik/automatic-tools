import os,time
import socket
from ping3 import ping
import nmap
import requests
import cv2

def scan_network():
    """
    Mendeteksi perangkat dalam jaringan lokal menggunakan nmap.
    """
    subnet = input("Masukkan subnet (misalnya 192.168.1.0/24): ")
    nm = nmap.PortScanner()
    print("\nMemindai jaringan, harap tunggu...")
    try:
        scan_result = nm.scan(hosts=subnet, arguments='-sn')
        for host in scan_result['scan']:
            state = scan_result['scan'][host].get('status', {}).get('state', 'unknown')
            print(f"IP: {host}, Status: {state}")
    except Exception as e:
        print(f"Kesalahan saat memindai jaringan: {e}")

def check_device_name(ip):
    """
    Mencoba mendapatkan nama perangkat melalui IP.
    """
    try:
        device_name = socket.gethostbyaddr(ip)[0]
        print(f"Nama perangkat (hostname): {device_name}")
    except socket.herror:
        print("Tidak dapat menentukan nama perangkat.")

def get_device_info(ip):
    """
    Mendapatkan informasi perangkat melalui IP menggunakan nmap.
    """
    nm = nmap.PortScanner()
    print("\nMendapatkan informasi perangkat...")
    try:
        scan_result = nm.scan(hosts=ip, arguments='-O')
        os_info = scan_result['scan'][ip].get('osmatch', [])
        if os_info:
            print(f"Informasi perangkat: {os_info[0]['name']} ({os_info[0]['accuracy']}% akurasi)")
        else:
            print("Tidak ada informasi perangkat yang ditemukan.")
    except Exception as e:
        print(f"Kesalahan saat mendapatkan informasi perangkat: {e}")

def lookup_mac(mac_address):
    """
    Mendapatkan vendor perangkat dari alamat MAC.
    """
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Vendor perangkat: {response.text}")
        else:
            print("Vendor tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def capture_camera():
    """
    Mengambil gambar dari kamera dan menyimpannya ke folder.
    """
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Tidak dapat mengakses kamera.")
        return
    
    print("Mengambil foto...")
    time.sleep(2)
    ret, frame = cam.read()
    if ret:
        folder = "photos"
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, "capture.jpg")
        cv2.imwrite(filepath, frame)
        print(f"Foto disimpan di: {filepath}")
    else:
        print("Gagal mengambil foto.")
    cam.release()

def main_menu():
    """
    Menu utama dengan lima pilihan.
    """
    while True:
        print("\nMenu Utama:")
        print("1. Cek IP dalam satu jaringan")
        print("2. Cek nama perangkat melalui IP")
        print("3. Cek informasi perangkat melalui IP")
        print("4. Cek vendor perangkat melalui alamat MAC")
        print("5. Cek kamera atau ambil foto")
        print("0. Keluar")
        
        choice = input("Pilih menu (0-5): ")
        if choice == '1':
            scan_network()
        elif choice == '2':
            ip = input("Masukkan IP perangkat: ")
            check_device_name(ip)
        elif choice == '3':
            ip = input("Masukkan IP perangkat: ")
            get_device_info(ip)
        elif choice == '4':
            mac = input("Masukkan alamat MAC: ")
            lookup_mac(mac)
        elif choice == '5':
            capture_camera()
        elif choice == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    os.system('clear')
    main_menu()
