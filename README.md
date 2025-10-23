# Pre Entrega Automation Testing Josue Diaz

> Practicas sobre pruebas automatizadas de la web https://www.saucedemo.com/

## Propósito del proyecto

Realizar practicas de automatizacion de pruebas en un sitio web, como parte de la Pre Entrega del trabajo final del curso de Testing Automation, en el cual hasta ahora hemos aprendido a hacer pruebas con Pytest, Selenium, generar reportes, etc.

En este proyecto se automatizan las siguientes pruebas:
- Sitio web:  https://www.saucedemo.com/
- Ingreso al login
- Validar titulo de la pagina
- Validar que existan articulos disponibles
- Validar los elementos del Menu correctamente
- Validar el filtro de la pagina
- Validar que se pueda agregar un producto al carrito
- Validar que se incremente el carrito de compra
- Validar que el producto agregado al carrito sea el correcto

## Tecnologías utilizadas

- Visual Studio Code: editor de código fuente gratuito, ligero y potente que se ejecuta en Windows, macOS y Linux.
- Python: Lenguaje de programación utilizado para crear scripts que ejecutan pruebas automáticamente en aplicaciones de software, en lugar de realizar el proceso manualmente
- Selenium WebDriver: Herramienta para automatizar pruebas de navegadores web, permitiendo simular acciones del usuario real.
- Pytest: Framework de pruebas en Python que facilita la escritura y ejecución de casos de prueba automáticos.

## Instrucciones de instalación de dependencias

- Visual Studio Code: desde https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Pytest: Dentro del Visual Studio Code, abra su terminal o símbolo del sistema, ejecute el comando: pip install pytest
- Selenium: Dentro del Visual Studio Code, abra su terminal o símbolo del sistema,ejecuta el comando: pip install selenium
- Generacion de Reportes: Dentro del Visual Studio Code, abra su terminal o símbolo del sistema, ejecuta el comando: pip install pytest-htm

## Comando para ejecutar las pruebas 
- py -m pytest -v .\tests\test_login.py
- py -m pytest -v .\tests\test_navegacion.py
- py -m pytest -v .\tests\test_carrito.py
- Ejecutar Reporte: py -m pytest .\tests\test_login.py -v --html=reporte.html
- O ir al archivo run_test.py y ejecutar el archivo directamente (boton play), el cual ejecutara los 3 archivos, uno tras otro y generara el reporte al finalizar con la fecha y hora

👤 **Autor**
- Josue Diaz
- GitHub: https://github.com/josuediaz8/
