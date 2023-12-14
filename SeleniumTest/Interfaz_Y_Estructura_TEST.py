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

    # Verifica la presencia de campos de información personal
    name_field = driver.find_element(By.ID, "nameField")
    assert name_field.is_displayed()

    email_field = driver.find_element(By.ID, "mailField")
    assert email_field.is_displayed()

    # ... (repite para otros campos)

    # Verifica la presencia del botón "Generar CV"
    generate_button = driver.find_element(By.ID, "btn")
    assert generate_button.is_displayed()

    # Si llegamos aquí, la prueba se ejecutó con éxito
    print("La prueba fue realizada con éxito.")

except Exception as e:
    # Si hubo un problema durante la ejecución de la prueba
    print(f"Hubo un problema durante la prueba: {str(e)}")

finally:
    # Cierra el navegador al finalizar
    driver.close()
