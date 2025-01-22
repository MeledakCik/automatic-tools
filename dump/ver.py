import requests,os,re
import time
from rich.console import Console
from rich.panel import Panel 
from rich import print as prints
import threading

console = Console()
Uuid=[]
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
IG_API = 'https://i.instagram.com/api/v1/'
HEADERS = {
    'Host': 'www.instagram.com',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '129477',
    'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5',
}

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
            exit()
            return None, None, None, None, None, None  
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        prints(Panel.fit(f"[bold white]cookies Invalid Gunakan Cookies yang Lain!",style="bold red"))
        time.sleep(3)
        exit()
        return None, None, None, None, None, None 

def dumps(kuki, typess, xyz=[]):
	if 'csrftoken' not in str(kuki):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
			token = memek['config']['csrf_token']
			kuki['cookie'] += ';csrftoken=%s;' % (token)
		except:
			os.system('rm -rf .Cokies-IG.txt')
			exit()
	prints(Panel.fit(f"[bold white] Masukan Target Username Anda",style='bold blue'))      
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

def process_user(user, kuki, typess, xyz):
	req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
	match = re.search(r'"user_id":"(\d+)"', str(req))
	if match:
		uid = match.group(1)
		if uid not in xyz:
			xyz.append(uid)
		mode = 'followers' if typess is True else 'following'
		Graphql(typess, uid, kuki['cookie'], '')

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
                exit(f'\n Invalid Cookie')
        khm = 'edge_followed_by' if typess is True else 'edge_follow'
        for xyz in req['data']['user'][khm]['edges']:
            username = xyz['node']['username']
            xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print('\r└──╭➣ Mendapatkan ID {}'.format(len(Uuid)), end='')
                time.sleep(0.0009)
        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end is True:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)
        else:
            req = requests.get(f'https://www.instagram.com/{username}/', cookies=cokie).text
            match = re.search(r'"user_id":"(\d+)"', str(req))
            if match:
                uid = match.group(1)
                if uid not in xyz:
                    xyz.append(uid)
                mode = 'followers' if typess is True else 'following'
                Graphql(typess, uid, cokie['cookie'], '')
    except:pass

if __name__ == "__main__":
    aset = Aset_Ig()
    pilih = input('+_ Pilih dump mengikuti/pengikut [m/p] : ')
    if pilih.lower() =='m':
        dumps(aset, False)
    elif pilih.lower() == 'p':
        dumps(aset, True)
    else:
        prints(Panel.fit(f"Pilih yang bener bro"))