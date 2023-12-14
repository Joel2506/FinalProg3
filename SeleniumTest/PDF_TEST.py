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

    # Ingresa información personal (puedes adaptar esto a tus necesidades)
    driver.find_element(By.ID, "nameField").send_keys("Nombre Completo")
    driver.find_element(By.ID, "mailField").send_keys("correo@example.com")
    driver.find_element(By.ID, "contactField").send_keys("+123456789")
    driver.find_element(By.ID, "langField").send_keys("Inglés, Español")
    driver.find_element(By.ID, "addressField").send_keys("Dirección de prueba")

    # Ingresa información profesional (puedes adaptar esto a tus necesidades)
    driver.find_element(By.ID, "educationField").send_keys("Educación de prueba")
    driver.find_element(By.ID, "workField").send_keys("Experiencia de prueba")
    driver.find_element(By.ID, "skillsField").send_keys("Habilidades de prueba")
    driver.find_element(By.ID, "pagField").send_keys("https://www.ejemplo.com")
    driver.find_element(By.ID, "cerField").send_keys("Certificación de prueba")
    driver.find_element(By.ID, "resumeField").send_keys("Resumen de prueba")

    # Simula la generación del CV
    driver.find_element(By.ID, "btn").click()

    # Imprime un mensaje indicando que la prueba fue realizada con éxito
    print("La prueba de generación de CV fue realizada con éxito.")

except Exception as e:
    # Imprime un mensaje indicando que hubo un problema durante la prueba
    print(f"Hubo un problema durante la prueba: {str(e)}")

finally:
    # Cierra el navegador al finalizar
    driver.close()
