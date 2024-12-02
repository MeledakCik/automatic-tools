import os
import re
import requests
from flask import Flask, render_template, request, redirect, url_for, session
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Global session for maintaining cookies and headers
session_requests = requests.session()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    try:
        # Fetch login page to get logintoken
        login_page = session_requests.get("https://lms.smkn4padalarang.sch.id/login/index.php", verify=False)
        logintoken_match = re.search('name="logintoken" value="(.*?)"', login_page.text)
        
        if not logintoken_match:
            return "Gagal mendapatkan logintoken, silakan coba lagi!"
        
        logintoken = logintoken_match.group(1)
        data = {
            "logintoken": logintoken,
            "username": username,
            "password": password
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

        # Send login data
        response = session_requests.post(
            "https://lms.smkn4padalarang.sch.id/login/index.php",
            data=data,
            headers=headers,
            verify=False
        )

        if 'Dashboard' in response.text:
            # Save cookies if login is successful
            cookies = session_requests.cookies.get_dict()
            session['cookies'] = cookies
            return redirect(url_for('profile'))

        return "Username atau password salah, coba lagi!"
    
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

@app.route('/profile')
def profile():
    if 'cookies' not in session:
        return redirect(url_for('home'))

    try:
        cookies = session['cookies']
        response = session_requests.get("https://lms.smkn4padalarang.sch.id/user/profile.php", cookies=cookies, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        profile_data = {}

        # Extract profile information
        for item in soup.find_all("li", class_="contentnode"):
            dt = item.find("dt")
            dd = item.find("dd")
            if dt and dd:
                key = dt.text.strip()
                value = dd.text.strip() if not dd.find("a") else dd.find("a").text.strip()
                profile_data[key] = value
        
        return render_template('profile.html', profile_data=profile_data)

    except Exception as e:
        return f"Terjadi kesalahan saat mengambil data profil: {str(e)}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
