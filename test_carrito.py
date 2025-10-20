from selenium import webdriver
from selenium.webdriver.common.by import By
from test_login import *
from test_navegacion import *
import time

#creo lista para guardar el producto agregado
producto_agregado = []

def agregar_producto_carrito ():
    #valido que hayan productos
    if validar_articulos() > 0:
        
        global producto_agregado

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        nombre_producto_clickeado = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text

        precio_producto_clickeado = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

        producto_agregado.append(nombre_producto_clickeado)

        producto_agregado.append(precio_producto_clickeado)

        productos[0].find_element(By.TAG_NAME, "button").click()
    
        
        driver.implicitly_wait(3)
        
        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        assert int(contador_carrito)  == 1

        print(f"el nombre del articulo clickeado es: {producto_agregado[0]}")
        print(f"el precio del articulo clickeado es: {producto_agregado[1]}") 

        time.sleep(2)

    else:
        print("No hay productos para agr")


def navegar_carrito (producto_agregado):

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    articulos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

    nombre_primer_producto = articulos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    precio_primer_producto = articulos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    
    assert producto_agregado[0] == nombre_primer_producto

    assert producto_agregado[1] == precio_primer_producto

    print(f"El  nombre del producto del carrito es: {nombre_primer_producto}")
    print(f"El  precio del producto del carrito es: {precio_primer_producto}")

    time.sleep(2)

agregar_producto_carrito ()
navegar_carrito (producto_agregado)