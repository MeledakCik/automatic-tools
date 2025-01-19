import os
import requests
import json
import re
import sys
import time

tokenku = []
def banner():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")


def login3():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cookie.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get(
                f'https://graph.facebook.com/me?fields=id,name&access_token={tokenku[0]}',
                cookies={'cookie': cok}
            )
            user_data = sy.json()
            sy2 = user_data['name']
            sy3 = user_data['id']
            print(f"Login berhasil! Selamat datang")
            dump_massal()
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print("Koneksi internet bermasalah. Silakan periksa koneksi Anda.")
            exit()
    except IOError:
        login_lagi334()


def login_lagi334():
    try:
        os.system('clear')
        banner()
        cookie = input(f'  [•] Masukkan Cookie : ')
        open(".cookie.txt", "w").write(cookie)
        with requests.Session() as rsn:
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
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
                    open(".token.txt", "w").write(token)
                    print("Login berhasil! Jalankan ulang perintah.")
                else:
                    print("Gagal mendapatkan token.")
            except Exception as e:
                print(f"Kesalahan saat login: {e}")
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cookie.txt")
        print("Login gagal. Silakan coba lagi.")
        print(e)
        exit()

def dump_massal():
    try:
        token = open('.token.txt', 'r').read().strip()
        cok = open('.cookie.txt', 'r').read().strip()
    except IOError:
        print("Cookies Invalid")
        exit()
    
    target_id = input("Masukkan ID Facebook: ").strip()
    file_output = f"DUMP-{target_id}.txt"
    hasil_dump = set()
    jumlah_id = 0
    
    def dump_friends(user_id):
        nonlocal jumlah_id
        try:
            session = requests.Session()
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
            }
            params = {
                "access_token": token,
                "fields": "friends"
            }
            response = session.get(f"https://graph.facebook.com/{user_id}", headers=headers, params=params, cookies={"cookies": cok})
            data = response.json()
            
            if "friends" in data:
                for friend in data["friends"]["data"]:
                    friend_id = friend["id"]
                    friend_name = friend["name"]
                    dump_result = f"{friend_id}|{friend_name}"
                    
                    if dump_result not in hasil_dump:
                        hasil_dump.add(dump_result)
                        jumlah_id += 1  # Tambahkan jumlah ID
                        with open(file_output, "a") as f:
                            f.write(dump_result + "\n")
                return [friend["id"] for friend in data["friends"]["data"]]
            else:
                return []
        except Exception as e:
            return []
    
    antrean = [target_id]
    
    while antrean:
        current_id = antrean.pop(0)
        teman_baru = dump_friends(current_id)
        antrean.extend(teman_baru)
        print(f"\rCollect ({jumlah_id} ID)", end="", flush=True)
        time.sleep(1)
    
    print(f"\nProses dumping selesai. Total ID yang didump: {jumlah_id}")
    print(f"Hasil dumping disimpan dalam file: {file_output}")

if __name__ == "__main__":
    login3()
