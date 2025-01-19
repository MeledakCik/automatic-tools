Author    = 'Cik kawan'
Facebook  = None
Instagram = 'kkngksyf_'
Whatsapp  = '081322544391'

P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu

import os, sys, time, re, datetime, random
from datetime import datetime
import requests
import bs4
from bs4 import BeautifulSoup as bs

ses = requests.Session()

def random_ua_vivo():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

auth1 = 'Cik kawan'
auth2 = 'Kakangkasyaf'
reco = 'Gausa Direcode Bos, Tinggal Pake Aja'
rede = 'Dibilangin Gausa Direcode'
key = len(auth1)*len(auth2)-len(auth1)
headers_get = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : random_ua_vivo()}
perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'
head_email = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'}
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
ok = 0
cp = 0
boys_name = ['Axel Lateef Noah','Anzel Qasim Wisthara','Basheer Malik Yazdan','Bernardus Clementine Christian','Carel Vasco Zachariah','Cyrus Osmanth Elkanah','Damian Vasyl Isaac','Dominic Valdi Xander','Ephraim Benedict Gevariel','El Fatih Ghazwan','Fawwaz Rafisqy Ezaz','Faheem Fakhri Isyraq','Gianluca Nathanael Nadav','Haddad Ammar Ar-Rayyan','Istafa Tabriz Qiwam','Kenneth Krisantus Lazarus','Nathanael Alfred William','Vaskylo Yeremia Clearesta','Xaferius Eliel Antonios','Yesaya Nathanael Liam']
girls_name = ['Atika Fithriya Tsabita','Alya Kinana Juwairiyah','Adzkiya Naila Taleetha','Adiva Arsyila Savina','Aqeela Nabiha Sakhi','Bilqis Adzkiya Rana','Chayra Ainin Qulaibah','Caliana Fiona Syafazea','Chaerunnisa Denia Athalla','Dhawiyah Nisrin Naziha','Dilara Adina Yuani','Farah Sachnaz Ashanty','Ghariyah Zharufa Abidah','Hamna Nafisa Raihana','Hanin Raihana Syahira','Izza Hilyah Nafisah','Kayla Zhara Qamela','Mahreen Shafana Almahyra','Rasahana Shafwa Ruqayah','Shakayla Aretha Shaima']
ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1970,2001))}
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s;'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))

def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

