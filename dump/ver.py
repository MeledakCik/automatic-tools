from urllib.parse import quote
import re, os, random, urllib, urllib.request, time, requests,datetime
import requests,json,os,random,datetime,time,re
from bs4 import BeautifulSoup as bsp
from rich.console import Console
from rich.panel import Panel 
from rich import print as prints
import threading
from rich.console import Console as sol
import time
from rich.table import Table as me
import datetime
from string import *
xyz=[]
# Define color codes for output styling
B = '\x1b[1;94m'  # BLUE
U = '\x1b[1;95m'  # PURPLE
O = '\x1b[1;96m'  # LIGHT BLUE
N = '\x1b[0m'     # RESET
H = "\033[0;92m"   # GREEN
K = "\033[0;93m"   # YELLOW
M = '\x1b[1;91m'   # RED
P = "\033[0m"      # WHITE
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K
P = '\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
H = '\x1b[1;92m' # HIJAU +
h = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
B = '\x1b[1;94m'

ses = requests.Session()
X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
IG_URL = 'z.p42.www.instagram.com'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': X_IG_APP_ID,'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
xx = 0
rr = random.randint;rc = random.choice
console = Console()
Uid, Uuid , Uuid4= [], [], []
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}


def Aset_Ig():
    os.system('clear')
    if os.path.isfile('.Cokies-IG.txt') is True:
        coki = {'cookie': open('.Cokies-IG.txt', 'r').read()}
    else:
        prints(Panel.fit(f"[bold white]Silahkan Masukan Cookies Akun Instagram Pastikan Menggunakan Akun Tumbal!",style="bold blue"))
        raraky = {'cookie':input("\n└──╭➣ cookie: ")}
        if raraky['cookie'] == 'res':
            coki = {'cookie':find_res()}
        else:
            coki = raraky
    try:
        uid = re.search(r'ds_user_id=(\d+)', str(coki['cookie'])).group(1)
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()
        if 'user' in req:
            req = req['user']
            open('.Cokies-IG.txt', 'w').write(f'{coki["cookie"]}')
            full_name = req['full_name']
            username = req['username']
            follower_count = req['follower_count']
            following_count = req['following_count']
            media_count = req['media_count']
            return coki, full_name, username, follower_count, following_count, media_count
        else:
            os.system('rm -rf .Cokies-IG.txt')
            prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
            time.sleep(3)
            return None, None, None, None, None, None  
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
        time.sleep(3)
        return None, None, None, None, None, None 


def menu():
    os.system('clear')
    aset, full_name, username, fol, following, media = Aset_Ig()
    if aset is None:
        time.sleep(3)
        return
    os.system('clear')
    tabel1 = f"[bold white]01\n02"
    tabel2 = (
        f"[bold white]Crack Dari Pengikut\nCrack Dari Mengikuti"
    )
    tabel3 = f"[bold white]ON\nON"
    colume_tabel = me()
    colume_tabel.add_column("NO", style="bold green", justify='center')
    colume_tabel.add_column("PILIHAN", style="bold green", justify='center', width=55)
    colume_tabel.add_column("STATUS", style="bold green", justify='center')
    colume_tabel.add_row(tabel1, tabel2, tabel3)
    sol().print(colume_tabel, justify='start', style="bold blue")
    x = input('└──╭➣ Pilih 1 Sampai 2: ')
    if x in ['01','1']:
        dumps(aset, True)
    elif x in ['02','2']:
        dumps(aset, False)


def dumps(kuki, typess, xyz=[]):
    if 'csrftoken' not in str(kuki):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
            token = memek['config']['csrf_token']
            kuki['cookie'] += ';csrftoken=%s;' % (token)
        except:
            os.system('rm -rf .Cokies-IG.txt')
            exit()

    prints(Panel.fit(f"[bold white] Masukan Target Username Anda", style='bold blue'))      
    
    while True:
        users = input(f'└──╭➣ Targets User : ').split(',')
        prints(f" \n[bold white]└──╭➣ Process Collecting Username.....")         

        threads = []
        for y in users:
            thread = threading.Thread(target=process_user, args=(y, kuki, typess, xyz))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        print("")
        if os.path.exists('dump.txt'):
            with open('dump.txt', 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines[:4]):
                    username = line.split('|')[0].strip()
                    prints(f"[bold white]{i+1}. {username}") 
        print("\nKamu telah beres dump")
        ulang = input("Apakah ingin dump lagi? (y/n): ").strip().lower()
        if ulang != 'y':
            print("Terima kasih! Program selesai.")
            break


def process_user(user, kuki, typess, xyz):
	req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
	match = re.search(r'"user_id":"(\d+)"', str(req))
	if match:
		uid = match.group(1)
		if uid not in xyz:
			xyz.append(uid)
		mode = 'followers' if typess is True else 'following'
		Graphql(typess, uid, kuki['cookie'], '')

def Graphql(typess, userid, cokie, after):
    global xx, Uuid
    api = "https://www.instagram.com/graphql/query/"
    csr = 'variables={"id":"%s","first":24,"after":"%s"}' % (userid, after)
    mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
    
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cookie": cokie
        }
        req = requests.get(api, params=mek, headers=ptk).json()
        
        if 'require_login' in req:
            if len(Uuid) > 0:
                pass
            else:
                exit('\n[!] Invalid Cookie')

        khm = 'edge_followed_by' if typess is True else 'edge_follow'
        
        with open('dump.txt', 'a') as file:  # Mode 'a' untuk append
            for xyz in req['data']['user'][khm]['edges']:
                xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
                if xy not in Uuid:
                    xx += 1
                    Uuid.append(xy)
                    print(f'\r└──╭➣ Mendapatkan ID {len(Uuid)}', end='')
                    time.sleep(0.0009)
                    file.write(xy + '\n')  # Menulis data baru tanpa menghapus yang lama

        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    menu()
    
    