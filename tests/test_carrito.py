from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#creo lista para guardar el producto agregado
producto_agregado = []

def test_agregar_producto_carrito (login_in_diver):
    
    driver = login_in_diver
        
    global producto_agregado #declaro variable global

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item") #listo los pruductos
        
    nombre_producto_clickeado = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text #obtengo el nombre del producto agregado 

    precio_producto_clickeado = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text #obtengo el precio

    producto_agregado.append(nombre_producto_clickeado) #agredo el nombre del producto a la lista para luego compararlo

    producto_agregado.append(precio_producto_clickeado) ##agredo el precio del producto a la lista para luego compararlo

    productos[0].find_element(By.TAG_NAME, "button").click() #hago clic en agregar producto
    
        
    driver.implicitly_wait(3) #espero que muestre la pagina de carrito
        
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text #encuentro el contador del carrito

    assert int(contador_carrito)  == 1

    print(f"el nombre del articulo clickeado es: {producto_agregado[0]}") #imprimo por consola nombre y luego precio
    print(f"el precio del articulo clickeado es: {producto_agregado[1]}") 

    time.sleep(2)




def test_navegar_carrito (login_in_diver):
    try:

        test_agregar_producto_carrito (login_in_diver)
        
        driver = login_in_diver

        time.sleep(2)

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() #accedo al carrito

        articulos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item") #guardo los productos en una lista

        nombre_primer_producto = articulos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text #encuentro el nombre del producto

        precio_primer_producto = articulos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_price").text #encuentro el precio del producto
        
        assert producto_agregado[0] == nombre_primer_producto #comparo el nombre del producto que guarde en variable global con el que esta actualmente en el carrito a ver si coinciden

        assert producto_agregado[1] == precio_primer_producto #comparo el precio del producto que guarde en variable global con el que esta actualmente en el carrito a ver si coinciden

        print(f"El  nombre del producto del carrito es: {nombre_primer_producto}")
        print(f"El  precio del producto del carrito es: {precio_primer_producto}")

        print(f"Se valido el producto del carrito correctamente") 

        time.sleep(2)

    except Exception as e:
         
         print(f"Error al validar el producto en el carrito: {e}")
         raise

    finally:
        
        driver.quit()    