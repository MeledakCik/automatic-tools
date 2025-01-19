import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,json,os,sys,random,datetime,time,re
from bs4 import BeautifulSoup as bsp
from rich.console import Console
from rich.panel import Panel 
from rich import print as prints
import threading
from rich.console import Console as sol
import time
from rich.table import Table as me
import datetime
from rich.columns import Columns
from rich.progress import Progress,TextColumn,SpinnerColumn
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
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3

#------------------[ COLOR TABLE FOR RICH ]-------------------#
LIGHT = "#875f5f" # LIGHT
GOLD    = "#ffd700" # GOLD
MEDIUM  = "#875fd7" # MEDIUM GREEN
PINK    = "#FF00FF" # PINK
WHITE  = "#FFFFFF" # WHITE
SKY     = "#87afff" # SKY BLUE
ORNG   = "#d78700" # ORANGE3
ORCH   = "#ff5fff" # MEDIUM ORCH

ses = requests.Session()
X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
IG_API = 'https://i.instagram.com/api/v1/'
IG_URL = 'z.p42.www.instagram.com'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': X_IG_APP_ID,'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
headers_log = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
}

xx = 0
rr = random.randint;rc = random.choice
console = Console()
Uid, Uuid , Uuid4= [], [], []
Ok, Cp, Loop = 0, 0, 0
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:asal_kota = cek_data["city"]
except:asal_kota = {'-'}
try:asal_reg = cek_data["region"]
except:asal_reg = cek_data['-']
try:times = cek_data["timezone"]
except:times = cek_data['-']
try:city = cek_data["city"]
except:city = cek_data['-']

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
Okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
Cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def generate_random_ua():
    devices = ['Android', 'iPhone', 'Windows']
    os_version = random.choice(['10', '11', '12'])
    device_type = random.choice(devices)
    browser_version = random.randint(40, 100)
    ua = f"Mozilla/5.0 ({device_type}; {os_version} OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version}.0.0.0 Mobile Safari/537.36"
    return ua

def InstaIgeh():
    rr = random.randint
    rc = random.choice
    UA1 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9,14))}_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 Instagram 31.0.0.14.97 (iPhone9,1; iOS {str(rr(9,14))}_2_5; en_US; en-US; scale=2.00; gamut=wide; {str(rr(700,799))}x{str(rr(1300,1500))})"
    UA2 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; SAMSUNG.{str(rr(111111,211111))}.SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/{str(rr(73,150))}.92.0.4515.166.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36"
    UA3 = f"Mozilla/5.0 (Linux; Android 7.0; LGT32 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Safari/537.36 Instagram 258.1.0.26.100 Android (24/7.0; {str(rr(200,240))}dpi; {str(rr(1100,1200))}x{str(rr(1800,1900))}; LGE/KDDI; LGT32; b5; b5; ja_JP; 412452718)"
    uacrack6 = f"Mozilla/5.0 (Linux; Android 8.0.0; ONEPLUS A5000 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.65.0.3325.109.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (26/8.0.0;{str(rr(200,240))}480dpi; {str(rr(1100,1200))}1080x1920{str(rr(1800,1900))}; OnePlus; ONEPLUS A5000; OnePlus5; qcom; ru_UA; 98288242)"
    UA7 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX1851 Build/RKQ1..{str(rr(111111,211111))}.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.95.0.4638.74.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]"
    UA5 = f"Mozilla/5.0 (Linux; Android 10; Infinix X682B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.88.0.4324.93.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 172.0.0.21.123 Android (29/10;  {str(rr(200,240))}320dpi; {str(rr(1100,1200))}720x1464{str(rr(1800,1900))} ; INFINIX MOBILITY LIMITED/Infinix; Infinix X682B; Infinix-X682B; mt6769; tr_TR; 269790803)"
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UaMainn = random.choice([UA1, UA2, UA3,uacrack6,UA7,UA5,satu,dua,tiga,empat,lima])
    return UaMainn

