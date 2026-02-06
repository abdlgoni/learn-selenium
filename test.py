import time
from selenium import webdriver


driver = webdriver.Chrome()
try:
    print("Membuka Browser")
    driver.get("https://www.python.org")

    judul = driver.title
    print("Judul Halaman Ini {judul}")
    time.sleep(2)

    print("Pindah ke web selenium")
    driver.get("https://www.selenium.dev")
    time.sleep(2)

    print("Kembali ke halaman sebelumnya")
    driver.back()
    driver.refresh()
    time.sleep(2)
    url_now = driver.current_url
    print(f"URL saat ini {url_now}")

except Exception as e:
    print(f"Terjadi error: {e}")

finally:
    driver.quit()
    print("Browser Ditutup")