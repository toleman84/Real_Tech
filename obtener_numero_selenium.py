#!/usr/bin/env python3

import os
import shutil
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


def guardar_numero(numbers, user_id):
    """
    Guarda el número en el archivo 'user_id_num.json' sin eliminar los existentes.
    """
    archivo_backup = "url_backup.json" # user_id_num.json

    # agregar número
    try:
        # Cargar JSON
        with open(archivo_backup, "r", encoding="utf-8") as f:
            datos = json.load(f)

        # Verificar si la clave "numero" existe y actualizarla
        actualizado = False
        for item in datos:
            if item.get("user_id") == user_id:
                print(f"Actualizando número para user_id {user_id}: {numbers}")
                item["numero"] = int(numbers)
                actualizado = True
                break # Una vez encontrado y actualizado, salimos del loop

        if actualizado:
            # Guardar los cambios en el archivo original
            with open(archivo_backup, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
                print(f"Archivo actualizado correctamente: {archivo_backup}")

        else:
            print(f"⚠ No se encontró el user_id {user_id} en el JSON.")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Error al procesar el archivo JSON: {e}")


def obtener():
    """Leer el archivo 'url.json', hacer backup y procesar cada URL."""
    archivo_original = "url.json"
    archivo_backup = "url_backup.json"

    # Crear copia de seguridad SOLO UNA VEZ antes de empezar
    if os.path.exists(archivo_original):
        shutil.copy(archivo_original, archivo_backup)
        print(f"📂 Copia de seguridad creada: {archivo_backup}")

    # Leer el JSON de la copia de seguridad
    with open(archivo_backup, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        url = item.get("link")
        user_id = item.get("user_id")

        if url and user_id:
            obtener_numero_selenium(url, user_id)
        else:
            print(f"Faltan datos en el item: {item}")


def obtener_numero_selenium(url, user_id):
    """
    Abre la URL con Selenium, simula un clic en el elemento que contiene "#whatsapp"
    y extrae el número de teléfono para guardarlo en 'user_id_num.json'.
    """
    # match = None
    try:
        # Abrir la página en el navegador
        driver.get(url)
        time.sleep(5)  # Esperar a que cargue la página completamente

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
                print(f"✅ WhatsApp encontrado para {user_id}: {numbers}")
                guardar_numero(numbers, user_id)
            else:
                print("No se pudo extraer el número.")
        else:
            print("No se encontró el botón de WhatsApp en la página.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    obtener()
