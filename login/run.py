import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess

ses = requests.Session()

from rich.panel import Panel 
from rich import print as prints

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

headers_log = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def generate_random_ua():
    devices = ['Android', 'iPhone', 'Windows']
    os_version = random.choice(['10', '11', '12'])
    device_type = random.choice(devices)
    browser_version = random.randint(40, 100)
    ua = f"Mozilla/5.0 ({device_type}; {os_version} OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version}.0.0.0 Mobile Safari/537.36"
    return ua


def Login():
    username = input(f'└──╭➣ {H}Masukan Username :{H} ')
    password = input(f'└──╭➣ {H}Masukan Password :{H} ')
    url = 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Foidc%2F%3Fapp_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignupviafb%252F%26response_type%3Dcode%26scope%3Dopenid%2Bemail%2Bprofile%2Blinking%26state%3DATBsvZdpIa4cg4v1QzOlMGb9B1GsGFMSd3gGjdhOY8VbVr18SuQ1P7aqrXN9_wwFD6QPmlsIHcC-f9L2SU39myyphzqIltgFOsRXrTpZHT7CR8Ep1dKdU9ZcoeO-ETgxMLMxQAssLDrLhaK6jZjYEwW0OFfRNT5z4mpHoVd2LSMyVDLUA2Ytcson-29F4eu6IOezoBZVOTgRuRd4AS3xIH-CMWr2yZ2hYnarG4N4LWSH5CVFPS5C0K8gnENwF4nq02rE'
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