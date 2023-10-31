from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import schedule

# Configura las opciones de Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_binary = "/usr/bin/firefox"
firefox_options.binary_location = firefox_binary

# Configura el servicio de Geckodriver
geckodriver_path = '/snap/bin/geckodriver'
firefox_service = Service(geckodriver_path)

# Inicia Firefox
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)


# Abre la página de WhatsApp Web
driver.get("https://web.whatsapp.com/")
print('WhatsApp Web cargado')

# Configura el nombre del contacto
contact_name = input("Dame el nombre del contacto: ")

# Encuentra todos los elementos de contacto por su clase
wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
contact_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'Mk0Bp')))

# Filtra los elementos que tienen la segunda clase " _30scZ"
contact_elements = [element for element in contact_elements if " _30scZ" in element.get_attribute("class")]

# Encuentra el elemento de contacto con el nombre especificado
for contact_element in contact_elements:
    contact_text = contact_element.text
    if contact_name in contact_text:
        contact_element.click()
        print(f'Contacto "{contact_name}" seleccionado')
        break

# Configura el mensaje a enviar
mensaje = input("Dime cuál va a ser el mensaje a enviar: ")

# Envía el mensaje 10 veces
for i in range(10):
    wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
    input_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_3Uu1_')))

    # Escribe el mensaje
    input_box.send_keys(mensaje)

    # Envía el mensaje presionando Enter
    input_box.send_keys(Keys.RETURN)

# Cierra Firefox
driver.quit()
print("Mensajes enviados")
