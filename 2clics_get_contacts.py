#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

def get_contacts():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 🔴 SE ELIMINA PARA VER EL NAVEGADOR
    chrome_options.add_argument("--start-minimized")  # 🔥 Minimiza la ventana
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://app.2clics.uy/contactos")
    time.sleep(5)  # Esperar carga de la página
    
    contacts = {}
    contact_links = driver.find_elements(By.CSS_SELECTOR, "td_address")
    
    for link in contact_links:
        contact_name = link.text
        contact_url = link.get_attribute("href")
        contact_id = contact_url.split("/")[-1]
        
        # Ir a la página de contacto para obtener el agente asignado
        driver.get(contact_url)
        time.sleep(3)  # Esperar carga
        
        try:
            agent_name = driver.find_element(By.CSS_SELECTOR, "h6.m_hide").text.split("\n")[0].strip()
        except:
            agent_name = "Desconocido"
        
        try:
            phone_number = driver.find_element(By.CSS_SELECTOR, "span.ng-star-inserted").text.strip()
        except:
            phone_number = "No disponible"
        
        if agent_name in contacts:
            contacts[agent_name].append(phone_number)
        else:
            contacts[agent_name] = [phone_number]
        
        driver.back()
        time.sleep(3)  # Volver a la lista de contactos
    
    driver.quit()
    
    with open("2clics_contactos.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

    print("Datos guardados en contactos.json")

if __name__ == "__main__":
    get_contacts()
