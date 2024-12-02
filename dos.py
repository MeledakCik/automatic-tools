import requests,re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()

def login():
    try:
        p = session.get("https://lms.smkn4padalarang.sch.id/login/index.php", verify=False)
        logintoken_match = re.search('name="logintoken" value="(.*?)"', str(p.text))
        if not logintoken_match:
            print("Gagal mendapatkan logintoken, silakan coba lagi!")
            return
        logintoken = logintoken_match.group(1)
        header = {
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
            "username": "0076497918",
            "password": "Kakangkasyaf123"
        }
        response = session.post(
            "https://lms.smkn4padalarang.sch.id/login/index.php",
            headers=header,
            data=data,
            allow_redirects=True,
            verify=False
        )

        if 'Dashboard' in response.text:
            cookies = "; ".join([
                f"{key}={value}"
                for key, value in session.cookies.get_dict().items()
            ])
            print(f"Log in Success")
            print(f"Username: 0076497918, Password: Kakangkasyaf123")
            print(f"{cookies}")
            try:
                url = "https://lms.smkn4padalarang.sch.id/login/change_password.php?id=1"
                heade = {
                    'Host':'lms.smkn4padalarang.sch.id',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Cookie': cookies,
                    'Referer': 'https://lms.smkn4padalarang.sch.id/user/preferences.php?userid=228&course=1',
                    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                    'Sec-Ch-Ua-Mobile': '?0',
                    'Sec-Ch-Ua-Platform': '"Windows"',
                    'Upgrade-Insecure-Requests': '1',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
                }
                password_change_payload = {
                    'sesskey': 'ArwHAUPPR5',
                    '_qf__login_change_password_form': '1',
                    'id': '1',
                    'password': 'Kakangkasyaf123',  # Password lama
                    'newpassword1': 'Kakangkasyaf321',  # Password baru
                    'newpassword2': 'Kakangkasyaf321',  # Konfirmasi password baru
                    'submit': 'submitbutton'
                }
                change_response = session.post(url, data=password_change_payload,headers=heade,verify=False)
                if change_response.status_code == 200:
                    print("Password berhasil diubah.")
                else:
                    print("Gagal mengubah password. Periksa kembali.")
            except Exception as e:
                print("Terjadi kesalahan: {str(e)}")
        else:
            print("Username atau password salah, coba lagi!")
    except Exception as e:
        print("Terjadi kesalahan: {str(e)}")
        
        
login()