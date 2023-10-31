import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Firefox(options=firefox_options)
# Inicializa el navegador y abre WhatsApp Web
driver.get("https://web.whatsapp.com/")
# Escanea el código QR manualmente
input("Presiona enter para hacer la captura")
driver.save_screenshot("./screenshot.png")


