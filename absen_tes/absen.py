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
        print(f"Username: USERNAME, Password: PASS")
        
        # Navigate to the attendance page
        driver.get("https://lms.smkn4padalarang.sch.id/mod/attendance/view.php?id=990")

        # Wait for the 'Submit attendance' link to be clickable
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Submit attendance"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(4)
        print("Attendance page loaded successfully")

        # Try to select the correct radio button based on the availability
        try:
            # Check if the radio button with value 117 is present
            status_116 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "id_status_116"))
            )
            status_116.click()
        except:
            # If not, check for the radio button with value 118
            try:
                status_118 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "id_status_118"))
                )
                status_118.click()
            except:
                print("No valid options found, no changes saved.")

        # Click the Save button after selecting a radio button
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "id_submitbutton"))
        )
        save_button.click()
        print("Form submitted successfully.")

        driver.quit()

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

login()
