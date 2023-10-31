from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
import schedule




firefox_options = Options()
firefox_binary = "/usr/bin/firefox"
firefox_options.binary_location = firefox_binary

geckodriver_path = '/snap/bin/geckodriver'
firefox_options.add_argument("--headless")
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_service = Service(geckodriver_path)
driver = webdriver.Firefox(service=firefox_service,options=firefox_options)
input("Presiona enter para hacer la captura")
driver.save_screenshot("./screenshot.png")
input('Avisa cuando estes listo')

contact_name = str(input("Dame el nombre del contacto"))

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
time.sleep(1.5)
mensaje = input("Dime cual va a ser el mensaje a enviar")

for i in range(10):
    wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
    input_box = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, '_3Uu1_')))

    # Escribe el mensaje "hola"
    for x in mensaje:
        input_box.send_keys(x)

# Envía el mensaje presionando Enter (opcional)
    input_box.send_keys(Keys.RETURN)
input('Cerrar')
driver.close()
print("Mensajes enviados")


# Programa la ejecución del código a las 14:00


# Ejecuta el programa en segundo plano
while True:
    schedule.run_pending()
    time.sleep(1)

driver.close()