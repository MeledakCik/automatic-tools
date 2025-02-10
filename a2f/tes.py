import re
import requests
import json
import os
import sys
import time
from bs4 import BeautifulSoup
from rich.panel import Panel
from rich import print as prints

ua = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) '
                  'AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 '
                  'Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'
}

def Aset_Ig():
    os.system('clear')
    if os.path.isfile('.Cokies-IG.txt') and os.path.getsize('.Cokies-IG.txt') > 0:
        with open('.Cokies-IG.txt', 'r') as file:
            coki = {'cookie': file.read().strip()}
    else:
        prints(Panel.fit("[bold white]Silahkan Masukkan Cookies Akun Instagram!", style="bold blue"))
        coki = {'cookie': input("\n└──╭➣ Cookie: ")}

    try:
        uid = re.search(r'ds_user_id=(\d+)', coki['cookie']).group(1)
        req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()
        if 'user' in req:
            with open('.Cokies-IG.txt', 'w') as file:
                file.write(coki["cookie"])
            user = req['user']
            return coki, user['full_name'], user['username'], user['follower_count'], user['following_count'], user['media_count']
        else:
            os.remove('.Cokies-IG.txt')
            prints(Panel.fit("[bold red]Cookies Invalid! Gunakan cookies lain!", style="bold red"))
            time.sleep(3)
            return None, None, None, None, None, None
    except Exception:
        os.remove('.Cokies-IG.txt')
        prints(Panel.fit("[bold red]Cookies Invalid! Gunakan cookies lain!", style="bold red"))
        time.sleep(3)
        return None, None, None, None, None, None

def get_csrf_token(cookies):
    return cookies.get('csrftoken', '') or cookies.get('sessionid', '')

def auto_komen(coki):
    prints(Panel.fit("[bold white]Masukkan link postingan atau reels (pisahkan dengan koma).", style="bold blue"))
    links = input('└──╭➣ Masukkan Link: ').split(',')
    comment = input('└──╭➣ Masukkan Komentar: ')
    media_ids = []
    session = requests.Session()

    for link in links:
        try:
            response = session.get(link.strip(), cookies=coki, headers=ua)
            if response.status_code != 200:
                prints(f"[bold red]Gagal mengambil data dari: {link}")
                continue
            media_id_match = re.search(r'"media_id":"(\d+)"', response.text)
            if media_id_match:
                media_ids.append(media_id_match.group(1))
            else:
                prints(f"[bold red]Media ID tidak ditemukan untuk link: {link}")
        except Exception as e:
            prints(f"[bold red]Error: {e}")

    for media_id in media_ids:
        start_coment(session, coki, media_id, comment)

def start_coment(session, coki, media_id, comment):
    if 'csrftoken' not in str(coki):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=kuki).json()
            token = memek['config']['csrf_token']
            coki['cookie'] += ';csrftoken=%s;' %s (token)
        except:
            os.system('rm -rf .Cokies-IG.txt')
            exit()
    try:
        url = f"https://i.instagram.com/api/v1/web/comments/{media_id}/add/"
        payload = {"comment_text": comment}
        response = session.post(url, cookies=coki, headers=headers, data=payload)
        print(response.text)
        if response.status_code == 200:
            prints(f"[bold green]Berhasil komentar di media ID: {media_id}")
            exit()
        else:
            prints(f"[bold red]Gagal komentar di media ID: {media_id} - Status: {response.status_code} - Pesan: {response.text}")
            exit()
    
    except Exception as e:
        prints(f"[bold red]Error saat komentar: {e}")

def menu():
    os.system('clear')
    aset, full_name, username, followers, following, media = Aset_Ig()
    if aset is None:
        time.sleep(3)
        return
    while True:
        os.system('clear')
        prints(Panel.fit("[bold white]Instagram Bot - Auto Komen", style="bold blue"))
        prints(f"[bold white]Akun: {full_name} (@{username})")
        prints("[1] Auto Komen")
        prints("[2] Keluar")
        pilihan = input("└──╭➣ Pilih menu: ")

        if pilihan == "1":
            auto_komen(aset)
            exit()
        elif pilihan == "2":
            prints("[bold red]Keluar dari program.")
            sys.exit()
        else:
            prints("[bold red]Pilihan tidak valid.")
            time.sleep(2)

if __name__ == '__main__':
    menu()
