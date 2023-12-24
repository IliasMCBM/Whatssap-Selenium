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
contacto = ""
mensaje = ""
cerrar = ""

# Encuentra todos los elementos de contacto por su clase
time.sleep(1.5)
def principal(cantidad):
    for i in range(cantidad):
        wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')))
        # Escribe el mensaje "hola"
        input_box.send_keys(mensaje)

        # Envía el mensaje presionando Enter (opcional)
        input_box.send_keys("\n")


while cerrar != "s":
    contacto = input("Dime a quíen se lo quieres enviar\n")
    mensaje = input("Dime el mensaje a enviar\n")
    contact_elements = driver.find_elements(By.CLASS_NAME, 'Mk0Bp')
    contact_elements = [element for element in contact_elements if " _30scZ" in element.get_attribute("class")]
    encontrados = []
    for contact_element in contact_elements:
        contact_text = contact_element.text
        encontrados.append(contact_text)
        if contacto in contact_text:
            confirmar = input(f"Se ha encontrado el siguiente contacto: {contact_text}\n ¿Enviar mensaje?(s)")
            if confirmar == "s":
                contact_element.click()
                time.sleep(1)
                break
    principal(int(input("Dime la cantidad de mensajes que quieres enviar\n")))
    cerrar = input("Quieres cerrar el programa? (s para confirmar)\n")

input("Dale enter para cerrar la ventana")
driver.close()