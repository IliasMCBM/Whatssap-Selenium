from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

'''# Opciones de Chrome para ejecutar en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')'''

# Inicializa el navegador y abre WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Escanea el código QR manualmente
input("Escanea el código QR y presiona Enter cuando esté listo...")

# Nombre del contacto al que deseas enviar un mensaje
contact_name = "Ilias"

# Espera para asegurarse de que WhatsApp Web esté completamente cargado
time.sleep(2)

# Encuentra todos los elementos de contacto
contact_elements = driver.find_element(By.NAME, 'Scan me!')
print(contact_elements)





#contact_elements = driver.find



"""
# Recorre los elementos de contacto para encontrar "Nizar"
for contact_element in contact_elements:
    contact_text = contact_element.text
    if contact_name in contact_text:
        contact_element.click()
        break  # Detener el bucle cuando se encuentra el contacto

"""