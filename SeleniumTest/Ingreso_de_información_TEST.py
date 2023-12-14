from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el controlador del navegador (asegúrate de tener el controlador descargado y en el PATH)
driver = webdriver.Chrome()

try:
    # Abre la página web
    driver.get("file:///C:/Users/Joel%20Javier/Desktop/cv%20generator/index.html")

    # Espera hasta que la página esté completamente cargada
    WebDriverWait(driver, 10).until(EC.title_contains("Generador de CV"))

    # Ingresa información personal
    name_field = driver.find_element(By.ID, "nameField")
    name_field.send_keys("John Doe")

    contact_field = driver.find_element(By.ID, "contactField")
    contact_field.send_keys("+123456789")

    address_field = driver.find_element(By.ID, "addressField")
    address_field.send_keys("123 Main Street, City")

    # Verifica que la información ingresada sea correcta
    assert name_field.get_attribute("value") == "John Doe"
    assert contact_field.get_attribute("value") == "+123456789"
    assert address_field.get_attribute("value") == "123 Main Street, City"

    # Si llegamos aquí, la prueba se ejecutó con éxito
    print("La prueba de ingreso de información personal fue realizada con éxito.")

except Exception as e:
    # Si hubo un problema durante la ejecución de la prueba
    print(f"Hubo un problema durante la prueba: {str(e)}")

finally:
    # Cierra el navegador al finalizar
    driver.close()
