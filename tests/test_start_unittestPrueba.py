import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartUnittestPrueba(unittest.TestCase):
    """Clase de prueba para validaciones básicas"""
    
    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        # Crear una nueva instancia del navegador Microsoft Edge
        self.driver = webdriver.Edge()
        
    def test_example(self):
        """Caso de prueba de ejemplo"""
        # Navegar a una URL
        self.driver.get("https://idkjose.github.io/PaginaPruebas/")
        
        # Agregar validaciones aquí
        self.assertIn("Pagina", self.driver.title)
        
    def tearDown(self):
        """Limpieza después de cada prueba"""
        # Cerrar el navegador
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
