from tkinter.ttk import _Padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore # Tambahkan ini
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
from cryptography.hazmat.backends import default_backend  # type: ignore
import os
import base64

def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),  # Menyertakan algoritma hash SHA256
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    return kdf.derive(password.encode())


# Fungsi untuk mengenkripsi data
def encrypt(data: str, key: bytes):
    iv = os.urandom(16)  # Inisialisasi vektor
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Padding untuk memastikan panjang data sesuai blok AES
    padder = _Padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    
    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(iv + encrypted).decode()

# Fungsi untuk mendekripsi data
def decrypt(encrypted_data: str, key: bytes):
    raw_data = base64.b64decode(encrypted_data)
    iv = raw_data[:16]
    encrypted = raw_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
    
    # Remove padding
    unpadder = _Padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted.decode()

# Fungsi untuk mengenkripsi skrip Python
def encrypt_script(file_path, password):
    with open(file_path, 'r') as file:
        script_code = file.read()

    salt = os.urandom(16)  # Salt acak
    key = generate_key(password, salt)

    encrypted_code = encrypt(script_code, key)

    # Menyimpan hasil enkripsi ke file
    with open(f"{file_path}.enc", 'w') as enc_file:
        enc_file.write(base64.b64encode(salt).decode() + "\n" + encrypted_code)

# Fungsi untuk mendekripsi dan mengeksekusi skrip Python
def decrypt_and_execute(file_path, password):
    with open(file_path, 'r') as enc_file:
        encrypted_data = enc_file.read()

    salt_b64, encrypted_code_b64 = encrypted_data.split("\n", 1)
    salt = base64.b64decode(salt_b64)
    encrypted_code = encrypted_code_b64.strip()

    key = generate_key(password, salt)
    decrypted_code = decrypt(encrypted_code, key)

    # Menyimpan skrip yang didekripsi sebagai file sementara
    temp_file = 'ipcek.py'
    with open(temp_file, 'w') as temp_script:
        temp_script.write(decrypted_code)

    # Menjalankan skrip yang didekripsi
    os.system(f'python {temp_file}')

# Contoh penggunaan
if __name__ == "__main__":
    password = "tes"

    # Enkripsi skrip Python (misalnya 'test_script.py')
    encrypt_script('ipcek.py', password)

    # Dekripsi dan eksekusi skrip terenkripsi
    decrypt_and_execute('ipcek.py.enc', password)
