from selenium.webdriver.common.by import By #para poder llamar por By a los elementos, es como un acceso rapido



def test_login_validacion(login_in_diver):

    try:
        
        driver = login_in_diver

        url_actual = driver.current_url

        print(f"La url actual es: {url_actual}")

        assert 'inventory.html' in url_actual, "No se redirigio a la pagina de inventario"

    except Exception as e:
         
         print(f"Error al validar la sesion: {e}")

    finally:
        
        driver.quit()