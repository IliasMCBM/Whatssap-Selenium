from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa el navegador y abre WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Escanea el código QR manualmente
input("Escanea el código QR y presiona Enter cuando esté listo...")

# Nombre del contacto al que deseas enviar un mensaje
contact_name = "Pablo"

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
wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')))

# Cantidad de veces que deseas enviar el mensaje "hola"
veces_a_enviar = 2

for _ in range(veces_a_enviar):
    # Escribe el mensaje "hola"
    input_box.send_keys("hola")
    # Envía el mensaje presionando Enter (opcional)
    input_box.send_keys("\n")
    time.sleep(0.5)

input("Dale enter para cerrar la ventana")