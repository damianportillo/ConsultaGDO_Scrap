from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.argentina.gob.ar/jefatura/innovacion-publica/expedientes")

anioexpediente = driver.find_element(By.ID,"edit-anioexpediente")
numeroexpediente = driver.find_element(By.ID,"edit-numeroexpediente") 
codigoreparticion = driver.find_element(By.ID,"edit-codigoreparticion") 

anioexpediente.send_keys("2022")
numeroexpediente.send_keys("21874523")
codigoreparticion.send_keys("DAFUP#MDS")

time.sleep(3)

boton = driver.find_element(By.ID,"edit-submit")
if boton.is_displayed():
    boton.click()
else:
    print("El botón no es interactuable")

time.sleep(5000)
