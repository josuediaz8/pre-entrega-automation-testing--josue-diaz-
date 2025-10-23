from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_validar_titulo(login_in_diver):
    try:
            
        driver = login_in_diver

        nombre_titulo = "Swag Labs"

        titulo_actual = driver.title #obtengo el titulo de la pagina
        
        print(f"El titulo actual de la pagina es:  {titulo_actual}") #muestro por consola el titulo actual

        assert nombre_titulo == titulo_actual #valido que sean iguales

    except Exception as e:
         
         print(f"Error al validar el titulo: {e}")
         raise

    finally:
        
        driver.quit()


def test_validar_articulos(login_in_diver):
    
    try:
        driver = login_in_diver

        lista_productos = driver.find_elements(By.CLASS_NAME, "inventory_item") #obtengo todos los productos de la pagina

        cantidad_productos = len(lista_productos) #obtengo la cantidad de productos

        assert cantidad_productos > 0, "No hay productos visibles en la web"

        print(f"La cantidad de productos es: {cantidad_productos}") #muestro por consola la cantidad

    except Exception as e:
         
         print(f"Error al validar si hay articulos: {e}")
         raise

    finally:
        
        driver.quit()



def test_listar_producto(login_in_diver):
  
    driver = login_in_diver

    time.sleep(2)

    lista_productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    nombre_primer_producto = lista_productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text #obtengo el nombre del primer producto
    precio_primer_producto = lista_productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text #obtengo el precio del primer producto
        
    print(f"El nombre del primer producto es: {nombre_primer_producto}") #muestro por consola nombre y luego precio
    print(f"El  precio del primer producto es: {precio_primer_producto}")




def test_validar_items_menu(login_in_diver):
    try:
        driver = login_in_diver
        #guardo en lista los elementos del menu para luego comparar
        elementos_menu = [
            "All Items", 
            "About", 
            "Logout", 
            "Reset App State"
        ]

        driver.find_element(By.ID, "react-burger-menu-btn").click() #hago click en el boton del menu para activar los items

        #espera explicita
        wait = WebDriverWait(driver, 10)
        
        #espera hasta que este visible para capturar el nombre de los items del menu
        boton_all_items = wait.until(EC.visibility_of_element_located((By.ID, 'inventory_sidebar_link'))).text

        boton_about = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-test="about-sidebar-link"]'))).text

        boton_loguot = wait.until(EC.visibility_of_element_located((By.ID, 'logout_sidebar_link'))).text

        boton_reset = wait.until(EC.visibility_of_element_located((By.ID, 'reset_sidebar_link'))).text

        #imprimimos por consola los elementos del menu
        print(f"Los Items del Menu son: {boton_all_items}, {boton_about}, {boton_loguot}, {boton_reset}")

        #Validamos que sean los correctos elemento
        assert elementos_menu[0] == boton_all_items
        assert elementos_menu[1] == boton_about
        assert elementos_menu[2] == boton_loguot
        assert elementos_menu[3] == boton_reset

    except Exception as e:
         
         print(f"Error al validar los Items del Menu: {e}")
         raise

    finally:
        
        driver.quit()


def test_validar_filtro_web(login_in_diver):
    try: 
        driver = login_in_diver
        
        #guardo en lista los elementos del filtro para luego comparar
        elementos_filtro = [
            "Name (A to Z)",
            "Name (Z to A)",
            "Price (low to high)",
            "Price (high to low)"
        ]

        #acceso a cada elemento del filtro por XPath
        filtro_AtoZ = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').text
        filtro_ZtoA = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').text
        filtro_LowtoHigh = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').text
        filtro_HightoLow = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').text

        #muestro por consola 
        print(f"Los elementos del Filtro son: {filtro_AtoZ}, {filtro_ZtoA}, {filtro_LowtoHigh}, {filtro_HightoLow}") 

        #Validamos que sean los correctos los filtros
        assert elementos_filtro[0] == filtro_AtoZ
        assert elementos_filtro[1] == filtro_ZtoA
        assert elementos_filtro[2] == filtro_LowtoHigh
        assert elementos_filtro[3] == filtro_HightoLow
    
    except Exception as e:
         
         print(f"Error al validar el filtro de la web: {e}")
         raise

    finally:
        
        driver.quit()