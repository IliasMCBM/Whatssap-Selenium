from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


# Inicializa el navegador y abre WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Escanea el código QR manualmente
input("Escanea el código QR y presiona Enter cuando esté listo...")

# Nombre del contacto al que deseas enviar un mensaje
contact_name = "Nizar"

# Mensaje que deseas enviar
message = "Hola, Nizar. Este es un mensaje automatizado."

# Encuentra el cuadro de búsqueda y busca el contacto
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(contact_name)
time.sleep(2)  # Espera para que se carguen los resultados de búsqueda

# Abre la conversación con el contacto
contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
contact.click()

# Escribe y envía el mensaje
input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
input_box.send_keys(message)
input_box.send_keys("\n")  # Envía el mensaje presionando Enter

# Cierra el navegador
driver.quit()

