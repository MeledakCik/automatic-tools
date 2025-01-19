import requests,bs4,sys,os,datetime,re,time,json,random,concurrent
from rich.console import Console
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel
from bs4 import BeautifulSoup as bs
from datetime import datetime
from rich.panel import Panel as nel
from concurrent.futures import ThreadPoolExecutor
from rich.table import Table as me

console = Console()


M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
P2 = "[#FFFFFF]" # PUTIH
ses = requests.Session()

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
headers1 = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
    
def pilihan():
    os.system('clear') 
    print("") 
    cetak(f"{M2}[ ──────────── [  {P2}{H2}Menu Pilihan{P2}  {M2}] ──────────── ]{P2}") 
    print("") 
    prints(f"{P2}1. Info Username Instagram \t\t\t[ {H2}Aman{P2} ]\n2. Feed Username Instagram \t\t\t[ {H2}Aman{P2} ]\n3. Info Shared Instagram \t\t\t[ {H2}Aman{P2} ]\n")
    cetak(f"{M2}[ ──────────── [  {P2}{H2}Menu Instagram Info{P2}  {M2}] ──────────── ]{P2}") 
    print("") 
    su = input(f"└──╭➣ Pilihan 1 Sampai 4 : ") 
    if su in ["1"]:
        print("") 
        name = input('└──╭➣  Masukkan username : ')
        data_target(name)
    elif su in ["2"]:
        print("") 
        name = input('└──╭➣  Masukkan username : ')
        data_info(name)
    elif su in ["3"]:
        print("") 
        shared_data()
    else:
        exit()
        
        
def data_target(name):
    for y in name.split(','):
        y = y.strip()  # Hilangkan spasi ekstra
        try:
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)',
                'x-ig-app-id': '1217981644879628'
            }
            # Ambil informasi profil
            profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers=HEADERS).json()['data']['user']

            # Ekstrak data yang dibutuhkan
            post = profil_info_target.get("edge_owner_to_timeline_media", {}).get("count", 0)
            userId = profil_info_target.get("id", None)
            peng = profil_info_target.get("edge_followed_by", {}).get("count", 0)
            meng = profil_info_target.get("edge_follow", {}).get("count", 0)
            mail = profil_info_target.get("business_email", "Tidak tersedia")
            phone = profil_info_target.get("business_phone_number", "Tidak tersedia")
            fullname = profil_info_target.get("full_name", "Tidak tersedia")
            fbid = profil_info_target.get("fbid", "Tidak tersedia")

            # Cetak hasil
            print(f"  Username: {y}")
            print(f"  Jumlah Postingan: {post}")
            print(f"  User ID: {userId}")
            print(f"  Jumlah Pengikut: {peng}")
            print(f"  Jumlah Mengikuti: {meng}")
            print(f"  Email Bisnis: {mail}")
            print(f"  Nomor Telepon Bisnis: {phone}")
            print(f"  Nama Lengkap: {fullname}")
            print(f"  FBID: {fbid}")

        except Exception as e:
            print(f"Terjadi kesalahan saat memproses username {y}: {e}")
            


def data_info(name):
    for y in name.split(','):
        y = y.strip()  # Hilangkan spasi ekstra
        try:
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)',
            }
            # Ambil informasi profil
            response = requests.get(f'https://i.instagram.com/api/v1/feed/user/{y}/username/', headers=HEADERS)

            if response.status_code == 200:
                profil_info_target = response.json()
                
                # Ambil data yang diperlukan
                user_data = profil_info_target.get('user', {})
                if user_data:
                    data = {
                        'username': user_data.get('username', 'Tidak ditemukan'),
                        'full_name': user_data.get('full_name', 'Tidak ditemukan'),
                        'profile_pic_url': user_data.get('profile_pic_url', 'Tidak ditemukan'),
                        'is_private': user_data.get('is_private', False),
                        'is_verified': user_data.get('is_verified', False),
                        'fbid_v2': user_data.get('fbid_v2', 'Tidak ditemukan'),
                        'match' : re.findall(r'"id":"(\d+)"', response.text)
                        
                    }
                    print(f"  Username      : {data['username']}")
                    print(f"  Full Name     : {data['full_name']}")
                    print(f"  Profile Pic   : {data['profile_pic_url']}")
                    print(f"  Private       : {'Yes' if data['is_private'] else 'No'}")
                    print(f"  Verified      : {'Yes' if data['is_verified'] else 'No'}")
                    print(f"  Facebook ID V2   : {data['fbid_v2']}")
                    print(f"  Media ID    : {data['match']}")
                else:
                    print(f"Data pengguna tidak ditemukan untuk username {y}")
            else:
                print(f"Gagal mengambil data untuk username {y}. Status Code: {response.status_code}")
                print(f"Pesan Error: {response.text}")
                print("-" * 50)

        except Exception as e:
            print(f"Terjadi kesalahan saat memproses username {y}: {e}")
            print("-" * 50)

def shared_data():
    try:
        HEADERS = headers1
        response = requests.get(f'https://i.instagram.com/api/v1/web/data/shared_data/', headers=HEADERS)
        res = response.json()
        print(res['config'])
    except Exception as e:
        print(f"Terjadi kesalahan saat memproses username : {e}")
        print("-" * 50)
        

if __name__=='__main__':
    pilihan()