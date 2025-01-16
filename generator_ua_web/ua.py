import requests
from bs4 import BeautifulSoup
import time  # Import time untuk delay

url = "https://whatmyuseragent.com/device/vv/vivo-x100"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "table table-striped table-hover table-bordered table-useragents"})
rows = table.find_all("tr")[1:]  # Skipping the header row

for row in rows:
    columns = row.find_all("td")
    user_agent = columns[0].text.strip()
    
    print(f"{user_agent}")
    print("")
    time.sleep(1)  # Menunggu 1 detik sebelum melanjutkan ke iterasi berikutnya
