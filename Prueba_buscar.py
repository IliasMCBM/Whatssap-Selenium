from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa el navegador y abre WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Escanea el código QR manualmente
input("Escanea el código QR y presiona Enter cuando esté listo...")

# Nombre del contacto al que deseas enviar un mensaje
contact_name = "Ilias"

# Espera para asegurarse de que WhatsApp Web esté completamente cargado
time.sleep(5)

# Encuentra todos los elementos de contacto por su clase
contact_elements = driver.find_elements(By.CLASS_NAME, 'Mk0Bp')
# Filtra los elementos que tienen la segunda clase " _30scZ"
contact_elements = [element for element in contact_elements if " _30scZ" in element.get_attribute("class")]

for contact_element in contact_elements:
    contact_text = contact_element.text
    if contact_name in contact_text:
        contact_element.click()
        time.sleep(2)  # Espera 2 segundos para que la estructura de la página cambie
        break  # Detener el bucle cuando se encuentra el contacto
input("Dale enter para cerrar la ventana")