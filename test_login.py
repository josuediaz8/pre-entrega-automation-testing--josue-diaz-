from selenium import webdriver
from selenium.webdriver.common.by import By #para poder llamar por By a los elementos, es como un acceso rapido
import time

driver = webdriver.Chrome() #iniciamos una variable por navegador

driver.get("https://www.saucedemo.com/") # abre la pagina web


def login ():
     
     try:
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user") #encuentro por ID y le escribo el nombre de usuario
        
        driver.find_element(By.NAME, "password").send_keys("secret_sauce") #encuentro por NAME y le escribo el nombre de usuario
        
        time.sleep(2) #espero 2 seg

        boton_login = driver.find_element(By.XPATH, "//*[@id='login-button']") #encuentro por XPath
        
        boton_login.click() #hago click en el boton de login

        time.sleep(3) #esperamos 3 segundos
     
     except Exception as e:
         
         print(f"Error al iniciar sesion: {e}") #en caso de error muestra msj por consola

    # finally:
     #   driver.quit()



def validar_url():
    
    url_actual = driver.current_url

    print(f"La url actual es: {url_actual}")

    assert 'inventory.html' in url_actual




if __name__ == "__main__": #se ejcucuta solo cuando se llama el propio archivo
   
   login ()
   validar_url()