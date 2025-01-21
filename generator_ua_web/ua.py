import re

def extract_device_model_language_and_dpi(user_agents):
    """
    Fungsi untuk mengekstrak model perangkat, bahasa, dan DPI dari daftar User-Agent.
    
    Args:
        user_agents (list): Daftar User-Agent berbentuk string.
        
    Returns:
        tuple: Enam list:
            - android_models: Model perangkat Android.
            - ios_models: Model perangkat iOS.
            - android_langs: Bahasa (locale) pada perangkat Android.
            - ios_langs: Bahasa (locale) pada perangkat iOS.
            - android_dpis: DPI pada perangkat Android.
            - ios_dpis: DPI pada perangkat iOS.
    """
    if not isinstance(user_agents, list):
        raise ValueError("Input harus berupa list dari string User-Agent.")
    
    android_models = []
    ios_models = []
    android_langs = []
    ios_langs = []
    android_dpis = []
    ios_dpis = []
    
    # Pola regex untuk model, bahasa, dan DPI
    pattern = r"(?:Android.*?;\s([\w\-]+).*?([a-z]{2}_[A-Z]{2}).*?(\d{2,4}dpi)|iPhone.*?\((iPhone[\w,]+).*?([a-z]{2}_[A-Z]{2}).*?(\d{2,4}dpi))"

    for ua in user_agents:
        if not isinstance(ua, str):
            android_models.append("User-Agent tidak valid")
            ios_models.append("User-Agent tidak valid")
            android_langs.append("User-Agent tidak valid")
            ios_langs.append("User-Agent tidak valid")
            android_dpis.append("User-Agent tidak valid")
            ios_dpis.append("User-Agent tidak valid")
            continue
        
        match = re.search(pattern, ua)
        if match:
            model = match.group(1) or match.group(4)
            lang = match.group(2) or match.group(5)
            dpi = match.group(3) or match.group(6)
            
            if "Android" in ua:
                android_models.append(model)
                android_langs.append(lang)
                android_dpis.append(dpi or "DPI tidak ditemukan")
            elif "iPhone" in ua:
                ios_models.append(model)
                ios_langs.append(lang)
                ios_dpis.append(dpi or "DPI tidak ditemukan")
        else:
            android_models.append("Model tidak ditemukan")
            ios_models.append("Model tidak ditemukan")
            android_langs.append("Bahasa tidak ditemukan")
            ios_langs.append("Bahasa tidak ditemukan")
            android_dpis.append("DPI tidak ditemukan")
            ios_dpis.append("DPI tidak ditemukan")
        
    return android_models, ios_models, android_langs, ios_langs, android_dpis, ios_dpis

# Membaca User-Agent dari file
def read_user_agents_from_file(file_path):
    """
    Membaca User-Agent dari file teks.
    
    Args:
        file_path (str): Path file teks yang berisi User-Agent.
        
    Returns:
        list: Daftar User-Agent.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            user_agents = [line.strip() for line in file if line.strip()]
        return user_agents
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

# Path file User-Agent
file_path = "user_agents.txt"

# Membaca User-Agent dari file
user_agents = read_user_agents_from_file(file_path)

# Menjalankan fungsi
if user_agents:
    android_models, ios_models, android_langs, ios_langs, android_dpis, ios_dpis = extract_device_model_language_and_dpi(user_agents)
    
    # Menggabungkan hasil dengan format "merek1", "merek2"
    android_string = ", ".join(f'"{model}"' for model in android_models)
    ios_string = ", ".join(f'"{model}"' for model in ios_models)
    lang_andro_string = ", ".join(f'"{lang}"' for lang in android_langs)
    lang_ios_string = ", ".join(f'"{lang}"' for lang in ios_langs)
    dpi_andro_string = ", ".join(f'"{dpi}"' for dpi in android_dpis)
    dpi_ios_string = ", ".join(f'"{dpi}"' for dpi in ios_dpis)
    
    print(f"Versi Android:\n{android_string}")
    print(f"Versi iOS:\n{ios_string}")
    print(f"Bahasa Android:\n{lang_andro_string}")
    print(f"Bahasa iOS:\n{lang_ios_string}")
    print(f"DPI Android:\n{dpi_andro_string}")
    print(f"DPI iOS:\n{dpi_ios_string}")
else:
    print("Tidak ada User-Agent untuk diproses.")
