import requests,re,json,os,time
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
P2 = "[#FFFFFF]" # PUTIH

ses = requests.Session()

def clear():
    os.system('clear')
    
def menu():
    prints(Panel.fit(f"1. [bold green]Dump Instagram No Login \n[white1]2. [bold green] exit"))
    i = input(f"+_ Masukan Pilihan : ")
    if i == "1":
        dump_insta_nologin()
    elif i == "2":
        exit()
    else:
        prints(Panel.fit(f"[bold red]Pilihan Tidak Ada"))
        time.sleep(2)
        menu()
        
