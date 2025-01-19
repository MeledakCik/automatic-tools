import re
import time
from bs4 import BeautifulSoup as bs
import requests

ses = requests.Session()
head_email = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_email_10minutemail():
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

if __name__ == '__main__':
    get_email_10minutemail()
