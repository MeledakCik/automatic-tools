import requests,os,re
import time
from rich.console import Console
from rich.panel import Panel 
from rich import print as prints
import threading

console = Console()
Uuid=[]
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}


def Login():
    prints(Panel.fit(f"[bold white]Masukan Cookies Instagram",style="bold blue"))
    coki = input("\n└──╭➣ Masukan cookie: ")
    try:
        uid = re.search(r'ds_user_id=(\d+)', str(coki).group(1))
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()
        if 'user' in req:
            req = req['user']
            open('.Cokies-IG.txt', 'w').write(f'{coki}')
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
            exit()
            return None, None, None, None, None, None  
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
        time.sleep(3)
        exit()
        return None, None, None, None, None, None 


def Menu():
    try:
        cok = open('.Cokies-IG.txt', 'r').read()
    except FileNotFoundError:
        prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
        time.sleep(3)
        Login()
    prints(Panel.fit(f"[bold white]1. Dump Pengikut \n2. Dump Mengikuti",style="bold green"))
    pilih = input('+_ Pilih Menu : ')
    if pilih =='1':
        dumps(cok, True)
    elif pilih == '2':
        dumps(cok, False)
    else:
        prints(Panel.fit(f"Pilih yang bener bro"))

def dumps(kuki, typess, xyz=[]):
    if 'csrftoken' not in str(kuki):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
            token = memek['config']['csrf_token']
            kuki['cookie'] += f';csrftoken={token};'
        except:
            os.system('rm -rf .Cokies-IG.txt')
            exit()
    print(Panel.fit(f"[bold white] Masukan Target Username Anda", style='bold blue'))
    users = input(f'└──╭➣ Targets User : ').split(',')
    print(f"\n[bold white]└──╭➣ Process Collecting Username.....")
    threads = []
    for y in users:
        thread = threading.Thread(target=process_user, args=(y, kuki, typess, xyz))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("")
    prints(Panel.fit(f"[bold green]Total Akun Terkumpul : {len(Uuid)}", style="bold green"))

def process_user(user, kuki, typess, xyz):
    req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
    match = re.search(r'"user_id":"(\d+)"', str(req))
    if match:
        uid = match.group(1)
        if uid not in xyz:
            xyz.append(uid)
        mode = 'followers' if typess is True else 'following'
        Graphql(typess, uid, kuki['cookie'], '', xyz)

def Graphql(typess, userid, cokie, after, xyz):
    global xx
    api = "https://www.instagram.com/graphql/query/"
    csr = f'variables={{"id":"{userid}","first":24,"after":"{after}"}}'
    mek = f"query_hash=58712303d941c6855d4e888c5f0cd22f&{csr}" if typess is False else f"query_hash=37479f2b8209594dde7facb0d904896a&{csr}"
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cookie": cokie,
        }
        req = requests.get(api, params=mek, headers=ptk).json()
        if 'require_login' in req:
            exit('\n Invalid Cookie')
        khm = 'edge_followed_by' if typess is True else 'edge_follow'
        for node in req['data']['user'][khm]['edges']:
            username = node['node']['username']
            xy = username + '|' + node['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print(f'\r└──╭➣ Mendapatkan ID {len(Uuid)}', end='')
                process_user(username, {"cookie": cokie}, typess, xyz)
        if req['data']['user'][khm]['page_info']['has_next_page']:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after, xyz)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    Menu()