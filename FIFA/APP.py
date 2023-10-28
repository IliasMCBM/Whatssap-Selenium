from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
# Credenciales de inicio de sesión (ajusta esto)
usuario = 'iliasamchichou@gmail.com'
contrasena = 'Ilias2004$'
precio='34000'
# Nombre del jugador que quieres fichar (ajusta esto)
nombre_jugador = 'Casemiro'

# Inicializar el controlador del navegador
driver = webdriver.Chrome()

# Abrir la página de la web app de FIFA
driver.get('https://www.ea.com/es-es/fifa/ultimate-team/web-app/')
    #input('Presiona Enter para continuar...')
time.sleep(5)
# Esperar a que el botón de inicio de sesión aparezca
login_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'btn-standard.call-to-action'))
)
login_btn.click()
    #input('Presiona Enter para continuar...')
time.sleep(0.2)
# Iniciar sesión
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
)
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
)
    #input('')
time.sleep(0.2)
username_input.send_keys(usuario)
    #input('Hola')
time.sleep(0.2)
password_input.send_keys(contrasena)
password_input.send_keys(Keys.RETURN)
input('Entrada al mercado')
# Acceder a la pestaña de "Mercado"
tienda_btn = driver.find_element(By.XPATH, '/html/body/main/section/nav/button[3]')
tienda_btn.click()
time.sleep(0.5)
#input('Entrada a transferibles')

# Acceder a la búsqueda en el mercado
buscar_btn = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]')
buscar_btn.click()
time.sleep(1)
#input('Meter nombre')
# Ingresar el nombre del jugador en el campo de búsqueda
nombre_input = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input')
nombre_input.send_keys(nombre_jugador)
#input('Seleccionar jugador')
time.sleep(1)
nombre_click = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button')
nombre_click.click()
#input('Meter puja maxima')
Precio_max = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input')
Precio_max.send_keys(precio)

#input('Meter precio')
# Ingresar el nombre del jugador en el campo de búsqueda
Precio_max = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
Precio_max.send_keys('35000')
time.sleep(1)
input('Prueba')
#input('Buscar')
# Hacer clic en el botón de búsqueda
buscar = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')
buscar.click()
for i in range(10):
    try:
        elemento1 = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]')
        # Si el elemento existe, haces clic en el botón de comprar correspondiente
        boton_comprar = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
        boton_comprar.click()
        input('')
    except NoSuchElementException:
        # Si el elemento con el primer XPath no existe, haces clic en los otros botones
        try:
            boton_alternativo1 = driver.find_element(By.XPATH, '/html/body/main/section/section/div[1]/button[1]')
            boton_alternativo1.click()
            time.sleep(0.2)  # Puedes agregar una pausa para esperar que cargue la página
            # Encuentra el elemento con el XPath dado
            elemento = driver.find_element(By.XPATH,
                                           '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input')

            # Verifica si el texto del elemento es igual a '200'
            if elemento.get_attribute('value') == '200':
                # Asigna el valor de la variable 'precio' al elemento
                driver.execute_script(f"arguments[0].value = '{precio}';", elemento)
            # Encuentra y hace clic en el botón con el XPath dado
            boton = driver.find_element(By.XPATH,
                                        '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/button[1]')
            boton.click()
            boton_alternativo2 = driver.find_element(By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')
            boton_alternativo2.click()


            time.sleep(0.75)


        except NoSuchElementException:
            print("Ninguno de los elementos esperados se encontró en la página.")

# Esperar para cargar los resultados de la búsqueda (ajusta el tiempo según tu conexión)
time.sleep(10)
input('Terminado')
# Fichar al jugador (ajusta esto según la interfaz de la web app)
# Por ejemplo, hacer clic en el primer resultado
try:
    fichar_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Fichar")]')
    fichar_btn.click()
except Exception as e:
    print("No se encontró el botón de fichar:", e)

# Maneja posibles errores, como la falta de fondos o problemas en la página

# Cerrar sesión
driver.get('https://www.ea.com/es-es/fifa/ultimate-team/web-app/logout')
time.sleep(2)

# Cierra el navegador
driver.quit()
