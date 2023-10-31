from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import schedule
firefox_options = Options()
a = 0
firefox_driver_path = '/usr/bin/firefox'

geckodriver_path = '/snap/bin/geckodriver'
firefox_options.add_argument("--headless")
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_service = Service(geckodriver_path)
driver = webdriver.Firefox(service=firefox_service,options=firefox_options)
driver.get("https://web.whatsapp.com/")
input("Presiona enter para hacer la captura")
driver.save_screenshot("./screenshot.png")
input("Presiona enter cuando hayas scaneado el codigo")
#driver.save_screenshot("./screenshot2.png")

contact_name = str( input("Dame el nombre del contacto"))

# Encuentra todos los elementos de contacto por su clase
print("Conseguir el elemento del contacto")
contact_elements = driver.find_elements(By.CLASS_NAME, 'Mk0Bp')
# Filtra los elementos que tienen la segunda clase " _30scZ"
print("Filtrando los elementos por el contacto")
contact_elements = [element for element in contact_elements if " _30scZ" in element.get_attribute("class")]

print("Buscle for para buscar el contacto")
for contact_element in contact_elements:
    print(f"Iteracion nº {a} de buscar el contacto")
    a+=1
    contact_text = contact_element.text
    if contact_name in contact_text:
        contact_element.click()
        time.sleep(2)  # Espera 2 segundos para que la estructura de la página cambie
        break  # Detener el bucle cuando se encuentra el contacto


driver.save_screenshot("./screenshot2.png")



time.sleep(1.5)
mensaje = input("Dime cual va a ser el mensaje a enviar")
print(f"Esperando para cargar el mensaje a enviar")
def send_message():
    for i in range(10):
        wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
        input_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')))
        # Escribe el mensaje "hola"
        input_box.send_keys(mensaje)

        # Envía el mensaje presionando Enter (opcional)
        input_box.send_keys("\n")

    driver.close()
    print("Mensajes enviados")
print("Esperando a enviar el mensaje")
# Programa la ejecución del código a las 14:00
#schedule.every().day.at("18:23").do(send_message)

send_message()



# Ejecuta el programa en segundo plano
while True:
    schedule.run_pending()
    time.sleep(1)

driver.close()