def aguss():
    rr = random.randint
    rc = random.choice
    fbcr = str(
        random.choice([
            'TELKOMSEL', 'AXIS', 'Indosat', 'XL', '3SinyalKuatHemat',
            'Tsel-PakaiMasker', 'XL Axiata'
        ]))
    androversi = random.choice(["15_4", "14_3", "13_5", "14_5", "13_4"])
    build = ['MRA58K', 'UCC50Z', 'QKQ1.200127.002']
    andro = ['k', 'a', 'b', 'x', 'y', 'z', 'd', 'l']
    browser = ['HeyTapBrowser', 'MZBrowser']
    asep1 = random.choice(["Y6MLQN", "8G7LN3", "2783VM", "X35XFL", "W5T30Y"])
    asep4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {androversi} like Mac OS X) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{asep1} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
    asep5 = f"Mozilla/5.0 (Linux; Android {androversi} SM-N960N Build/QP1A.190711.020; wv) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/4.0 Chrome/{rr(10,99)}.0.{rr(1000,9999)}.{rr(73,150)} Whale/1.0.0.0 Crosswalk/25.80.14.20 Mobile Safari/537.36 NAVER(inapp; search; 598; 10.28.2)"
    asep10 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; itel A663L Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36"
    asep6 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; Infinix X6832 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/455.0.0.44.88;]"
    asep7 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; V1818CA Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 VivoBrowser/18.6.0.0"
    asep8 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; zh-tw; PCLM50 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 HeyTapBrowser/40.8.27.1"
    asep9 = f"Mozilla/5.0 (Linux; AndroId {str(rr(2,13))}; zh-CN; M2104K10AC Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} UCBrowser/16.3.8.1289 Mobile Safari/537.36"
    v1 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; meizu 17 Pro Build/{str(rc(build))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(73,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]"
    v2 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; meizu 17 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} Mobile Safari/537.36"
    v3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(2,13))}; zh-CN; MZ-meizu 17 Pro Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} MZBrowser/8.{str(rr(1,20))}.1 Mobile Safari/537.36"
    v4 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; {str(rc(andro))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(59,169))}.0.0.0 Mobile Safari/537.36"
    hir = f"Mozilla/5.0 (Linux; U; Android {str(rr(2,13))}; zh-CN MZ-MEIZU 18 Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(100,150))} {str(rc(browser))}/9.{str(rr(1,20))}.1 Mobile safari/537.36"
    ua_rmx = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; RMX{str(rr(1599,3999))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(89,120))}.0.{str(rr(3999,4999))}.{str(rr(55,129))} Mobile Safari/537.36"
    ua_oppo = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; CPH{str(rr(1999,4999))} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(59,159))}.0.{str(rr(2999,4999))}.{str(rr(55,159))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.48.122;]"
    ya = random.choice([hir, asep4,asep5, asep10, asep6, asep7, asep8, asep9, v1, v2, v3, v4,ua_rmx,ua_oppo])
    return ya

def login_to_instagram():
    os.system('clear')
    if os.path.isfile('.Cokies-IG.txt') is True:
        cookie = {'cookie': open('.Cokies-IG.txt', 'r').read()}
    else:
        username = input(" +_ Masukan Username :")
        password = input(" +_ Masukan Password :")
        url = 'https://www.instagram.com/accounts/login/ajax/'
        response = ses.get('https://www.instagram.com/accounts/login/', headers=headers_log)
        csrf_token = response.cookies.get('csrftoken')
        login_headers = {
            'User-Agent': generate_random_ua(),
            'X-CSRFToken': csrf_token,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.instagram.com/accounts/login/',
        }

        data = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1605155817:{password}',  # Format the password with timestamp
        }
        login_response = ses.post(url, headers=login_headers, data=data, cookies={'csrftoken': csrf_token})
        if login_response.status_code == 200 and 'authenticated' in login_response.json() and login_response.json()['authenticated']:
            x = ses.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s" % username, headers={"user-agent": generate_random_ua(), "x-ig-app-id": '936619743392459'})
            usres = ses.get('https://www.instagram.com/push/web/get_push_info').json()['data']['user_id']
            x_json = x.json()["data"]["user"]
            pengikut = x_json["edge_followed_by"]["count"]
            mengikut = x_json["edge_follow"]["count"]
            postingan = x_json["edge_owner_to_timeline_media"]["count"]
            cookie = ";".join([key + "=" + value.replace('"', '') for key, value in ses.cookies.get_dict().items()])
            print(f"\n{B}{username} {password}{N}")
            print(f"{H}Followers: {O}{pengikut}{N}")
            print(f"{H}Posts: {O}{postingan}{N}")
            print(f"{H}Following: {O}{mengikut}{N}")
            print(f"{B}Cookies:{N}\n{P}{cookie}{N}")
            print(f"{H}Login successful!{N}")
            print(f"{H}User ID Akun: {O}{usres}{N}")
            time.sleep(2)
        else:
            prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"bold green"));os.system('rm -rf .kukis.txt');exit()
            return False
    try:
        uid = re.search(r'ds_user_id=(\d+)', str(cookie)).group(1)
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=cookie).json()
        if 'user' in req:
            req = req['user']
            open('.Cokies-IG.txt', 'w').write(f'{cookie}')
            full_name = req['full_name']
            username = req['username']
            follower_count = req['follower_count']
            following_count = req['following_count']
            media_count = req['media_count']
            return cookie, full_name, username, follower_count, following_count, media_count
        else:
            os.system('rm -rf .Cokies-IG.txt')
            print(f" {M}cookies Invalid Gunakan Cookies yang Lain!")
            time.sleep(3)
            return None, None, None, None, None, None  
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        print(f" {M}cookies Invalid Gunakan Cookies yang Lain!")
        time.sleep(3)
        return None, None, None, None, None, None 
        

    
