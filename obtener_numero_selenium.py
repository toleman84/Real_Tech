#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import json


# Configurar opciones de Chrome (SE QUITA el modo headless para ver el navegador)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 🔴 SE ELIMINA PARA VER EL NAVEGADOR
chrome_options.add_argument("--start-minimized")  # 🔥 Minimiza la ventana
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Inicializar WebDriver con interfaz gráfica
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de la publicación
# url = "https://apartamento.mercadolibre.com.uy/MLU-698247590-apartamentos-en-pozo-a-4-cuadras-de-la-rambla-_JM"


def guardar_numero(numbers):
    """
    Guarda el número en el archivo 'user_id_num.json' sin eliminar los existentes.
    Si el archivo no existe o su contenido no es una lista, se crea una nueva lista.
    """
    archivo = "user_id_num.json"
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if not isinstance(datos, list):
                datos = []
    except (FileNotFoundError, json.JSONDecodeError):
        datos = []

    # agregar el número obtenido
    datos.append(numbers)

    # guardar de vuelta en el archivo
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

    print(f"Número {numbers} guardado en {archivo}")


def obtener():
    """Leer el archivo 'url.json' y procesar cada URL."""
    with open('url.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        url = item.get("link")
        # print(url)
        if url:
            obtener_numero_selenium(url)
        else:
            print("No se encontró el campo 'link' en el item", item)


def obtener_numero_selenium(url):
    """
    Abre la URL con Selenium, simula un clic en el elemento que contiene "#whatsapp"
    y extrae el número de teléfono para guardarlo en 'user_id_num.json'.
    """
    # match = None
    try:
        # Abrir la página en el navegador
        driver.get(url)
        time.sleep(2)  # Esperar a que cargue la página completamente

        # Buscar la etiqueta <use href="#whatsapp">
        whatsapp_icon = None
        icons = driver.find_elements(By.TAG_NAME, "use")
        for icon in icons:
            href = icon.get_attribute("href")
            if href and "#whatsapp" in href:
                whatsapp_icon = icon
                break  # Tomamos el primer <use> encontrado

        if whatsapp_icon:
            # Simular clic en <use> usando ActionChains
            action = ActionChains(driver)
            action.move_to_element(whatsapp_icon).click().perform()
            
            # Esperar a que la nueva página cargue
            time.sleep(5)

            # Capturar la URL después de hacer clic
            whatsapp_link = driver.current_url
            # print("Enlace de WhatsApp encontrado:", whatsapp_link)

            # Extraer el número de WhatsApp con regex
            match = re.search(r"phone=(\d+)", whatsapp_link)
            if match:
                numbers = match.group(1)
                print("Número de WhatsApp:", numbers)
                guardar_numero(numbers)
            else:
                print("No se pudo extraer el número.")
        else:
            print("No se encontró el botón de WhatsApp en la página.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    obtener()
