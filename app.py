from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

password = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
username = driver.find_element(By.ID, "username")

login_btn.click()
username.send_keys("admin")
password.send_keys("12345")
