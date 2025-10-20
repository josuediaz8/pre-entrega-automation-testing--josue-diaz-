from selenium import webdriver
from selenium.webdriver.common.by import By
from test_login import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def validar_titulo():

    nombre_titulo = "Swag Labs"

    titulo_actual = driver.title
    
    print(f"El titulo de la pagina es:  {titulo_actual}")

    assert nombre_titulo == titulo_actual


lista_productos = []
cantidad_productos = 0

def validar_articulos():

    global lista_productos
    global cantidad_productos

    lista_productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    cantidad_productos = len(lista_productos)

    print(f"La cantidad de productos es: {cantidad_productos}")

    return cantidad_productos
    


def listar_producto(lista_productos, cantidad_productos):

    if cantidad_productos > 0:
        nombre_primer_producto = lista_productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_primer_producto = lista_productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        
        print(f"El nombre del primer producto es: {nombre_primer_producto}")
        print(f"El  precio del primer producto es: {precio_primer_producto}")

        time.sleep(2)

    else:
        print(f"No hay productos para listar")
    
def validar_items_menu():

    elementos_menu = [
        "All Items", 
        "About", 
        "Logout", 
        "Reset App State"
    ]

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    boton_all_items = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.ID, 'inventory_sidebar_link'))
    ).text

    boton_about = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test="about-sidebar-link"]'))
    ).text

    boton_loguot = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
    ).text

    boton_reset = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.ID, 'reset_sidebar_link'))
    ).text

    #imprimimos por consola los elementos del menu
    print(f"Los Items del Menu son: {boton_all_items}, {boton_about}, {boton_loguot}, {boton_reset}")

    #Validamos que sean los correctos elemento
    assert elementos_menu[0] == boton_all_items
    assert elementos_menu[1] == boton_about
    assert elementos_menu[2] == boton_loguot
    assert elementos_menu[3] == boton_reset


 #   driver.implicitly_wait(3)

def validar_filtro_web():

    elementos_filtro = [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)"
    ]

    filtro_AtoZ = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').text
    filtro_ZtoA = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').text
    filtro_LowtoHigh = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').text
    filtro_HightoLow = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').text

    print(f"Los elementos del Filtro son: {filtro_AtoZ}, {filtro_ZtoA}, {filtro_LowtoHigh}, {filtro_HightoLow}")

    #Validamos que sean los correctos los filtros
    assert elementos_filtro[0] == filtro_AtoZ
    assert elementos_filtro[1] == filtro_ZtoA
    assert elementos_filtro[2] == filtro_LowtoHigh
    assert elementos_filtro[3] == filtro_HightoLow


login()
validar_titulo ()

if __name__ == "__main__":
    validar_articulos()
    listar_producto(lista_productos, cantidad_productos)
    validar_items_menu()
    validar_filtro_web()