def menu():
    os.system('clear')
    aset = login_to_instagram()
    os.system('clear')
    tabel1 = "01\n02\n00"
    tabel2 = (
        "Dump Pengikut\nDump Mengikuti\nGanti Cookie"
    )
    tabel3 = "ON\nON\nON"
    colume_tabel = me()
    colume_tabel.add_column("NO", style="bold green", justify='center')
    colume_tabel.add_column("PILIHAN", style="bold green", justify='center', width=55)
    colume_tabel.add_column("STATUS", style="bold green", justify='center')
    colume_tabel.add_row(tabel1, tabel2, tabel3)
    sol().print(colume_tabel, justify='start', style="bold green")
    x = input('└──╭➣ Pilih 1 Sampai 3: ')
    if x in ['01','1']:
        dumps(aset, True)
    elif x in ['02','2']:
        dumps(aset, False)
    elif x in ['00','0']:
        os.system('rm -rf .Cokies-IG.txt')
        print("berhasil menghapus cookies")
        exit()

def dumps(kuki, typess, xyz=[]):
    if 'csrftoken' not in str(kuki):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
            token = memek['config']['csrf_token']
            kuki['cookie'] += ';csrftoken=%s;' % (token)
        except:
            os.system('rm -rf .Cokies-IG.txt')
            exit()
    print(f" \nYour Targets Usernames")         
    users = input(f'Targets User [ bisa banyak ]: {b}').split(',')
    namefile = input('Masukan Nama File [ txt ] : ')
    print(f"\nProcess Collecting Username")         
    threads = []
    for y in users:
        thread = threading.Thread(target=process_user, args=(y, namefile,kuki, typess, xyz))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("")
    Metode(namefile)

def process_user(user, namefile,kuki, typess, xyz):
    global xx
    req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
    match = re.search(r'"user_id":"(\d+)"', str(req))
    if match:
        uid = match.group(1)
        if uid not in xyz:
            xyz.append(uid)
        mode = 'followers' if typess is True else 'following'
        after = ''
        api = "https://www.instagram.com/graphql/query/"
        csr = 'variables={"id":"%s","first":24,"after":"%s"}' % (uid, after)
        mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
        try:
            ptk = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "cookie": kuki
            }
            req = requests.get(api, params=mek, headers=ptk).json()
            if 'require_login' in req:
                if len(Uuid) > 0:
                    pass
                else:
                    exit(f'\n{B}[{b}●{B}]{M} Invalid Cookie')
            khm = 'edge_followed_by' if typess is True else 'edge_follow'
            for xyz in req['data']['user'][khm]['edges']:
                xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
                if xy not in Uuid:
                    xx += 1
                    Uuid.append(xy)
                    print(f'\r Collected ID : {b}{len(Uuid)}', end='')
                    open(namefile, 'w').write('\n'.join(Uuid))
            end = req['data']['user'][khm]['page_info']['has_next_page']
            if end is True:
                after = req['data']['user'][khm]['page_info']['end_cursor']
                process_user(typess, uid, kuki, after)
        except:
            pass
def Metode(namefile): 
    print(f"Kamu berhasi Dump username {len(Uuid)} dan tersimpan di {namefile}")
    exit()