def jeda(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)
def tunggu_kode(t):
    for x in range(t+1):
        print('\r%sTunggu Kode %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)
        
def get_pass():
    up = 'ABCDEFGHIJKLMNOPQRSTUVWses'
    lw = up.lower()
    nb = '0123456789'
    ch = up + lw + nb
    pw = ''.join(random.choice(ch) for _ in range(12))
    return(pw.lower())

def hitung(a):
    for x in range(a+1):
        print('\r[%sOK:%s%s] [%sCP:%s%s] Tunggu %s Detik         '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
        a -= 1
        time.sleep(1)
def get_nope():
    na   = random.choice(['77','78','59'])
    ni   = str(random.randrange(1000,10000))
    nu   = str(random.randrange(10000,100000))
    nope = '08%s%s%s'%(na,ni,nu)
    return(nope)

def main_menu():
    print('%s[%s1%s] %sCreate Account'%(M,P,M,P))
    x = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).lower()
    print('')
    if   x in ['1','01','001','a']:
        menu_create()
    else: exit('%sIsi Yang Benar!%s'%(M,P))

def menu_create():
    firstname = input(' Masukan nama pertama : ')
    lastname = input(' Masukan nama terakhir : ')
    sex = input(' Masukan nomor sex [ 1 (female) | 2 (male)] : ')
    try :
        req = ses.get('https://10minutemail.net/m/?lang=id', headers=head_email, allow_redirects=True)
        req.raise_for_status()
        soup = bs(req.content, 'html.parser')
        ses_email = re.search(r'sessionid="(.*?)"', str(soup)).group(1)
        tim_email = str(time.time()).replace('.', '')[:13]
        dat = {'new': '1', 'sessionid': ses_email, '_': tim_email}
        email_response = ses.post(
            'https://10minutemail.net/address.api.php', 
            data=dat, headers=head_email, allow_redirects=True
        )
        email_response.raise_for_status()
        email_data = email_response.json()
        email = email_data['mail_get_mail']
        try:
            url = "https://m.facebook.com/reg/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM3MTcxMTczLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D"
            payload = {
                "jazoest": "2911",
                "lsd": "AVrEvFcYUD0",
                "firstname": firstname,  
                "lastname": lastname,   
                "birthday_day": ttl['tgl'],  
                "birthday_month": ttl['bln'],
                "birthday_year": ttl['thn'], 
                "sex": sex,                  
                "reg_email__": email, 
                "reg_email_confirmation__": email, 
                "reg_passwd__": get_pass(),
                "terms": "on",
                "referrer": "",
                "asked_to_login": "0",
                "use_custom_gender": "",
                "ns": "0",
                "ri": "2c41c5c0-8d62-4386-a9b8-e57dc5dc98a3",
                "action_dialog_shown": "",
                "invid": "",
                "a": "",
                "oi": "",
                "locale": "en_GB",
                "app_bundle": "",
                "app_data": "",
                "reg_data": "",
                "app_id": "",
                "fbpage_id": "",
                "reg_oid": "",
                "reg_instance": "O2cXZ8ScY2EJWVKTxnWzPbEi",
                "openid_token": "",
                "uo_ip": "",
                "guid": "",
                "key": "",
                "re": "",
                "mid": "",
                "fid": "",
                "reg_dropoff_id": "",
                "reg_dropoff_code": "",
                "ignore": "reg_email_confirmation__",
            }
            cok  = '; '.join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])
            cok += perangkat
            pos = bs(requests.post(url, data=payload, headers=headers_get, cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            if pos.status_code == 200:
                print('Nama   : %s'%(str(firstname + ' ' + lastname)))
                print('Pass   : %s'%(str(get_pass())))
                print('Email  : %s'%(str(email)))
                try :
                    time.sleep(60)
                    dat['new'] = '0'
                    mail_response = ses.post('https://10minutemail.net/address.api.php', data=dat, headers=head_email, allow_redirects=True)
                    mail_response.raise_for_status()
                    mail_data = mail_response.json()
                    if 'mail_list' in mail_data:
                        for mail in mail_data['mail_list']:
                            if "Facebook" in mail['from']:
                                kode = re.search(r'FB-(\d+)', mail['subject'])
                                if kode:
                                    print(f"Kode FB: {kode.group(1)}")
                                    return email, kode.group(1)
                    print("Kode FB tidak ditemukan.")
                except Exception as e:
                    print(str(e))
            else:
                print('gagal membuat akun')
                print('Nama   : %s'%(str(firstname + ' ' + lastname)))
                print('Pass   : %s'%(str(get_pass())))
                print('Email  : %s'%(str(email)))
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    menu_create()
    

# try:
#     url2 = 'https://www.facebook.com/confirm_code/dialog/submit/?next=https%3A%2F%2Fwww.facebook.com%2F%3Flsrc%3Dlbr&cp=wsm57719%40msssg.com&from_cliff=1&conf_surface=hard_cliff&event_location=cliff'
#     data = {
#     'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(url)).group(1),
#     'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(url)).group(1),
#     'source_verified'  : 'www_reg',
#     'code' : get_code_10minutemail(),
#     'confirm'  : 'submit'}
#     cok  = '; '.join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])
#     cok += perangkat
#     post = bs(ses.post(url2,data=data,headers=headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
#     if 'c_user' in post.cookies.get_dict().keys():
#         cookie = cvt('ok',ses.cookies.get_dict())
#         id = ses.cookies.get_dict()['c_user']
#         print('\r%sStatus : %sSuccess%s                         '%(P,H,P))
#         print('Nama   : %s'%(str(firstname + ' ' + lastname)))
#         print('ID     : %s'%(str(id)))
#         print('Pass   : %s'%(str(get_pass())))
#         print('Email  : %s'%(str(get_email_10minutemail())))
#         print('TTL    : %s %s %s'%(ttl['tgl'],bulan[ttl['bln']],ttl['thn']))
#         print('Cookie : %s\n'%(str(cookie)))
#     else:
#         print('\r%sStatus : %sGagal%s'%(P,M,P))
#         print('Nama   : %s'%(str(pos.name)))
#         print('ID     : %s'%(str(pos.id)))
#         print('Pass   : %s'%(str(get_pass())))
#         print('Email  : %s'%(str(get_email_10minutemail())))
#         print('TTL    : %s %s %s'%(ttl['tgl'],bulan[ttl['bln']],ttl['thn']))
#         print('Cookie : %s\n'%(str(cvt('ok',ses.cookies.get_dict()))))
# except Exception as e: print(str(e))