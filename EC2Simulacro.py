from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys
import time
import schedule


a = 0
# Configura las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Ruta al controlador ChromeDriver
chrome_options.binary_location = '/usr/bin/chromium' # Reemplaza con la ruta real

# Inicia Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com/")
input("Presiona enter para hacer la captura")
driver.save_screenshot("/home/ubuntu/Whatssap-Selenium/screenshot.png")
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


time.sleep(1.5)
mensaje = input("Dime cual va a ser el mensaje a enviar")
print(f"Esperando para cargar el mensaje a enviar")
def send_message():
    for i in range(10):
        wait = WebDriverWait(driver, 10)  # Establece un tiempo máximo de espera de 10 segundos
        input_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_3Uu1_')))
        # Escribe el mensaje "hola"
        for x in mensaje:
            input_box.send_keys(x)

        # Envía el mensaje presionando Enter (opcional)
        #input_box.send_keys(Keys.RETURN)

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