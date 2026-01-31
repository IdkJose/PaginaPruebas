import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Heredar de unittest.TestCase [cite: 120]
class FindByIdName(unittest.TestCase):

    # Método de inicio de prueba (Setup) [cite: 125]
    def setUp(self):
        # Crear una nueva instancia del navegador (Edge o Chrome) [cite: 137]
        # Nota: Asegúrate de tener el driver instalado o usa webdriver.Chrome() si prefieres
        self.driver = webdriver.Edge()

        # Navegar a la web (AQUÍ PEGAS TU URL DE GITHUB PAGES) [cite: 139]
        self.driver.get("https://idkjose.github.io/PaginaPruebas/")

    # Caso de prueba 1: Buscar por ID [cite: 141]
    def testIdName(self):
        # Busca un elemento cuyo ID sea "noImportante" [cite: 142]
        elemento = self.driver.find_element(By.ID, "noImportante")

        if elemento is not None:
            print("El elemento by ID fue encontrado")

    # Caso de prueba 2: Buscar por Name (según página 4) [cite: 185]
    def testName(self):
        # Busca el elemento cuyo atributo NAME sea "ultimo" [cite: 188]
        elemento2 = self.driver.find_element(By.NAME, "ultimo")

        if elemento2 is not None:
            print("El elemento by NAME fue encontrado")

    # Método para cerrar el driver (Teardown) [cite: 382]
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()