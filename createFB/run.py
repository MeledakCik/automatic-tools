import threading
from queue import Queue
import requests
import random
import string
import json
import hashlib
from faker import Faker
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
> › Github :- @jatintiwari0 
> › By      :- JATIN TIWARI
> › Proxy Support Added by @coopers-lab
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                
""")
print('\x1b[38;5;208m⇼' * 60)

# Fungsi untuk menghasilkan string acak
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Fungsi mendapatkan domain email dari API mail.tm
def get_mail_domains(proxy=None):
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('hydra:member', [])
    except requests.RequestException as e:
        logging.error(f'Error mendapatkan domain email: {e}')
    return None

# Fungsi untuk membuat akun mail.tm
def create_mail_tm_account(proxy=None):
    fake = Faker()
    mail_domains = get_mail_domains(proxy)
    
    if not mail_domains:
        logging.error("[×] Tidak ada domain email yang tersedia.")
        return None, None, None, None, None

    domain = random.choice(mail_domains)['domain']
    username = generate_random_string(10)
    password = fake.password()
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
    first_name = fake.first_name()
    last_name = fake.last_name()

    url = "https://api.mail.tm/accounts"
    headers = {"Content-Type": "application/json"}
    data = {"address": f"{username}@{domain}", "password": password}

    try:
        response = requests.post(url, headers=headers, json=data, proxies=proxy, timeout=5)
        response.raise_for_status()
        return f"{username}@{domain}", password, first_name, last_name, birthday
    except requests.RequestException as e:
        logging.error(f'[×] Gagal membuat email: {e}')
    
    return None, None, None, None, None

# Fungsi untuk mendaftarkan akun Facebook
def register_facebook_account(email, password, first_name, last_name, birthday, proxy=None):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req, proxy)

    if 'error_code' in reg:
        logging.error(f"[×] Registrasi gagal. Response: {reg}")
        return None

    user_id = reg.get('new_user_id', 'UNKNOWN')
    token = reg.get('session_info', {}).get('access_token', 'UNKNOWN')

    print(f'''
    -----------GENERATED-----------
    EMAIL : {email}
    ID : {user_id}
    PASSWORD : {password}
    NAME : {first_name} {last_name}
    BIRTHDAY : {birthday} 
    GENDER : {gender}
    -----------GENERATED-----------
    Token : {token}
    -----------GENERATED-----------
    ''')

# Fungsi untuk memanggil API dengan error handling
def _call(url, params, proxy=None, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBLC/en_US;]'}
    try:
        response = requests.post(url, data=params, headers=headers, proxies=proxy, timeout=5) if post else requests.get(url, params=params, headers=headers, proxies=proxy, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f'[×] Error dalam API call: {e}')
    return {}

# Fungsi untuk memeriksa proxy yang valid
def test_proxy(proxy, q, valid_proxies):
    if test_proxy_helper(proxy):
        valid_proxies.append(proxy)
    q.task_done()

# Fungsi helper untuk menguji proxy
def test_proxy_helper(proxy):
    try:
        response = requests.get('https://api.mail.tm', proxies=proxy, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Fungsi untuk memuat proxy dari file
def load_proxies():
    try:
        with open('proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file]
        return [{'http': f'http://{proxy}'} for proxy in proxies]
    except FileNotFoundError:
        logging.error('[×] File proxies.txt tidak ditemukan!')
    return []

# Fungsi untuk mendapatkan proxy yang bekerja
def get_working_proxies():
    proxies = load_proxies()
    valid_proxies = []
    q = Queue()
    
    for proxy in proxies:
        q.put(proxy)
    
    threads = []
    for _ in range(min(10, len(proxies))):  # Maksimum 10 thread
        worker = threading.Thread(target=worker_test_proxy, args=(q, valid_proxies))
        worker.daemon = True
        worker.start()
        threads.append(worker)
    
    q.join()

    for _ in range(len(threads)):
        q.put(None)
    
    for thread in threads:
        thread.join()
    
    return valid_proxies

# Fungsi worker untuk menguji proxy
def worker_test_proxy(q, valid_proxies):
    while True:
        proxy = q.get()
        if proxy is None:
            break
        test_proxy(proxy, q, valid_proxies)

# Menjalankan program utama
working_proxies = get_working_proxies()

if not working_proxies:
    logging.error('[×] Tidak ada proxy yang valid. Cek kembali proxy Anda.')
else:
    num_accounts = int(input('[+] Berapa akun yang ingin dibuat? '))
    for _ in range(num_accounts):
        proxy = random.choice(working_proxies)
        email, password, first_name, last_name, birthday = create_mail_tm_account(proxy)
        if all([email, password, first_name, last_name, birthday]):
            register_facebook_account(email, password, first_name, last_name, birthday, proxy)

print('\x1b[38;5;208m⇼' * 60)
