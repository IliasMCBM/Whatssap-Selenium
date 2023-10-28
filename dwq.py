import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.cdc.gov/nchs/pressroom/sosmap/flu_pneumonia_mortality/flu_pneumonia.htm')
driver.implicitly_wait(5)

year_list = ["2017", "2018", "2019", "2020", "2021"]


# EL SELECTOR DE AÑOS LO TIENEN BIEN HECHO PARA QUE SOLO SE PUEDA ACCEDER A SU REFRESCO VÍA CLICK
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "Year")))
time.sleep(1)
year_selector = driver.find_element(By.NAME, "Year")
selected_year = year_selector.get_attribute("value")
print(f"El año {selected_year} es el preseleccionado")

dfs = []

for year in year_list:

  year_selector = driver.find_element(By.NAME, "Year")
  time.sleep(1)
  year_selector = Select(year_selector)

  try:

    year_selector.select_by_value(year)
    table_html = driver.find_elements(By.CLASS_NAME, 'table-container')[0].get_attribute("innerHTML")

    year_df = pd.read_html(table_html)[0]
    year_df["year"] = year
    dfs.append(year_df)

  except Exception as e:
    print(f"Error al leer el año {year}: {e}")

df_influenza = pd.concat(dfs)
df_influenza.columns = ["state", "influenza_death_rate", "influenza_deaths", "year"]
df_influenza.head()