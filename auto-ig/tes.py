import random,re,time,json,bs4
import requests
from bs4 import BeautifulSoup as bsp

xyz=[]
Uuid=[]
# Define color codes for output styling
B = '\x1b[1;94m'  # BLUE
U = '\x1b[1;95m'  # PURPLE
O = '\x1b[1;96m'  # LIGHT BLUE
N = '\x1b[0m'     # RESET
H = "\033[0;92m"   # GREEN
K = "\033[0;93m"   # YELLOW
M = '\x1b[1;91m'   # RED
P = "\033[0m"      # WHITE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
}
ses = requests.Session()

def generate_random_ua():
    devices = ['Android', 'iPhone', 'Windows']
    os_version = random.choice(['10', '11', '12'])
    device_type = random.choice(devices)
    browser_version = random.randint(40, 100)
    ua = f"Mozilla/5.0 ({device_type}; {os_version} OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version}.0.0.0 Mobile Safari/537.36"
    return ua

def login_to_instagram(username, password):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    response = ses.get('https://www.instagram.com/accounts/login/', headers=headers)
    csrf_token = response.cookies.get('csrftoken')
    if csrf_token:
        print(f"{B}CSRF Token: {H}{csrf_token}{N}")
    else:
        print(f"{M}CSRF Token not found!{N}")
        return

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
        if 'csrftoken' not in str(cookie):
            try:
                memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cookie).json()
                token = memek['config']['csrf_token']
                cookie['cookie'] +=';csrftoken=%s;'%(token)
            except Exception as e:
                print(f'\n[bold white]Gagal dump Csrftoken tidak tersedia, dump akan berhenti : {e}')
                exit()
        usres = ses.get('https://www.instagram.com/push/web/get_push_info')
        yo = usres.json()['data']['user_id']
        print(f"{H}User ID Akun: {O}{yo}{N}")
        print(f"\n{H}Masukkan Username Instagram, Tekan CTRL+C Jika Ingin Berhenti Dump{P}")
        print('')
        name = input('└──╭➣  Masukkan username : ')
        jumlah = input('└──╭➣  Masukkan jumlah page ( max 60 ) : ')
        data_target(name,jumlah)
        print('')
        try:
            csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(yo,'')
            mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr)
            try:
                ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cookie}
                req = requests.get('https://www.instagram.com/graphql/query/', params=mek, headers=ptk).json()
                if 'require_login' in req:
                    if len(Uuid) > 0:
                        pass
                    else:
                        exit(f'\nInvalid Cookie')
                for xyz in req["data"]["user"]["edge_follow"]['edges']:
                    username = xyz['node']['username'] + '|' + xyz['node']['full_name']
                    if username not in Uuid:
                        Uuid.append(username)
                        print('\r └──╭➣ Mengumpulkan Uid [ {} ] '.format(len(Uuid)), end='')
                        time.sleep(0.0009)

            except Exception as e:
                print(f"{M}Error: {e}{N}")
        except Exception as e:
            print(f"{M}Error: {e}{N}")
    else:
        print(f"{M}Login failed! Please check your username or password.{N}")
        

        
def data_target(name,jumlah):
    for y in name.split(','):
        y = y.strip()  # Hilangkan spasi ekstra
        try:
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)',
                'x-ig-app-id': '1217981644879628'
            }
            profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers=HEADERS).json()['data']['user']
            userId = profil_info_target.get("id", None)
            print(f"User ID Target: {userId}")
            try:
                respo = ses.get(f"https://www.instagram.com/api/v1/friendships/{userId}/followers/?count={jumlah}&search_surface=follow_list_page",headers=HEADERS).json()['users']
                usernames = [entry['username'] for entry in respo if 'username' in entry]
                print(usernames)
            except Exception as e:
                print(f"Terjadi kesalahan saat memproses username {y}: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan saat memproses username {y}: {e}")
            

login_to_instagram("dliigx","meledakcik123#")
# Usernames : dikanrch_ 
# Passwords : Dika05 
