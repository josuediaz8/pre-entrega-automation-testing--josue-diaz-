import pytest
import datetime

#lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_navegacion.py",
    "tests/test_carrito.py"
]

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + [f"--html=report-{now}.html", "--self-contained-html", "-v"]

#ejecuto main que llama a pytest_args donde estatodo concatenado
pytest.main(pytest_args)