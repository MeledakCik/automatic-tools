from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login():
    try:
        # Set up the WebDriver (Make sure to use the appropriate driver for your browser)
        driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
        driver.get("https://lms.smkn4padalarang.sch.id/login/index.php")

        # Wait for page to load and login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'logintoken')))

        # Get the login token
        logintoken_element = driver.find_element(By.NAME, 'logintoken')
        logintoken = logintoken_element.get_attribute("value")

        if not logintoken:
            print("Gagal mendapatkan logintoken, silakan coba lagi!")
            driver.quit()
            return
        
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys("USERNAME")
        password_input.send_keys("PASS")
        password_input.send_keys(Keys.RETURN)

        # Wait for login to complete and for the Dashboard to be visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Dashboard')))
        
        print(f"Log in Success")
        print(f"Username: 0076497918, Password: Kakangkasyaf123")
        
        try:
            driver.get("https://lms.smkn4padalarang.sch.id/login/change_password.php?id=1")

            # Wait for the password change page to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_password')))

            current_password_input = driver.find_element(By.ID, "id_password")
            new_password1_input = driver.find_element(By.ID, "id_newpassword1")
            new_password2_input = driver.find_element(By.ID, "id_newpassword2")
            
            current_password_input.send_keys('PASS')
            new_password1_input.send_keys('PASS_NEW')
            new_password2_input.send_keys('PASS_NEW')
            new_password2_input.send_keys(Keys.RETURN)

            # Wait for the page to respond after form submission
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "submitbutton")))
            
            print(f"change pass done")
            print(f"Username: USERNAME, Password: {new_password1_input}")
        except Exception as e:
            print(f"Terjadi kesalahan saat mengubah password: {str(e)}")
        
        driver.quit()
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

login()
