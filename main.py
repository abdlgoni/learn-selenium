import time
from selenium import webdriver

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

options.add_experimental_option("detach", True)
try:
    # 2. Buka Website
    print("Membuka browser...")
    driver.get("https://www.google.com")
    driver.maximize_window() # Perbesar layar

    # 3. Interaksi Sederhana (Contoh: Ketik 'Selenium Python' lalu Enter)
    # Mencari kotak pencarian berdasarkan nama elemen 'q'
    search_box = driver.find_element(By.NAME, "q")
    
    # Ketik keyword
    search_box.send_keys("Youtube")
    
    # Tunggu sebentar agar kita bisa melihat hasilnya (hanya untuk demo)
    time.sleep(2)
    
    # Tekan Enter (submit form)
    search_box.submit()
    
    print("Berhasil melakukan pencarian!")
    
    # Tahan sebentar sebelum script lanjut (atau gunakan input() untuk pause)
    input("Tekan Enter di terminal untuk menutup browser...")

except Exception as e:
    print(f"Terjadi error: {e}")

finally:
    # 4. Tutup Browser
    driver.quit()
    print("Browser ditutup.")